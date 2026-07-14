import requests  # Порушення: Async I/O Blocking (використовуємо sync замість async)
from fastapi import FastAPI
from database import SessionLocal
from models import User

app = FastAPI()

# Порушення: Dependency Injection (використання глобальної сесії замість Depends)
db = SessionLocal()

@app.get("/users")
async def get_users():
    # Порушення: N+1 Query Problem (запитуємо всіх, потім у циклі ліземо в базу)
    users = db.query(User).all()
    
    results = []
    for user in users:
        # Тут бот має побачити, що ми звертаємося до user.profile (N+1)
        # І також побачити блокуючий запит requests.get
        external_data = requests.get(f"https://api.example.com/data/{user.id}").json()
        results.append({"user": user.name, "data": external_data})
        
    return results