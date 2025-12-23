# Chat Router

Usage:

Open separate terminals for ./router.py (a service for routing messages to the right users), ./alice.py and ./bob.py (each user has their own service)

Open yet another terminal for sending messages using the ./chat_send.py command:

./chat_send.py "Hi @alice and @bob"

The router will reroute messages that tag a (known) user directly to the service corresponding to that user.
