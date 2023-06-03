import threading

def worker(num):
    """Function to be executed by each thread."""
    print(f"Worker {num} starting...")
    # Do some work here
    print(f"Worker {num} finished.")

# Create and start multiple threads
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

# Wait for all threads to complete
for t in threading.enumerate():
    if t != threading.main_thread():
        t.join()

print("All threads finished.")