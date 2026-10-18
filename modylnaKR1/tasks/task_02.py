
def solve(n: str) -> str:
    try:
        number = int(n)
    except ValueError:
        return "Помилка: n має бути цілим від 1 до 12"

    if number < 1 or number > 12:
        return "Помилка: n має бути цілим від 1 до 12"

    lines = []
    total = 0

    for i in range(1, 11):
        result = number * i
        lines.append(f"{number} x {i} = {result}")
        total += result

    lines.append(f"Сума: {total}")

    return "\n".join(lines)
