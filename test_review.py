import fastapi


async def test():
    await db.query()
    
async def test1():
    await asyncio.sleep(15)

def test2():
          await db.query()