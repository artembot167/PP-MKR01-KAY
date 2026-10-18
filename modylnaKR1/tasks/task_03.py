
def solve(text: str) -> str:
    words = text.split()

    count_words = len(words)
    count_upper = 0
    longest = "-"

    for word in words:
        if word[0].isupper():
            count_upper += 1

        if longest == "-" or len(word) > len(longest):
            longest = word

    return (f"Слів: {count_words}\n"
            f"Найдовше: {longest}\n"
            f"З великої літери: {count_upper}")
