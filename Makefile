.PHONY: pubsub
pubsub:
	./driver.sh \
		"./pubsub/subscriber.py 1" \
		"./pubsub/subscriber.py 1" \
		"./pubsub/subscriber.py 2" \
		"./pubsub/subscriber.py 3" \
		"./pubsub/publisher.py -b -t 3"
