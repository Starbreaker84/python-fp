from pymonad.maybe import Nothing, Just, Maybe

to_left = lambda num: lambda pole: (
    Nothing
    if abs((pole[0] + num) - pole[1]) > 4
    else Just((pole[0] + num, pole[1]))
)

to_right = lambda num: lambda pole: (
    Nothing
    if abs((pole[1] + num) - pole[0]) > 4
    else Just((pole[0], pole[1] + num))
)

banana = lambda x: Nothing

def show(maybe: Maybe[tuple[int, int]]) -> None:
    print(maybe.is_just())

begin = lambda: Just( (0, 0) )

def main():
    show(
        begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-2))
    )

    show(
        begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-1))
    )

    show(
        begin().bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-2))
    )


if __name__ == "__main__":
    main()