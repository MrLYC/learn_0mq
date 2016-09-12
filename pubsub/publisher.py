#!/usr/bin/env python
# encoding: utf-8

import time
import argparse
from collections import deque
import os

import zmq


parser = argparse.ArgumentParser(description="publisher")
parser.add_argument("-p", "--port", type=int, default=8081)
parser.add_argument("-b", "--bind", action="store_true", default=False)
parser.add_argument("-s", "--sleep", type=int, default=1)
parser.add_argument("-t", "--topic", type=int, default=3)
args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.PUB)
if args.bind:
    socket.bind("tcp://127.0.0.1:%s" % args.port)
else:
    socket.connect("tcp://127.0.0.1:%s" % args.port)

topics = deque(range(args.topic))

for i in range(1000):
    time.sleep(args.sleep)
    topic = topics[0]
    topics.rotate()
    message = i
    print("publisher send to {topic}: {message}".format(topic=topic, message=message))
    socket.send("{topic} {message}".format(topic=topic, message=message))
