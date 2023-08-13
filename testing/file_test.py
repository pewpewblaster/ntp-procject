import time
from concurrent.futures import ThreadPoolExecutor

class MyThreadPool:
    """A multithreading class that uses ThreadPoolExecutor."""

    def __init__(self, num_threads=4):
        """Initialize the class with the number of threads."""
        self.num_threads = num_threads
        self.thread_pool = ThreadPoolExecutor(max_workers=num_threads)

    def run_jobs(self, jobs):
        """Run the jobs in the thread pool."""
        start_time = time.time()
        results = list(self.thread_pool.map(jobs))
        end_time = time.time()
        delta_time = end_time - start_time
        print(f"Delta time: {delta_time}")
        return results

    def add_job(self, job):
        """Add a job to the thread pool."""
        self.thread_pool.submit(job)

def my_job(name):
    """A simple job that prints the name."""
    print(f"Hello, {name}")
    time.sleep(1)
    return name

def main():
    """The main function."""
    # Create a thread pool with 4 threads.
    pool = MyThreadPool(num_threads=4)

    # Create a list of jobs.
    jobs = [lambda: my_job("Alice"), lambda: my_job("Bob"), lambda: my_job("Carol")]

    # Run the jobs in the thread pool.
    results = pool.run_jobs(jobs)

    # Print the results.
    for name in results:
        print(name)

if __name__ == "__main__":
    main()
