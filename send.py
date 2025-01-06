import asyncio

from rstream import Producer

STREAM_NAME = "hello-python-stream"
# 5GB
STREAM_RETENTION = 5000000000


async def send():
    async with Producer(
        host="rabbitmq",
        username="guest",
        password="guest",
    ) as producer:
        await producer.create_stream(
            STREAM_NAME, exists_ok=True, arguments={"max-length-bytes": STREAM_RETENTION}
        )

        messages = [b"First message", b"Second message", b"Third message"]
        for msg in messages:
            await producer.send(stream=STREAM_NAME, message=msg)
            print(f"[x] Sent: {msg}")

        print(" [x] All messages sent")

with asyncio.Runner() as runner:
    runner.run(send())