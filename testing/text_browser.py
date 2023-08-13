import threading
import time
import concurrent.futures

def load_heavy_task(num_loops):
    for _ in range(num_loops):
        time.sleep(0.1)

def concurrency_test():
    start = time.time()
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=load_heavy_task, args=(100,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    delta_time = end - start
    print("Concurrency:", delta_time)

def parallelism_test():
    start = time.time()
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=load_heavy_task, args=(100,))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    delta_time = end - start
    print("Parallelism:", delta_time)

def threadpool_test():
    start = time.time()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    tasks = [executor.submit(load_heavy_task, 100) for _ in range(3)]

    for task in tasks:
        task.result()

    end = time.time()
    delta_time = end - start
    print("ThreadPool:", delta_time)

def main():
    i = 0
    for _ in range(10):
        print(i)
        i += 1
        concurrency_test()
        parallelism_test()
        threadpool_test()

if __name__ == "__main__":
    main()
