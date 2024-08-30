import aio_pika
from aio_pika import ExchangeType, Message
import asyncio
from typing import Any, Callable, Optional

class RabbitMQClient:
    def __init__(self, url: str, exchange_name: str, exchange_type: ExchangeType = ExchangeType.DIRECT):
        self.url = url
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.connection: Optional[aio_pika.RobustConnection] = None
        self.channel: Optional[aio_pika.RobustChannel] = None
        self.exchange: Optional[aio_pika.Exchange] = None

    async def connect(self):
        # Установка соединения с RabbitMQ
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(self.exchange_name, self.exchange_type)

    async def close(self):
        # Закрытие соединения с RabbitMQ
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()

    async def publish_message(self, routing_key: str, message: Any):
        # Публикация сообщения в RabbitMQ
        if not self.exchange:
            raise RuntimeError("Exchange is not declared. Call 'connect' first.")
        message_body = Message(body=str(message).encode())
        await self.exchange.publish(message_body, routing_key=routing_key)
        print(f"Message sent: {message} to routing_key: {routing_key}")

    async def consume_messages(self, queue_name: str, routing_key: str, callback: Callable[[aio_pika.IncomingMessage], Any]):
        # Подписка на очередь и обработка сообщений
        if not self.channel:
            raise RuntimeError("Channel is not opened. Call 'connect' first.")
        queue = await self.channel.declare_queue(queue_name)
        await queue.bind(self.exchange, routing_key)

        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                await callback(message)
                print(f"Message received: {message.body.decode()}")

        await queue.consume(on_message)

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

# Пример использования

async def message_handler(message: aio_pika.IncomingMessage):
    print(f"Received message: {message.body.decode()}")

async def main():
    rabbitmq_url = "amqp://guest:guest@localhost/"
    exchange_name = "test_exchange"
    queue_name = "test_queue"
    routing_key = "test_routing_key"

    async with RabbitMQClient(rabbitmq_url, exchange_name, ExchangeType.DIRECT) as client:
        await client.publish_message(routing_key, "Hello, RabbitMQ!")
        await client.consume_messages(queue_name, routing_key, message_handler)

if __name__ == "__main__":
    asyncio.run(main())
