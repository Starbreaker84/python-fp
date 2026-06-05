from pymonad.list import ListMonad

# Сделаем вспомогательгные типы
Cell = tuple[int, int]
Cells = frozenset[Cell]

def conquest_campaign(n: int, m: int, l: int, battalion: list[int]) -> int:

    # Начальная высадка
    def landing(xs: list[int]) -> ListMonad[Cell]:
        match xs:
            case [x, y, *rest]:
                return ListMonad((x, y)) + landing(rest)
            case []:
                return ListMonad()

    # Проверка клетки на вхождение в плацдарм
    def is_valid(cell: Cell) -> ListMonad[Cell]:
        return (
            ListMonad(cell)
            if 1 <= cell[0] <= n and 1 <= cell[1] <= m
            else ListMonad()
        )

    # Вычисляем клетки для захвата
    def next_step(cell: Cell) -> ListMonad[Cell]:
        return ListMonad(
            cell,
        (cell[0] + 1, cell[1]),
        (cell[0] - 1, cell[1]),
        (cell[0], cell[1] + 1),
        (cell[0], cell[1] - 1),
        ).bind(is_valid)

    # Оставляем только уникальные клетки
    def uniq(captured: ListMonad[Cell]) -> Cells:
        return frozenset(captured)

    # Функция осуществления захвата соседних клеток
    def expand(captured: Cells) -> Cells:
        return uniq(ListMonad(*captured).bind(next_step))

    # Итератор по нашей кампании по захвату плацдарма
    def campaign(day: int, captured: Cells) -> int:
        return (
            day
            if len(captured) == n * m
            else campaign(day + 1, expand(captured))
        )

    # Запуск итератора
    start: Cells = uniq(landing(battalion))

    return campaign(1, start)

def main():

    print(conquest_campaign(3, 4, 2, [2, 2, 3, 4]))


if __name__ == "__main__":
    main()