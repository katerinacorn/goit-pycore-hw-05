ERROR_MESSAGES = {
    "IndexError": "Missing required arguments. Usage: python3 log_parser.py <log_file_path> [log_level]",
    "TypeError": "Invalid argument type or count.",
    "ValueError": "Invalid value provided. Please check your inputs.",
    "KeyError": "Missing expected data in log entry.",
    "Exception": lambda e: f"Unexpected error: {str(e)}",
}
