from collections import Counter


def generate_phrase(letters: str, phrase: str) -> bool:
    phrase_count = Counter(phrase.lower())
    letters_count = Counter(letters.lower())

    # for when both letters and phrase are empty

    if not phrase_count and not letters_count:
        return True

    # for when there is not enough letters

    if len(phrase) > len(letters):
        return False

    for ch, count in phrase_count.items():
        if ch in letters_count and count <= letters_count.get(ch):
            continue
        else:
            return False

    return True


if __name__ == "__main__":
    characters = 'pt!ercyKadfsgvdf23'
    phrase = 'kat!'

print(generate_phrase(characters, phrase))
