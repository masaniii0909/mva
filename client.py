import sys
import os
import random
from word2number import w2n
import subprocess as sp
import websockets
import asyncio
ip = "127.0.0.1" # local
port = 2700
wakeword = "computer"

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            result = await websocket.recv()
            result = result.split(':')[1]
            print(result[2:-3])
def main():
    print('yea im here' * 5)
    result = websocket.recv()
    result = result[14:-3]
    print(result)
    if wakeword in cleanresult:
        print("hi")

while True:
    asyncio.run(listen(f'ws://{ip}:{port}'))
    main()
