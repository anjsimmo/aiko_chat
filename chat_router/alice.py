#!/usr/bin/env python3

import aiko_services as aiko

class Alice(aiko.Actor):
    def __init__(self, context):
        context.call_init(self, "Actor", context)
        print(f"MQTT topic: {self.topic_in}")

    def aloha(self, name):
        self.logger.info(f"Alice received: {name}")

if __name__ == "__main__":
    init_args = aiko.actor_args("alice")
    alice = aiko.compose_instance(Alice, init_args)
    aiko.process.run()
