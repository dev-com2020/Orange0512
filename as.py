import asyncio

def main():
    print("Mój program async")

async def pozdro(pierwszy, drugi):
    print(pierwszy)
    await asyncio.sleep(1)
    print(drugi)

asyncio.run(pozdro("Witaj", "Żegnaj"))

main()
