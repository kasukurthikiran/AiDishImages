# import asyncio


# async def fun_cal(n):
#     print("i 1 am function 1")
#     await asyncio.sleep(4)
#     print("i 2 am function 2")


# async def fun_cal1(n):
#     print("i 1.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 1.2 am function 2")


# async def fun_cal2(n):
#     print("i 2.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 2.2 am function 2")


# async def fun_cal3(n):
#     print("i 3.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 3.2 am function 2")


# async def fun_cal4(n):
#     print("i 4.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 4.2 am function 2")


# async def fun_cal5(n):
#     print("i 5.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 5.2 am function 2")


# async def fun_cal6(n):
#     print("i 6.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 6.2 am function 2")


# async def fun_cal7(n):
#     print("i 7.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 7.2 am function 2")


# async def fun_cal8(n):
#     print("i 8.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 8.2 am function 2")


# async def fun_cal9(n):
#     print("i 9.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 9.2 am function 2")


# async def fun_cal10(n):
#     print("i 10.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 10.2 am function 2")


# async def fun_cal11(n):
#     print("i 11.1 am function 1")
#     await asyncio.sleep(4)
#     print("i 11.2 am function 2")


# fun_cal1("Bob")
# fun_cal2("Charlie")
# fun_cal3("Charlie")
# fun_cal4("Charlie")
# fun_cal5("Charlie")
# fun_cal6("Charlie")
# fun_cal7("Charlie")
# fun_cal8("Charlie")
# fun_cal9("Charlie")
# fun_cal10("Charlie")


# async def main():
#     await asyncio.gather(
#         fun_cal("Alice"),
#         fun_cal1("Bob"),
#         fun_cal2("Charlie"),
#         fun_cal3("Charlie"),
#         fun_cal4("Charlie"),
#         fun_cal5("Charlie"),
#         fun_cal6("Charlie"),
#         fun_cal7("Charlie"),
#         fun_cal8("Charlie"),
#         fun_cal9("Charlie"),
#         fun_cal10("Charlie"),
#     )


# asyncio.run(main())


# # import asyncio


# # async def greet(name):
# #     print(f"Hello {name}")
# #     await asyncio.sleep(2)
# #     print(f"Welcome {name}")


# # async def main():
# #     await asyncio.gather(
# #         greet("Alice"),
# #         greet("Bob"),
# #         greet("Charlie"),
# #     )


# # asyncio.run(main())


# # # import asyncio


# # # async def greet(name):
# # #     print(f"Hello {name}")
# # #     await asyncio.sleep(2)
# # #     print(f"Welcome {name}")


# # # async def main():
# # #     task1 = asyncio.create_task(greet("Alice"))
# # #     task2 = asyncio.create_task(greet("Bob"))

# # #     # Do other things if needed...
# # #     await task1
# # #     await task2


# # # asyncio.run(main())


# # import asyncio


# # async def greet(name):
# #     print("sdf")
# #     await asyncio.sleep(4)
# #     print(name)


# # async def main():
# #     task1 = asyncio.create_task(greet("Alice"))

# #     task2 = asyncio.create_task(greet("Bob"))

# #     # Wait for both
# #     await asyncio.gather(task1, task2)


# # asyncio.run(main())


# # import time


# # def fun_cal():
# #     print("i 1 am function 1")
# #     time.sleep(4)
# #     print("i 2 am function 2")


# # def fun_cal1():
# #     print("i 1.1 am function 1")
# #     time.sleep(4)
# #     print("i 1.2 am function 2")


# # def fun_cal2():
# #     print("i 2.1 am function 1")
# #     time.sleep(4)
# #     print("i 2.2 am function 2")


# # fun_cal()
# # fun_cal1()
# # fun_cal2()


import asyncio

# Create a global semaphore with a concurrency limit
sem = asyncio.Semaphore(3)


# Wrap your function to use semaphore
async def run_with_semaphore(func, *args):
    async with sem:
        await func(*args)


# All your task functions
async def fun_cal(n):
    print("i 1 am function 1")
    await asyncio.sleep(4)
    print("i 2 am function 2")


async def fun_cal1(n):
    print("i 1.1 am function 1")
    await asyncio.sleep(4)
    print("i 1.2 am function 2")


async def fun_cal2(n):
    print("i 2.1 am function 1")
    await asyncio.sleep(4)
    print("i 2.2 am function 2")


async def fun_cal3(n):
    print("i 3.1 am function 1")
    await asyncio.sleep(4)
    print("i 3.2 am function 2")


