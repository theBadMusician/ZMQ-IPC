from src.base_subscriber import BaseSubscriber

class MySubscriber(BaseSubscriber):
    def __init__(self, name, address, topics, context=None):
        super().__init__(address=address, topics=topics, context=context)
        self.name = name

    def process_message(self, topic, message):
        print(f"{self.name} received message on topic '{topic}': {message}")
        # Implement custom processing logic here
