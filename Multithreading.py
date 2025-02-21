#******************------------**Multithreading/THREADS********************--------------------*************************
#Multithreading in Python is used to run multiple threads (smaller units of a process) concurrently to improve performance,
#especially in I/O-bound operations. The threading module in Python provides features to create and manage threads.
# We Can Run Multiple things Simultaneously within a single threads one by one from 1 thread two threads or multiiple run together

##Example
from time import sleep  # Importing sleep function to pause execution
from threading import Thread  # Importing Thread class for multithreading

# Defining a class Hello that extends the Thread class
class Hello(Thread):
    def run(self):  # Overriding the run() method, which is executed when the thread starts
        for i in range(5):  # Loop runs 5 times
            print("Hello")  # Print "Hello"
            sleep(1)  # Pause for 1 second to simulate a time-consuming task

# Defining another class Hi that also extends the Thread class
class Hi(Thread):
    def run(self):  # Overriding the run() method
        for i in range(5):  # Loop runs 5 times
            print("hi")  # Print "hi"
            sleep(1)  # Pause for 1 second

# Creating two thread objects from the Hello and Hi classes
t1 = Hello()
t2 = Hi()

# Starting the first thread
t1.start()  # Calls the run() method in Hello class

sleep(0.2)  # A small delay to ensure "Hello" and "hi" print alternately

# Starting the second thread
t2.start()  # Calls the run() method in Hi class

# Wait for both threads to finish execution before proceeding
t1.join()  # Ensures main thread waits for t1 to complete
t2.join()  # Ensures main thread waits for t2 to complete

# Once both threads are done, print "Bye"
print("Bye")
