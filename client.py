import sys
import os
import random
from word2number import w2n
import subprocess as sp
import websockets
import asyncio

wakeword = "computer"

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            print(await websocket.recv())
  
def main():
    result = websocket.recv()
    result = result[14:-3]
    print(cleanresult)
    if wakeword in cleanresult:
        print("hi")

if __name__ == "__main__":
    asyncio.run(listen(f'ws://{ip}:{port}'))
    main()
