"""Print the Collatz sequence starting from 27 and its total step count."""


def collatz(n):
    """Return the Collatz sequence from n through the first 1, inclusive."""
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    # Steps are transitions between values, so the initial 27 is not counted.
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
