from pymonad.tools import curry

@curry(2)
def tag(name: str, value: str) -> str:
    return f"<{name}>{value}</{name}>"

@curry(3)
def extended_tag(name: str, attr: dict[str, str], value: str) -> str:
    attributes: str = ""
    for key, value in attr.items():
        attributes += f" {key}=\"{value}\""
    return f"<{name}{attributes}>{value}</{name}>"

def main():
    bold = tag('b')
    italic = tag('i')

    print(bold("Minecraft"))
    print(italic("Cryper"))

    print("=================")

    extended_italic = extended_tag('i', {"color": "red", "class": "list-group"})
    print(extended_italic("item"))

    extended_italic = extended_tag('i', {})
    print(extended_italic("item"))

if __name__ == "__main__":
    main()
