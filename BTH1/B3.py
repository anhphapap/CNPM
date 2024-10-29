d = dict()


def add_word(key, val):
    if key not in d:
        d[key] = val


def count_words():
    return len(d)


def find_word(key):
    print(f"{key} = {d[key]}" if key in d else "not found")


def remove_word(key):
    if key in d:
        del d[key]


if __name__ == "__main__":
    find_word('x')
