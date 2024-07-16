# 0x03. Log Parsing

## Description

This project focuses on parsing logs, specifically HTTP request logs. The goal is to read lines from standard input, compute metrics, and print the statistics. This includes counting the number of lines by status code and the total file size.

## Files

- `0-stats.py`: Main script that reads from standard input and parses the logs. It prints the computed metrics after every 10 lines and finally after all input is processed.

## Requirements

- Python 3.x

## Usage

To execute the script, use the following command:
```bash
python3 0-stats.py

## Input Format

The input log lines have the following format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

- IP Address: The IP address of the client
- date: Date and time of the request
- status code: The HTTP status code returned
- file size: The size of the file returned to the client

## Output

The script prints the following metrics:

- Total file size: Sum of all file sizes encountered in the logs.
- Status code counts: Count of each status code encountered. Only print status codes with counts greater than 0.

The metrics are printed in the following format:

File size: <total file size>

<status code>: <number of occurrences>

...

## Example

Given the following input:

10.0.0.1 - [2017-01-01 00:00:01] "GET /projects/260 HTTP/1.1" 200 1024

10.0.0.2 - [2017-01-01 00:00:02] "GET /projects/260 HTTP/1.1" 301 512

10.0.0.3 - [2017-01-01 00:00:03] "GET /projects/260 HTTP/1.1" 404 256

The script would output:

File size: 1792

200: 1

301: 1

404: 1

## Author

This project is maintained by [Your Name].
