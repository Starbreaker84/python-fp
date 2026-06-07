from functools import reduce

def second_maximum(numbers: list[int]) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers[1:])


def main():
    print(second_maximum([10, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(second_maximum([10, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == "__main__":
    main()