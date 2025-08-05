import asyncio


async def print1(sec):
    # await asyncio.sleep(sec)
    print(sec)
    await asyncio.sleep(sec)


async def main():
    tasks = []  # Список задач
    for i in range(1, 16):
        tasks.append(asyncio.create_task(print1(i)))  # Создаем задачи и добавляем их в список

    await asyncio.gather(*tasks)  # Ждем выполнения всех задач




asyncio.run(main())
