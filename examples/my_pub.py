from src.base_publisher import BasePublisher
from datetime import datetime
import random
import time

class MyPublisher(BasePublisher):
    def __init__(self, name, address, context=None):
        super().__init__(address=address, context=context)
        self.name = name

    def run(self):
        topics = [f"{self.name}_data"]
        try:
            while self.running:
                topic = topics[0]
                message = {
                    "type": f"{self.name}_reading",
                    "timestamp": datetime.utcnow().isoformat(),
                    "payload": {
                        "value": random.uniform(0.0, 100.0)
                    }
                }
                self.publish(topic, message)
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"{self.name} Publisher interrupted")
        finally:
            self.stop()
