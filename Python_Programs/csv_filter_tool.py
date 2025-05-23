#!/usr/bin/env python3
import csv

# Input CSV file path
input_file = '4.0_MEGA_NUMBERED.csv'
# Output CSV file path
output_file = '4.0_MEGA_NUMBERED2.csv'

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row

        question_idx = header.index('question')
        response_idx = header.index('response')

        # Create a new CSV file for writing
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write the header row to the output CSV

            for row in reader:
                # Replace "U.S." with "US" in the 'question' and 'response' columns
                row[question_idx] = row[question_idx].replace('U.S.', 'US')
                row[response_idx] = row[response_idx].replace('U.S.', 'US')

                writer.writerow(row)

    print(f"CSV file processed. Modified data saved to '{output_file}'.")

process_csv(input_file, output_file)
