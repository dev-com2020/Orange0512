import asyncio
import time


# def main():
#     print("Mój program async")
#
# async def pozdro(pierwszy, drugi):
#     print(pierwszy)
#     await asyncio.sleep(1)
#     print(drugi)
#
# asyncio.run(pozdro("Witaj", "Żegnaj"))
#
# main()

# async def poinformuj(opoznienie, komunikat):
#     print(f"Przed {komunikat}")
#     await asyncio.sleep(opoznienie)
#     print(f"Po {komunikat}")
#
#
# async def main():
#     print(f"Start: {time.strftime('%X')}")
#     task1 = asyncio.create_task(poinformuj(1, "Pierwsze zadanie"))
#     task2 = asyncio.create_task(poinformuj(2, "Drugie zadanie"))
#
#     await task2
#     await task1
#
#     print(f"Stop: {time.strftime('%X')}")
#
# asyncio.run(main())

# async def zadanie(i):
#     print(f"Zadanie {i}")
#
# async def main():
#     print("10 zadań")
#     for k in range(10):
#         task = asyncio.create_task(zadanie(k))
#         await task
#
#
# asyncio.run(main())

# async def pozdrowienia():
#     print("pierwszy")
#     await asyncio.sleep(2)
#     print("drugi")
#
#
# async def main():
#     await asyncio.gather(pozdrowienia(), pozdrowienia(), pozdrowienia())
#
#
# start = time.perf_counter()
# asyncio.run(main())
# roznica = time.perf_counter() - start
# print(f"Czas wykonania:{roznica:.2f} sek.")


# async def generator(n):
#     for item in range(n):
#         yield item
#         await asyncio.sleep(1)
#
# async def main():
#     print("Generator")
#     async for i in generator(10):
#         print(i)

# asyncio.run(main())

# for item in range(10):
#     print(item)
#     time.sleep(1)

def generator(n):
    for item in range(n):
        yield item
        time.sleep(1)
        # return item

def main():
    print("Generator")
    for i in generator(10):
        print(i)


main()