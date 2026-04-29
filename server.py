import asyncio
import random
import websockets

clients = set()

async def handler(websocket):
    print("Cliente conectado")
    clients.add(websocket)

    try:
        async for message in websocket:
            print(f"Recibido: {message}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        clients.remove(websocket)
        print("Cliente desconectado")

async def broadcast_random():
    while True:
        if clients:
            number = random.randint(1, 100)
            print(f"Enviando: {number}")

            await asyncio.gather(*[
                client.send(str(number))
                for client in clients
            ])

        await asyncio.sleep(2)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("Servidor corriendo en ws://localhost:8765")

    await asyncio.gather(
        server.wait_closed(),
        broadcast_random()
    )

if __name__ == "__main__":
    asyncio.run(main())