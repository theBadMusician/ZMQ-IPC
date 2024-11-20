from examples.my_pub import MyPublisher
from examples.my_sub import MySubscriber
import time
import zmq

if __name__ == "__main__":
    # Create a shared ZeroMQ context
    context = zmq.Context.instance()

    # Define publishers
    publisher1 = MyPublisher(name="Publisher1", address="tcp://*:5556", context=context)
    publisher2 = MyPublisher(name="Publisher2", address="tcp://*:5557", context=context)

    # Start publishers
    publisher1.start()
    publisher2.start()

    # Define subscribers
    subscriber1 = MySubscriber(
        name="Subscriber1",
        address="tcp://localhost:5556",
        topics=["Publisher1_data"],
        context=context
    )
    subscriber2 = MySubscriber(
        name="Subscriber2",
        address="tcp://localhost:5557",
        topics=["Publisher2_data"],
        context=context
    )
    subscriber3 = MySubscriber(
        name="Subscriber3",
        address="tcp://localhost:5556",
        topics=["Publisher1_data"],
        context=context
    )

    # Start subscribers
    subscriber1.start()
    subscriber2.start()
    subscriber3.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Main program interrupted")
    finally:
        # Stop publishers
        publisher1.stop()
        publisher2.stop()
        # Stop subscribers
        subscriber1.stop()
        subscriber2.stop()
        subscriber3.stop()
        # Allow threads to finish
        publisher1.thread.join()
        publisher2.thread.join()
        subscriber1.thread.join()
        subscriber2.thread.join()
        subscriber3.thread.join()
        # Terminate the context
        context.term()
        print("All publishers and subscribers stopped")
