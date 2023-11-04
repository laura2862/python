import multiprocessing
import os
import time

mylist=[]
def add(num):
    print(f'*' * 50)
    print(f'add process\'s id and it\'s parent\'s id : {os.getpid()},{os.getppid()}')
    print(f'current add process is: {multiprocessing.current_process()}')
    print(f'*' * 50)
    for i in range(num):
        global mylist
        mylist.append(i)
        print(f'added {i} into list : {list}')
        time.sleep(0.2)
    print(f'*' * 50)
def read(count):
    print(f'*' * 50)
    print(f'read process\'s id and it\'s parent\'s id : {os.getpid()},{os.getppid()}')
    print(f'current read process is: {multiprocessing.current_process()}')
    print(f'*' * 50)
    for i in range(count):
        print(f'read: {i}')
        # way 3 : kill a process by calling os.kill
        os.kill(os.getpid(),9)
    print(f'*' * 50)

if __name__ == '__main__':
    # get current process id and parent id
    print(f'*' * 50)
    print('main start before sub-processes:')
    print(f' main process id: {os.getpid()}')
    # get current process object
    print(f'current main process is: {multiprocessing.current_process()}')
    print(f'*'*50)
    add_process=multiprocessing.Process(target=add,args=(5,))
    read_process=multiprocessing.Process(target=read,kwargs={'count':5})
    # way 2: to force terminate sub-process by setting deamon = True before the sub-processes started
    add_process.daemon=True
    read_process.daemon=True
    add_process.start()
    read_process.start()
    # join: let other processes execute after current process ends
    add_process.join()


    print('main start after sub-processes:')

    # way 1: to force terminate sub-process
    print(f'this is the last command in main to execute ')
    add_process.terminate()



