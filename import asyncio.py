import asyncio

async def print_B():
    print("B")
async def main_def():
    print("A")
    asyncio.gather(print_B())
    print("C")



asyncio.run(main_def())