async def fun_cal4(n):
    print("i 4.1 am function 1")
    await asyncio.sleep(4)
    print("i 4.2 am function 2")


async def fun_cal5(n):
    print("i 5.1 am function 1")
    await asyncio.sleep(4)
    print("i 5.2 am function 2")


async def fun_cal6(n):
    print("i 6.1 am function 1")
    await asyncio.sleep(4)
    print("i 6.2 am function 2")


async def fun_cal7(n):
    print("i 7.1 am function 1")
    await asyncio.sleep(4)
    print("i 7.2 am function 2")


async def fun_cal8(n):
    print("i 8.1 am function 1")
    await asyncio.sleep(4)
    print("i 8.2 am function 2")


async def fun_cal9(n):
    print("i 9.1 am function 1")
    await asyncio.sleep(4)
    print("i 9.2 am function 2")


async def fun_cal10(n):
    print("i 10.1 am function 1")
    await asyncio.sleep(4)
    print("i 10.2 am function 2")


async def fun_cal11(n):
    print("i 11.1 am function 1")
    await asyncio.sleep(4)
    print("i 11.2 am function 2")


# Main function
async def main():
    tasks = [
        run_with_semaphore(fun_cal, "Alice"),
        run_with_semaphore(fun_cal1, "Bob"),
        run_with_semaphore(fun_cal2, "Charlie"),
        run_with_semaphore(fun_cal3, "Charlie"),
        run_with_semaphore(fun_cal4, "Charlie"),
        run_with_semaphore(fun_cal5, "Charlie"),
        run_with_semaphore(fun_cal6, "Charlie"),
        run_with_semaphore(fun_cal7, "Charlie"),
        run_with_semaphore(fun_cal8, "Charlie"),
        run_with_semaphore(fun_cal9, "Charlie"),
        run_with_semaphore(fun_cal10, "Charlie"),
        run_with_semaphore(fun_cal11, "Charlie"),
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())


# # with get_db_session() as session:
# #     statement = select(UNMATCHEDRECORDS)
# #     dishes = session.exec(statement).all()
# #     dishes_with_id = [{"id": i.id, "name": i.name} for i in dishes]


# # @contextmanager
# # def get_db_session():
# #     yield from get_session()


# # with get_db_session() as session:
# #     statement = select(UNMATCHEDRECORDS).where(UNMATCHEDRECORDS.id == dish_id)
# #     dish = session.exec(statement).first()
# #     if dish:
# #         session.delete(dish)
# #         session.commit()
# #         print(f"Deleted dish with id={dish_id}")
# #     else:
# #         print("Dish not found")


#  results.append(
#             {
#                 "id": str(uuid.uuid4()),
#                 "dish": dish,
#                 "image_base64": base64_image,
#             }


# import time


# def blocking_task(n):
#     print(f"Task {n} started")
#     time.sleep(2)
#     print(f"Task {n} finished")


# for i in range(3):
#     blocking_task(i)


# import time
# from concurrent.futures import ThreadPoolExecutor


# def blocking_task(n):
#     print(f"Task {n} started")
#     time.sleep(2)
#     print(f"Task {n} finished")


# executor = ThreadPoolExecutor(max_workers=3)

# for i in range(4):
#     executor.submit(blocking_task, i)

# executor.shutdown(wait=True)


# import asyncio
# from concurrent.futures import ThreadPoolExecutor


# def blocking_task(n):
#     print(f"Task {n} started")
#     import time

#     time.sleep(2)
#     print(f"Task {n} finished")


# async def main():
#     executor = ThreadPoolExecutor(max_workers=2)
#     loop = asyncio.get_running_loop()

#     tasks = []
#     for i in range(4):
#         task = loop.run_in_executor(executor, blocking_task, i)
#         tasks.append(task)

#     await asyncio.gather(*tasks)


# asyncio.run(main())






{"restaurant_ids":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93","unmatched_records":[{"id":"8a155ae3-d199-4dcf-bf5b-4cb6f10ee739","name":"Omelette","r_id":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93"},{"id":"b2823d52-2359-4f22-b56e-697e8a1a09ef","name":"Pancakes","r_id":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93"},{"id":"98920e38-a673-44f8-84b2-0c923527db5c","name":"Avocado Toast","r_id":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93"},{"id":"2f4303fb-1f68-45c1-a29b-49b39e49d01b","name":"Cereal","r_id":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93"},{"id":"62603edb-9d93-4108-b541-eaa8bdbde9ea","name":"Yogurt Parfait","r_id":"5e9f84f6-d48f-4b6d-a299-bae5088c3d93"}]}%  
