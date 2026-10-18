
def solve(password: str) -> str:
    missing = []

    if len(password) < 8:
        missing.append("довжини")

    if not any(ch.isdigit() for ch in password):
        missing.append("цифри")

    if not any(ch.isupper() for ch in password):
        missing.append("великої літери")

    if not any(ch.islower() for ch in password):
        missing.append("малої літери")

    if not missing:
        return "Пароль прийнято"

    return "Не вистачає: " + ", ".join(missing)
