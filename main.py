import random
import threading

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

    def monte_carlo_thread():
        nonlocal inside_circle
        thread_inside_circle = 0

        for _ in range(points_per_thread):
            x, y = random.random(), random.random()
            if x ** 2 + y ** 2 <= 1:
                thread_inside_circle += 1

        inside_circle += thread_inside_circle

    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=monte_carlo_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return (inside_circle / num_points) * 4

if __name__ == "__main__":
    num_points = 1000000
    num_threads = 4

    pi_single_thread = monte_carlo_single_thread(num_points)
    pi_multi_thread = monte_carlo_multi_thread(num_points, num_threads)

    print(f"Approximation of π using a single thread: {pi_single_thread}")
    print(f"Approximation of π using {num_threads} threads: {pi_multi_thread}")
