
def solve(text: str) -> str:
    text = text.strip().lower()

    if not text:
        return "Порожній текст"

    counts = {}

    for char in text:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1

    if not counts:
        return "Порожній текст"

    result = []

    for char, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{char}: {count}")

    result.append(f"Різних символів: {len(counts)}")

    return "\n".join(result)
