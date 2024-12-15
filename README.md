# ZMQ-IPC
A messaging framework using ZeroMQ and MessagePack, facilitating modular inter-process communication with standardized message structures.

## Features

- **Base Classes**: Simplifies the setup of messaging nodes.
- **ZeroMQ Integration**: Delivers high-performance, asynchronous messaging.
- **MessagePack Serialization**: Provides efficient binary serialization.
- **Minimal Overhead**: Minimal design to maximize performance and decrease learning curve.
- **Flexible Architecture**: Supports multiple publishers and subscribers.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Install Dependencies

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/PyZMQ-Messaging-Framework.git
cd PyZMQ-Messaging-Framework
pip install -r requirements.txt
```

## Usage

### Base Classes

The base classes are located in the `src` directory:

- `BasePublisher` in `src/base_publisher.py`
- `BaseSubscriber` in `src/base_subscriber.py`

### Examples

Example implementations are provided in the `examples` directory:

- `main.py`: Demonstrates how to run multiple publishers and subscribers in the same program.
- `my_pub.py`: An example publisher subclass.
- `my_sub.py`: An example subscriber subclass.

#### Running the Examples

Start the example by running `main.py`:

```bash
python examples/main.py
```

#### Example Output

```plaintext
Publisher1 bound to tcp://*:5556
Publisher2 bound to tcp://*:5557
Subscriber1 connected to tcp://localhost:5556 and subscribed to topics: ['Publisher1_data']
Subscriber2 connected to tcp://localhost:5557 and subscribed to topics: ['Publisher2_data']
...
```

## Extending the Framework

### Creating a Custom Publisher

```python
from src.base_publisher import BasePublisher

class MyCustomPublisher(BasePublisher):
    def run(self):
        # Implement your custom publishing logic
        pass
```

### Creating a Custom Subscriber

```python
from src.base_subscriber import BaseSubscriber

class MyCustomSubscriber(BaseSubscriber):
    def process_message(self, topic, message):
        # Implement your custom message processing logic
        pass
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
