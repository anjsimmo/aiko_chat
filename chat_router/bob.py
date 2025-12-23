#!/usr/bin/env python3

import aiko_services as aiko

class Bob(aiko.Actor):
    def __init__(self, context):
        context.call_init(self, "Actor", context)
        print(f"MQTT topic: {self.topic_in}")

    def aloha(self, name):
        self.logger.info(f"Bob: {name} !")

if __name__ == "__main__":
    init_args = aiko.actor_args("bob")
    bob = aiko.compose_instance(Bob, init_args)
    aiko.process.run()
