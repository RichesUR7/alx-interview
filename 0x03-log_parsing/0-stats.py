#!/usr/bin/python3
"""
Module contains the method print_stats that parse the log
"""

import re
import signal
import sys

total_size = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

# Regular expression pattern for the log lines
log_pattern = re.compile(
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r'\[(.*?)\] "GET /projects/260 HTTP/1\.1" '
    r"(\d{3}) (\d+)"
)


def print_stats():
    """Function to print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """[TODO:description]

    Args:
        sig ([TODO:parameter]): [TODO:description]
        frame ([TODO:parameter]): [TODO:description]
    """
    print_stats()
    sys.exit(0)


# Set up signal handling for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        try:
            # match = log_pattern.match(line)
            # if match:
            #     total_size += int(match.group(4))
            #     status_codes[match.group(3)] += 1
            parts = line.split()
            size = int(parts[-1])
            code = parts[-2]

            if code in status_codes:
                status_codes[code] += 1
            total_size += size
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
        except Exception:
            pass

except KeyboardInterrupt:
    pass

finally:
    print_stats()
