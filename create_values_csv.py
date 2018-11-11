#!/usr/bin/env python3

import argparse
import csv
import random


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="give a name for the file to create")
    parser.add_argument("rows", help="the number of rows to create", type=int)

    args = parser.parse_args()

    generate(args.filename, args.rows)


def generate(name, row_count=10):
    count = 0
    print("Creating file: {} with {} rows.".format(name, row_count))

    with open(name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        while count < row_count:
            spamwriter.writerow([random.randint(1, 1000),
                                random.uniform(1, 100000),
                                random.randint(10, 1000),
                                random.uniform(100, 100000000),
                                random.uniform(1000, 1000000000)])

            count += 1

    print("Done generating file")


if __name__ == '__main__':
    main()
