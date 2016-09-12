.PHONY: pubsub
pubsub:
	./driver.sh \
		"./pubsub/subscriber.py 1" \
		"./pubsub/subscriber.py 1" \
		"./pubsub/subscriber.py 2" \
		"./pubsub/subscriber.py 3" \
		"./pubsub/publisher.py -b -t 3"

.PHONY: npuller
npuller:
	./driver.sh \
		"./pushpull/puller.py puller1" \
		"./pushpull/puller.py puller2" \
		"./pushpull/puller.py puller3" \
		"./pushpull/pusher.py pusher -b"

.PHONY: npusher
npusher:
	./driver.sh \
		"./pushpull/pusher.py pusher1" \
		"./pushpull/pusher.py pusher2" \
		"./pushpull/pusher.py pusher3" \
		"./pushpull/puller.py puller -b"
