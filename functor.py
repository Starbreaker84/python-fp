from pymonad.list import ListMonad
from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing

@curry(2)
def add(x: int, y: int) -> int:
    return x + y

def main():
     add10 = add(10)

     print(Just(3).map(add10)) # Just 13

     print(ListMonad(1, 2, 3).map(add10)) # [11, 12, 13]

if __name__ == "__main__":
    main()
