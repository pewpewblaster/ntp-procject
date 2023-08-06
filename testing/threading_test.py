import concurrent.futures
import threading
import time


def job(message):
    print(f"Processor name: {threading.current_thread().name}")
    print(f"Thread number: {threading.get_ident()}")
    print(f"Job {message} completed")


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(job, "Job 1"),
            executor.submit(job, "Job 2"),
            executor.submit(job, "Job 3"),
        ]

        for future in futures:
            future.result()
