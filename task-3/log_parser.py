import sys
import os
from collections import defaultdict
from decorators import input_error
from typing import List, Dict


ENCODING = "utf-8"
ARG_LOG_PATH_INDEX = 1
ARG_LOG_LEVEL_INDEX = 2


def parse_log_line(line: str) -> Dict:
    """
    Parses a single log line into a dictionary with keys: date, time, level, message.

    :param line: A single line from the log file.

    :return: Parsed components of the log line or empty dict on failure.
    """
    try:
        date, time, level, *message_parts = line.strip().split()
        message = " ".join(message_parts)
        return {"date": date, "time": time, "level": level.upper(), "message": message}
    except ValueError:
        return {}


def load_logs(path: str) -> List[Dict]:
    """
    Loads and parses all logs from a given file.

    :param path: Path to the log file.

    :return: A list of parsed log entries.
    """
    logs = []
    try:
        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, path)

        with open(full_path, "r", encoding=ENCODING) as f:
            logs = [parsed for line in f if (parsed := parse_log_line(line))]
    except FileNotFoundError:
        print(f"File '{full_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    """
    Filters log entries by the specified log level.

    :param logs: List of log entry dictionaries.
    :param level: Log level to filter by.

    :return: Filtered list of logs matching the level.
    """
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    """
    Counts the number of logs per log level.

    :param logs: List of log entries.

    :return: Dictionary with log level as key and count as value.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: Dict[str, int]):
    """
    Prints the counts of log entries per level in tabular format.

    :param counts: Dictionary with log levels and their counts
    """
    print("\nLog Level       | Count")
    print("----------------|------")
    for level in sorted(counts.keys()):
        print(f"{level:<16}| {counts[level]}")


def display_logs_for_level(logs: List[Dict], level: str):
    """
    Prints all log messages for the specified level.

    :param logs: List of log entries.
    :param level: Log level to display.
    """
    filtered = filter_logs_by_level(logs, level)
    if filtered:
        print(f"\nLog details for level '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"\nℹ️ No logs found for level '{level.upper()}'.")


@input_error
def main():
    """
    Main entry point for the script. Parses arguments, loads logs, and displays output.
    """
    log_file = sys.argv[ARG_LOG_PATH_INDEX]
    requested_level = sys.argv[ARG_LOG_LEVEL_INDEX]

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if requested_level:
        display_logs_for_level(logs, requested_level)


if __name__ == "__main__":
    result = main()
    if result:
        print(result)
