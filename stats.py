def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]


def sort_dict(text):
    sorted = []
    for key, value in text.items():
       sorted.append({"char": key, "num": value})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
