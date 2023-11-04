import threading
import time

sum=0
def add(lock):
    lock.acquire()
    global sum
    for i in range(1000):
        sum+=1
    print(f'added: {sum}')
    lock.release()
def read(lock):
    lock.acquire()
    global sum
    for i in range(1000):
        sum +=1
    print(f'read: {sum}')
    lock.release()

if __name__ == '__main__':
    print(f'the first command in main ~~~')
    time.sleep(0.2)
    # way 2: lock
    lock = threading.Lock()
    add_threading= threading.Thread(target=add,args=(lock,))
    read_threading=threading.Thread(target=read,kwargs={'lock':lock},daemon=True)
    # way2 setdaemon
    add_threading.setDaemon(True)
    add_threading.start()
    read_threading.start()
# way 1: join
#     add_threading.join()
#     read_threading.join()

# way 2: lock
    lock = threading.Lock()
    print(f'main: {sum}')
    time.sleep(1)
    print(f'the last command in main ~~~')
