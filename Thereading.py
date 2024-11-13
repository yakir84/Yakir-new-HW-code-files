import threading
import time
import random


def worker(thread_id, text):
    sleep_seconds = random.randint(0, 10)
    time.sleep(sleep_seconds)
    print("Thread " + str(thread_id) + ": " + text + " slept " + str(sleep_seconds) + " seconds" )

def main():
    num_of_threads = 5
    threads = []
    for i in range(num_of_threads):
        thread = threading.Thread(target= worker, args= (i, "good morning", ))
        thread.start() 
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()