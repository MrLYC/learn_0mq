#!/usr/bin/env python
# encoding: utf-8

import time
import argparse
import random

import zmq


parser = argparse.ArgumentParser(description="pusher")
parser.add_argument("name")
parser.add_argument("-p", "--port", type=int, default=8081)
parser.add_argument("-b", "--bind", action="store_true", default=False)
parser.add_argument("-s", "--sleep", type=int, default=1)
args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.PUSH)
if args.bind:
    socket.bind("tcp://127.0.0.1:%s" % args.port)
else:
    socket.connect("tcp://127.0.0.1:%s" % args.port)

while True:
    time.sleep(args.sleep)
    message = str(random.randint(0, 100))
    print("{name} pushed: {message}".format(name=args.name, message=message))
    socket.send(message)
