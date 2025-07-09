from main import parse_input, add_contact, change_contact, show_phone, show_all
from decorators import input_error
from messages import ERROR_MESSAGES


def test_parse_input():
    assert parse_input("add John 12345") == ("add", ["John", "12345"])
    assert parse_input("   phone Alice  ") == ("phone", ["Alice"])
    assert parse_input("") == ("", [])
    assert parse_input("   ") == ("", [])


def test_add_contact():
    contacts = {}
    assert add_contact(["John", "12345"], contacts) == "✅ Contact added."
    assert contacts == {"John": "12345"}


def test_change_contact():
    contacts = {"John": "12345"}
    assert change_contact(["John", "54321"], contacts) == "🔄 Contact updated."
    assert contacts["John"] == "54321"
    assert change_contact(["Unknown", "000"], contacts) == "❌ Contact not found."


def test_show_phone():
    contacts = {"Alice": "111"}
    assert show_phone(["Alice"], contacts) == "📞 Alice's phone number is 111"
    assert show_phone(["Bob"], contacts) == "❌ Contact not found."


def test_show_all():
    contacts = {"A": "1", "B": "2"}
    result = show_all(contacts)
    assert "📇 Contact list:" in result
    assert "📌 A: 1" in result
    assert "📌 B: 2" in result

    assert show_all({}) == "📭 No contacts found."


@input_error
def trigger_key_error():
    raise KeyError


@input_error
def trigger_value_error():
    raise ValueError


@input_error
def trigger_index_error():
    raise IndexError


@input_error
def trigger_type_error():
    raise TypeError


@input_error
def trigger_unexpected():
    raise RuntimeError("Something bad")


if __name__ == "__main__":
    test_parse_input()
    test_add_contact()
    test_change_contact()
    test_show_phone()
    test_show_all()

    assert trigger_key_error() == ERROR_MESSAGES["KeyError"]
    assert trigger_value_error() == ERROR_MESSAGES["ValueError"]
    assert trigger_index_error() == ERROR_MESSAGES["IndexError"]
    assert trigger_type_error() == ERROR_MESSAGES["TypeError"]
    assert trigger_unexpected() == ERROR_MESSAGES["Unexpected"](
        RuntimeError("Something bad")
    )

    print("✅ All tests passed.")
