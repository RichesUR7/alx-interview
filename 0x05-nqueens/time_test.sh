#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ./time_test.sh N"
	exit 1
fi

# Number of times to run each script
runs=10

# The size of the board (N)
N=$1

# Initialize time sums
time_sum_py=0
time_sum_so=0

echo "Running the scripts $runs times for N=$N..."

# Run the Python script
for ((i = 1; i <= $runs; i++)); do
	time_result=$( (time -p ./0-nqueens.py $N) 2>&1 | grep real | awk '{print $2}')
	time_sum_py=$(echo "$time_sum_py + $time_result" | bc)
done

# Run the Python script with shared library
for ((i = 1; i <= $runs; i++)); do
	time_result=$( (time -p ./0-nqueens_so.py $N) 2>&1 | grep real | awk '{print $2}')
	time_sum_so=$(echo "$time_sum_so + $time_result" | bc)
done

# Calculate averages and convert to milliseconds
avg_time_py=$(echo "scale=2; ($time_sum_py / $runs) * 1000" | bc)
avg_time_so=$(echo "scale=2; ($time_sum_so / $runs) * 1000" | bc)

# Print results
echo "Average execution time for 0-nqueens.py: $avg_time_py milliseconds"
echo "Average execution time for 0-nqueens_so.py: $avg_time_so milliseconds"
