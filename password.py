def showing(p1: list) -> None:
    for index, value in enumerate(p1):
        print(index, "->", value)

print(showing([True, False, 88, 'yes']))