#!/usr/bin/env python3

import aiko_services as aiko
from abc import ABC, abstractmethod
import multiprocessing as mp

class ChatRouter(aiko.Actor):
    def __init__(self, context):
        context.call_init(self, "Actor", context)
        print(f"MQTT topic: {self.topic_in}")

    def aloha(self, msg):
        self.logger.info(f"Router received: {msg}")

        known_users = ["alice", "bob"]

        for usr in known_users:
            if f"@{usr}" in msg:
                reroute(usr, msg)

class AbstractUser(aiko.Actor, ABC):
    @abstractmethod
    def aloha(self, name):
        pass

def reroute(usr, msg):
    # Spawns a new process that calls the command and then terminates
    # to workaround bug where multiple do_command calls seem to get queued rather than executed
    ctx = mp.get_context('spawn')
    process = ctx.Process(target=reroute_worker, args=(usr, msg))
    process.start()
    process.join()

def reroute_worker(usr, msg):
    import aiko_services as aiko

    aiko.do_command(
        AbstractUser,
        aiko.ServiceFilter("*", usr, "*", "*", "*", "*"),
        lambda router: router.aloha(msg),
        terminate=True)
    
    aiko.process.run()

if __name__ == "__main__":
    init_args = aiko.actor_args("chatrouter")
    router = aiko.compose_instance(ChatRouter, init_args)
    aiko.process.run()
