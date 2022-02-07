import asyncio


# so far we've been using asynchronous syntax to run programs synchronously but we want to continue doing other tasks when our program is waiting a coroutine.
# in order to execute tasks asynchronously when a coroutine is awaiting we need to create a new task.


async def main():
    print("Omid")

    # in order to create a new task we use asyncio.create_task()
    # creating a task automatically adds it to the event loop
    # this method returns a task object but you don't have to catch it in order to run the task
    task = asyncio.create_task(task_1("text"))

    # while we're creating the task before this line, the task doesn't execute until a pause (like awaiting a coroutine) happens in our main function.
    print("still continuing the main function before executing task")

    # now that we've hit a pause in our main function our task starts it's execution and this is how asynchronous programs work.
    await asyncio.sleep(3)

    # after our task is finished and we've awaited our coroutine (asyncio.sleep(3)) our main function continues.
    print("after the execution of task_1")


async def task_1(text):
    print(text)

    # here we're awaiting another coroutine in our task and because this coroutine takes longer than the coroutine in main function (asyncio.sleep(3)) we give the execution back to the main function and we don't return to this task.
    # if this coroutine was asyncio.slee(1) and it took less time than the coroutine in the main function then we would have continued this task instead of jumping back to the main funcion.
    await asyncio.sleep(5)

    # as we can see when we run this program this line doesn't get printed in the terminal.
    # when we run the tasks as we did in this program we only ensure that we enter the task and we don't guarantee that we finish it.
    # if we enter a task and await a coroutine that gives the execution back to the main function we don't return to the task even if it's no finished.
    print("finishing up task_1")


asyncio.run(main())
