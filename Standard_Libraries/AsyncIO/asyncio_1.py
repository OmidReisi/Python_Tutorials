# use asyncIO instead of threading for really heave IO_Bound or really slow IO's or when there are too many tasks.
import asyncio


# coroutines are components like funcions and methods that pack your work into different sections and this allows this coroutines to run asynchronously with each other
# in order to define a coroutine in python use async keyword before it.
# when you set a function as a coroutine it can't be run like before, because the function now returns a coroutine.
async def send_mail():
    print("Email sent.")


# this line raises an error because this is no longer a funcion but a coroutine and coroutines aren't executable.
# send_mail()


# in order to execute a coroutine you should use asyncio.run() method.
# in order to execute a coroutine it should be awaited it's execution.
# this function automatically generates an event loop and awaits the passed coroutine for it's execution.
# an event loop is like a low level task manager that takes care of the tasks and events and the order they should be executed.
# in order to have an asynchronous program you should have an event loop.
asyncio.run(send_mail())

# send_mail() is a coroutine. (asyncio.iscoroutine())
# send_mail is a coroutine function. (asyncio.iscoroutinefunction())
