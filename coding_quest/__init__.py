def squared(n):
    return pow(n, 2)


def windowed(items: list, window_size: int):
    for i in range(len(items) - window_size + 1):
        yield items[i : i + window_size]
