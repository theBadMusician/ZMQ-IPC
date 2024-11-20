import zmq
import msgpack
import threading

class BaseSubscriber:
    def __init__(self, address="tcp://localhost:5556", topics=None, context=None):
        """
        Initializes the subscriber with a ZeroMQ SUB socket.

        :param address: The address to connect the subscriber socket.
        :param topics: A list of topics to subscribe to.
        :param context: An optional ZeroMQ context to use.
        """
        if topics is None:
            topics = []
        self.context = context or zmq.Context.instance()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(address)
        self.running = False
        # Subscribe to specified topics
        for topic in topics:
            self.socket.setsockopt_string(zmq.SUBSCRIBE, topic)
        print(f"Subscriber connected to {address} and subscribed to topics: {topics}")

    def start(self):
        """
        Starts the subscriber in a new thread.
        """
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        """
        Stops the subscriber and closes the socket.
        """
        self.running = False
        self.socket.close()
        print("Subscriber stopped")

    def run(self):
        """
        Main loop of the subscriber. Receives messages and processes them.
        """
        try:
            while self.running:
                # Receive the topic and message
                topic_received, message_packed = self.socket.recv_multipart()
                # Deserialize the message
                message_data = msgpack.unpackb(message_packed, raw=False)
                # Process the message
                self.process_message(topic_received.decode('utf-8'), message_data)
        except KeyboardInterrupt:
            print("Subscriber interrupted")
        finally:
            self.stop()

    def process_message(self, topic, message):
        """
        Processes a received message. Should be overridden by subclasses.

        :param topic: The topic string of the received message.
        :param message: The deserialized message object.
        """
        print(f"Received message on topic '{topic}': {message}")
        # Implement message processing logic here
