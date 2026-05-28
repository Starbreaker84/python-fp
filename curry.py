from pymonad.tools import curry


@curry(2)
def appeal(greetings: str, name: str) -> str:
    return greetings + name

@curry(4)
def complete_appeal(greetings: str, separator: str, end: str, name: str) -> str:
    return greetings + separator + " " + name + end

def main():
    # Пример каррированной функции, которая позволяет единожды
    # задать приветсвие и затем может быть использована с разными именами

    appeal_to = appeal("Hello, ")
    print(appeal_to("John"))
    print(appeal_to("Robert"))

    print("++++++++++++++++++++")

    complete_appeal_to = complete_appeal("Hello", ",", "!")
    complete_appeal_to_john = complete_appeal_to("John")
    complete_appeal_to_robert = complete_appeal_to("Robert")
    print(complete_appeal_to_john)
    print(complete_appeal_to_robert)

    print("++++++++++++++++++++")

    question_to = complete_appeal("Who are you", ",", "?")
    print(question_to("Mike"))




if __name__ == "__main__":
    main()
