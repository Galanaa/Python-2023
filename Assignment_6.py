# Task 1


def calculate_price():
    price = 10

    quantity = 5

    def apply_discount():
        discount = 0.1

        global price

        price = 10 * (1 - discount)

        total_price = price * quantity

        print("The discounted price is", total_price)

    apply_discount()


calculate_price()

# Local variables are defined in a function and are thus limited to the scope of this function. Global variables are not defined inside any function and thus have a global scope.

# Task 2

import time

from functools import wraps


def timeit(func):
    # calculates the time difference with decorater notes, start time and end time after execution of function

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        total_time = end_time - start_time

        print(f"Function {func.__name__}{args} took {total_time:.4f} seconds")

        return result

    return timeit_wrapper


@timeit
def example(num):
    total = sum((x for x in range(0, num**2)))

    return total


if __name__ == "__main__":
    example(10)

    example(100)

    example(1000)

    example(5000)

    example(10000)

# Task 3

input_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_sum = 0

for number in input_list:
    # Sums up only even numbers

    if not number % 2:
        even_sum += number

even_sum

print("Sum of all even numbers:", even_sum)
