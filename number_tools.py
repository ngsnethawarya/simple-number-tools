def is_even(number: int) -> bool:
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


def square(number: int) -> int:
    """Return the square of a given number."""
    return number * number


if __name__ == "__main__":
    print("Example:")
    n = 4
    print(f"Is {n} even? -> {is_even(n)}")
    print(f"Square of {n} -> {square(n)}")
