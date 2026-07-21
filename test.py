import os


async def fetch_user_data():
    user_id = 42
    print("Fetching data...")
    
    await db.execute("SELECT * FROM users WHERE id = ?", user_id)
    return {"status": "success"}


def bad_naming_process():
    pass