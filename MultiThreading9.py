import time
import threading
import os


def SumEven(No):
    print("PID of SumEven thread is : ",threading.get_ident())
    

def SumOdd(No):
     print("PID of SumOdd thread is : ",threading.get_ident())
    

def main():
    print("PID of main thread is : ",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven, args=(100000,))
    t2 = threading.Thread(target=SumOdd, args=(100000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()