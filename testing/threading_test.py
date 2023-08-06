import concurrent.futures
import threading
import platform


def job(message):
    processor = platform.processor()
    thread_number = threading.get_ident()
    print(f"Processor name: {processor}")
    print(f"Thread number: {thread_number}")
    print(f"Job {message} completed")


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(job, "Job 1"),
            executor.submit(job, "Job 2"),
            executor.submit(job, "Job 3"),
        ]

        for future in futures:
            future.result()
