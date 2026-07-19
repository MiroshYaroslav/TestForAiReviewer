import time
import httpx
from fastapi import FastAPI
from database import SessionLocal
from models import User

app = FastAPI()

# ПОМИЛКА ЗАЛИШИЛАСЯ: Dependency Injection (використання глобальної сесії замість Depends)
db = SessionLocal()

@app.get("/users")
async def get_users():
    # ПОМИЛКА ЗАЛИШИЛАСЯ: N+1 Query Problem та синхронний виклик у async-функції
    users = db.query(User).all()
    
    results = []
    # ВИПРАВЛЕНО: Тепер використовуємо асинхронний клієнт замість requests
    async with httpx.AsyncClient() as client:
        for user in users:
            response = await client.get(f"https://api.example.com/data/{user.id}")
            results.append({"user": user.name, "data": response.json()})
            
    return results

@app.get("/heavy-task")
async def heavy_task():
    # НОВА ПОМИЛКА: використання синхронного time.sleep() в асинхронному роуті.
    # ШІ має зрозуміти, що це Async I/O Blocking і порадити asyncio.sleep().
    time.sleep(5)
    return {"status": "Task finished"}    



    