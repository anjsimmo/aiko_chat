#!/usr/bin/env python3

import aiko_services as aiko
from abc import ABC, abstractmethod

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
    def aloha(self, msg):
        pass

def reroute(usr, msg):
    # BUG: works the first time, but subsequent calls seem to just queue the command
    aiko.do_command(
        AbstractUser,
        aiko.ServiceFilter("*", usr, "*", "*", "*", "*"),
        lambda router: router.aloha(msg),
        terminate=False)

if __name__ == "__main__":
    init_args = aiko.actor_args("chatrouter")
    router = aiko.compose_instance(ChatRouter, init_args)
    while True:
        aiko.process.run()
