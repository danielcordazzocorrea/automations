from fastapi import FastAPI

app = FastAPI()

@app.post("/webhook")
async def webhook(data: dict):
    print("Received:", data)
    return {"status": "ok"}