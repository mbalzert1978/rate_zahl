x = list(range(10))
y = 5
z = ["1" for x in range(10)]


def test(value):
    if not isinstance(value, list):
        print(f"No valid Gameinstace: {value}")
        return
    if not isinstance(next(iter(value)), int):
        print(f"No valid Gameinstace: {value}")
        return
    return value


print(test(x))
print(test(y))
print(test(z))
