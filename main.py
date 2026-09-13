"""Console expense manager application."""

import json
from pathlib import Path

from expense import Expense

DATA_FILE: Path = Path("expenses.json")


def load_expenses() -> list[Expense]:
    """Load expenses from the JSON data file."""
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data: list[dict[str, object]] = json.load(file)
    return [Expense.from_dict(item) for item in data]


def save_expenses(expenses: list[Expense]) -> None:
    """Save expenses to the JSON data file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([expense.to_dict() for expense in expenses], file, ensure_ascii=False, indent=2)


def add_expense(expenses: list[Expense]) -> None:
    """Ask the user for expense details and add a new expense."""
    title: str = input("Назва: ").strip()
    try:
        amount: float = float(input("Сума: ").strip())
    except ValueError:
        print("Помилка: сума має бути числом.")
        return
    category: str = input("Категорія: ").strip()
    expenses.append(Expense(title=title, amount=amount, category=category))
    save_expenses(expenses)
    print("Витрату додано.")


def main() -> None:
    """Run the expense manager menu loop."""
    expenses: list[Expense] = load_expenses()
    while True:
        print("\n1. Додати витрату")
        print("2. Показати всі витрати")
        print("3. Показати витрати за категорією")
        print("4. Показати загальну суму")
        print("5. Вийти")
        choice: str = input("Оберіть дію: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Помилка: невідомий пункт меню.")


if __name__ == "__main__":
    main()
