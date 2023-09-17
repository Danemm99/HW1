import random
import threading
import time

def monte_carlo_single_thread(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

def monte_carlo_multi_thread(num_points, num_threads):
    inside_circle = 0
    points_per_thread = num_points // num_threads

    def monte_carlo_thread(event):
        nonlocal inside_circle
        thread_inside_circle = 0

        for _ in range(points_per_thread):
            x, y = random.random(), random.random()
            if x ** 2 + y ** 2 <= 1:
                thread_inside_circle += 1

        inside_circle += thread_inside_circle
        event.set()

    events = []

    for _ in range(num_threads):
        event = threading.Event()
        events.append(event)
        thread = threading.Thread(target=monte_carlo_thread, args=(event,))
        thread.start()

    for event in events:
        event.wait()

    return (inside_circle / num_points) * 4

if __name__ == "__main__":
    num_points = 1000000
    num_threads = 4

    start_time = time.time()
    pi_single_thread = monte_carlo_single_thread(num_points)
    end_time = time.time()

    single_thread_time = end_time - start_time

    start_time = time.time()
    pi_multi_thread = monte_carlo_multi_thread(num_points, num_threads)
    end_time = time.time()

    multi_thread_time = end_time - start_time

    print(f"Approximation of π using a single thread: {pi_single_thread}")
    print(f"Time taken by a single thread: {single_thread_time} seconds\n")


    print(f"Approximation of π using {num_threads} threads: {pi_multi_thread}")
    print(f"Time taken by {num_threads} threads: {multi_thread_time} seconds")