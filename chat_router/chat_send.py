#!/usr/bin/env python3

import click

import aiko_services as aiko
from router import ChatRouter

@click.command("main", help="Remote call AlohaHonua Actor")
@click.argument("name", default="Test message", required=False)

def main(name):
    aiko.do_command(
        ChatRouter,
        aiko.ServiceFilter("*", "chatrouter", "*", "*", "*", "*"),
        lambda router: router.aloha(name),
        terminate=True)

    aiko.process.run()

if __name__ == "__main__":
    main()
