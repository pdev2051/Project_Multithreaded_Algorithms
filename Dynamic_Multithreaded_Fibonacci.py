from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Set recursion threshold to avoid too many threads
RECURSION_THRESHOLD = 10

# Parallel Fibonacci using dynamic multithreading
def parallel_fib(n, executor):
    if n <= 1:
        return n
    elif n <= RECURSION_THRESHOLD:
        # Use normal recursion for small n to avoid thread overhead
        return parallel_fib(n - 1, executor) + parallel_fib(n - 2, executor)
    else:
        # Spawn: Submit tasks to executor
        future_x = executor.submit(parallel_fib, n - 1, executor)
        y = parallel_fib(n - 2, executor)
        x = future_x.result()  # Sync: wait for future_x
        return x + y

def main():
    n = 20
    start_time = time.time()

    # Create a ThreadPoolExecutor with dynamic threads
    with ThreadPoolExecutor() as executor:
        result = parallel_fib(n, executor)

    end_time = time.time()
    print(f"Fibonacci({n}) = {result}")
    print(f"Computed in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
