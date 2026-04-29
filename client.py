import sys
import os
import random
from word2number import w2n
import subprocess as sp
import websockets
import asyncio
ip = "127.0.0.1" 
port = 2700
wakeword = "computer"

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            result = (((await websocket.recv()).split(':')[1]))[2:-3]
            print(result)
            if wakeword in result and len(wakeword) == len(result):
                print("hi")

if __name__ == '__main__':
    asyncio.run(listen(f'ws://{ip}:{port}'))
