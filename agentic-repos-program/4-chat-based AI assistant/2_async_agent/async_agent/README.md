Summary Table:

Aspect	                    Code 1: Async (await Runner.run())	                Code 2: Sync (Runner.run_sync())

Function call style	         Async, requires await inside async function	        Sync, blocking call

Running the code	            Needs event loop: asyncio.run(main())	           Runs directly, no event loop needed

Code complexity             	Slightly more complex (async/await)	                Simple synchronous code

Use case	                    Async apps, concurrency, scalable workloads	    Simple scripts or sync environments

Performance behavior        	Non-blocking	                                Blocking (waits until completion)

Dependency on asyncio       	Yes	                                            No (internal management of async loop)


When to use which?

Use Code 1 (async) if you are building an application that supports or requires asynchronous operations (e.g., web servers, bots handling multiple users).


Use Code 2 (sync) if you want simple, linear code without dealing with async syntax or if you run scripts where blocking behavior is okay.