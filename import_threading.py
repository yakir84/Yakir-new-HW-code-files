import threading
import time
import random





def downloader(url):
    requests.get(url).json()

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=downloader, args=(url, ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
import threading
import time
import random