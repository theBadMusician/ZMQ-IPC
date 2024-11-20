import zmq
import msgpack
import threading
import time

class BasePublisher:
    def __init__(self, address="tcp://*:5556", context=None):
        """
        Initializes the publisher with a ZeroMQ PUB socket.

        :param address: The address to bind the publisher socket.
        :param context: An optional ZeroMQ context to use.
        """
        self.context = context or zmq.Context.instance()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(address)
        self.running = False
        print(f"Publisher bound to {address}")

    def start(self):
        """
        Starts the publisher in a new thread.
        """
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        """
        Stops the publisher and closes the socket.
        """
        self.running = False
        self.socket.close()
        print("Publisher stopped")

    def run(self):
        """
        Main loop of the publisher. Should be overridden by subclasses.
        """
        try:
            while self.running:
                # Implement the publishing logic here
                time.sleep(1)
        except KeyboardInterrupt:
            print("Publisher interrupted")
        finally:
            self.stop()

    def publish(self, topic, message):
        """
        Publishes a message under a specific topic.

        :param topic: The topic string.
        :param message: The message object to be serialized and sent.
        """
        # Serialize the message using MessagePack
        message_packed = msgpack.packb(message)
        # Send the topic and the packed message
        self.socket.send_multipart([topic.encode('utf-8'), message_packed])
        print(f"Published message on topic '{topic}': {message}")
