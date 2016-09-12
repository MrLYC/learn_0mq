#!/usr/bin/env python
# encoding: utf-8

import argparse
import time

import zmq


parser = argparse.ArgumentParser(description="subscriber")
parser.add_argument("name")
parser.add_argument("-p", "--port", type=int, default=8081)
parser.add_argument("-b", "--bind", action="store_true", default=False)
args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, "0")  # broadcast
socket.setsockopt(zmq.SUBSCRIBE, args.name)
if args.bind:
    socket.bind("tcp://127.0.0.1:%s" % args.port)
else:
    socket.connect("tcp://127.0.0.1:%s" % args.port)

while True:
    data = socket.recv()
    if not data:
        continue
    topic, message = data.split(" ", 1)
    print("{name} received from {topic}: {message}".format(
        name=args.name, topic=topic, message=message,
    ))
