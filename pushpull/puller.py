#!/usr/bin/env python
# encoding: utf-8

import argparse

import zmq


parser = argparse.ArgumentParser(description="puller")
parser.add_argument("name")
parser.add_argument("-p", "--port", type=int, default=8081)
parser.add_argument("-b", "--bind", action="store_true", default=False)
args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.PULL)
if args.bind:
    socket.bind("tcp://127.0.0.1:%s" % args.port)
else:
    socket.connect("tcp://127.0.0.1:%s" % args.port)

while True:
    message = socket.recv()
    if not message:
        continue
    print("{name} pull: {message}".format(
        name=args.name, message=message,
    ))
