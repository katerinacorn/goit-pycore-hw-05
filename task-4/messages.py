MESSAGES = {
    "welcome": "👋🤖 Welcome to the assistant bot!",
    "prompt": "👉 Enter a command: ",
    "goodbye": "\n👋🤖 Good bye!",
    "greeting": "🖐️ How can I help you?",
    "invalid": "❓ Invalid command.",
    "add_success": "✅ Contact added.",
    "change_success": "🔄 Contact updated.",
    "phone_found": lambda name, phone: f"📞 {name}'s phone number is {phone}",
    "contact_not_found": "❌ Contact not found.",
    "all_empty": "📭 No contacts found.",
    "all_header": "📇 Contact list:",
    "all_entry": lambda name, phone: f"\t 📌 {name}: {phone}",
    "help": (
        "📖 Available commands:\n"
        "  hello                  - Greet the bot\n"
        "  add <name> <phone>     - Add a new contact\n"
        "  change <name> <phone>  - Update existing contact\n"
        "  phone <name>           - Show contact's phone number\n"
        "  all                    - Show all contacts\n"
        "  help or -h             - Show this help message\n"
        "  close or exit          - Exit the assistant\n"
    ),
}

ERROR_MESSAGES = {
    "KeyError": "Enter user name.",
    "ValueError": "Invalid input. Expected: name and phone.",
    "IndexError": "Missing arguments. Please enter a user name.",
    "TypeError": "Invalid argument type or count.",
    "Unexpected": lambda e: f"😱 Unexpected error: {str(e)}",
}
