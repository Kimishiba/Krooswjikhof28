import asyncio
import json
import websockets

async def query():
    uri = "ws://192.168.1.41:8123/api/websocket"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNjhiMmQwODJhZTQ0NzYzOTJmZGNjNDY2OTgwOThjMiIsImlhdCI6MTc4MjY3MzM4OCwiZXhwIjoyMDk4MDMzMzg4fQ.tpfps7BgZyoKiaKF9AqRdoRVEODkR9LhLCeCF1ElAlM"
    
    async with websockets.connect(uri) as websocket:
        await websocket.recv()
        await websocket.send(json.dumps({
            "type": "auth",
            "access_token": token
        }))
        await websocket.recv()
        
        # Query system_log
        await websocket.send(json.dumps({
            "id": 1,
            "type": "system_log/list"
        }))
        
        resp = await websocket.recv()
        print("System log response:")
        print(json.dumps(json.loads(resp), indent=2))

if __name__ == "__main__":
    asyncio.run(query())
