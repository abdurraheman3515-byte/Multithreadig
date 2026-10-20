
import threading
import time

def square(f, s, Name):
    for i in range(f, s):
        print("Square:",i*i)
        time.sleep(2)
        print("Name:", Name)


def cube(f, s, Name):
    for i in range(f, s):
        print("Cube:",i*i*i)
        time.sleep(2)
        print("Name:", Name)


t1 = threading.Thread(target=square,args=(2, 6),kwargs={"Name": "threading  1"})
t2 = threading.Thread(target=cube  ,args=(2, 6),kwargs={"Name": "threading  2"})

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed!")