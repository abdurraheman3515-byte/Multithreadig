
import time
import threading


def Display():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for i in l1:
        print("Display:", i)
        
        time.sleep(2)


def sum():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s = 0

    for i in l1:
        s += i
        print("Sum:", s)
        time.sleep(2)


def string():
    l1 = ["Python", "Java","Javascript","Typescript","C", "C++","C#", "HTML", "SQL","Scala"]

    for i in l1:
        print("String:", i)
        print("================================")
        time.sleep(2)


t1 = threading.Thread(target=Display)
t2 = threading.Thread(target=sum)
t3 = threading.Thread(target=string)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

print("All threads completed!")
