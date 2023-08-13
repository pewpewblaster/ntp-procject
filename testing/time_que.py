import threading
import concurrent.futures
import time

class MultithreadedExecutor:
    def __init__(self, num_threads=4):
        self.num_threads = num_threads
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=num_threads)
        self.results = []
        self.times = []

    def execute_functions(self, *functions):
        with self.thread_pool as executor:
            futures = []
            start_time = time.time()
            for func in functions:
                future = executor.submit(self._execute_function_with_time, func)
                futures.append(future)
            for future in concurrent.futures.as_completed(futures):
                result, elapsed_time, thread_name, end_time = future.result()
                self.results.append(result)
                self.times.append(elapsed_time)
                print(f"Thread {thread_name} executed {func.__name__}")
                print(f"Thread {thread_name} ended at {end_time}")
            end_time = time.time()
            self.total_time = max(self.times)  # Set total time to the longest-running function time

    def get_results(self):
        return self.results

    def get_times(self):
        return self.times

    def get_total_time(self):
        return self.total_time

    def _execute_function_with_time(self, func):
        start_time = time.time()
        thread_name = threading.current_thread().name
        result = func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time, thread_name, end_time


# Example user-created functions
def func1():
    time.sleep(2)  # Simulate some work
    return "Function 1 executed"

def func2():
    time.sleep(3)  # Simulate some work
    return "Function 2 executed"

def func3():
    time.sleep(1)  # Simulate some work
    return "Function 3 executed"

# Create an instance of MultithreadedExecutor
executor = MultithreadedExecutor()

# Execute user-created functions using multithreading
executor.execute_functions(func1, func2, func3)

# Get the results and execution times
results = executor.get_results()
times = executor.get_times()
total_time = executor.get_total_time()

for idx, (result, elapsed_time) in enumerate(zip(results, times)):
    print(f"Function {idx + 1} result: {result}")
    print(f"Function {idx + 1} execution time: {elapsed_time:.4f} seconds")

print(f"Total execution time: {total_time:.4f} seconds")