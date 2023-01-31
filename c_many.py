import asyncio
import time
num_started=0
num_ended=0
async def say_after(delay, what):
  global num_started,num_ended
  num_started+=1#print('start '+what)
  await asyncio.sleep(delay)
  #print(what)
  num_ended+=1
def make_task(i):
    return asyncio.create_task(
      say_after(1, f'hellow{i}')
    )
n=100000
start=time.time()
def printit(what):
  global start
  cur=time.time()
  #print(f'{start} {cur}')
  elapsed=cur-start
  start=cur
  per_sec=n/elapsed  
  print(f'{what}: {n} elapsed secs: {elapsed:.2f},per sec:{per_sec:.2f}')

async def main():
    #print(f"started at {time.strftime('%X')}")

    tasks = [make_task(i) for i in range(n)]
    printit('create task')

    for x in tasks:
      await(x)
    printit('await task')

asyncio.run(main())    