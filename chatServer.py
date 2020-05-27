import asyncio
import websockets

async def clientHandler(websocket, path):
    while True:
        clients.add(websocket)
        receivedMessage = await websocket.recv()
        for client in clients:
            await client.send(receivedMessage)
clients = set()
server = websockets.serve(clientHandler, "localhost", 12345)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()

"""async def hello(websocket, path):
    while True:
        receivedMessage = await websocket.recv()
        print("Message reçu : "+ receivedMessage)
        messageTosend = receivedMessage
        await websocket.send(messageTosend)
start_server = websockets.serve(hello, "localhost", 12345)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()"""