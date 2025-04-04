import threading
from time import sleep

def taskA():
    for i in range(0, 10):
        print(f"Task A: {i} ")
        sleep(1)
    print("Task A completed")
    
    
def taskB():
    for i in range(0, 10):
        print(f"Task B: {i} ")
        sleep(1)
    print("Task B completed")
    
if __name__ == "__main__":
    threadA = threading.Thread(target=taskA)
    threadB = threading.Thread(target=taskB)
    
    threadA.start()
    threadB.start()
    
    threadA.join()
    threadB.join()
    
    print("Main thread completed")