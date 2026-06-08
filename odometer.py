from functools import reduce
from pymonad.maybe import Just


def chuncked(xs: list[int]) -> list[tuple[int, int]]:
    match xs:
        case [x, y, *rest]:
            return [(x, y)] + chuncked(rest)
        case []:
            return []

def odometer(oksana: list[int]) -> int:
    return (
        Just(reduce(lambda x, y: ( x[0] + (y[0] * (y[1] - x[1])), y[1]), chuncked(oksana), (0, 0)))
        .map(lambda x: x[0])
        .value
    )


def main():

    print(odometer([15,1,25,2,30,3,10,5]))

    print(odometer([10,1,20,2]))

if __name__ == "__main__":
    main()