from fastapi import APIRouter
import time

# Уявімо, що це імпорт твоєї бази
from app.db.database import AsyncSessionLocal 

router = APIRouter()

@router.get("/get_user_data")
async def get_user_data():
    # ❌ ПОМИЛКА 1: Блокуючий виклик в асинхронній функції
    time.sleep(2) 
    
    # ❌ ПОМИЛКА 2: Захардкоджені секретні дані
    api_key = "secret_super_key_12345" 
    
    # ❌ ПОМИЛКА 3: Неправильна робота з сесією БД (без async with або Depends)
    # З'єднання ніколи не закриється і призведе до витоку пам'яті
    db_session = AsyncSessionLocal() 
    
    try:
        # Якась логіка...
        data = {"user": "test", "key": api_key}
        return data
    except Exception as e:
        # ❌ ПОМИЛКА 4: "Голий" except (глушимо помилку, нічого не робимо)
        pass