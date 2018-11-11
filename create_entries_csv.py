#!/usr/bin/env python3

import argparse
import csv
import datetime
import random

FMT = '%Y-%m-%d %H:%M:%S'

NAMES = [
    "Edith Ferguson",
    "Kylie Filer",
    "Kenneth Omeara",
    "Naomi Bell",
    "Josef Hare",
    "Eva Bermudes",
    "Sandra Holmes",
    "Helen Piper",
    "Frances Kridler",
    "Jared Baum",
    "Kevin Brewer",
    "Sarah Trotter",
    "Ernest Martinez",
    "Betty Matthews",
    "Nicolas Rios",
    "Jennifer Blenman",
    "Ethel Gilbert",
    "Dennis Vercher",
    "Mary Haro",
    "Martha Gonzalez",
    "Sandra Lee",
    "Marla Diaz",
    "Louise Johnson",
    "Stephanie Ross",
    "Chad White",
    "Stephanie Caldwell",
    "Pamela Carr",
    "Beatriz Ruzich",
    "Adolfo Clarke",
    "Shirley Arndt",
    "Betty Bueche",
    "Lawrence March",
    "Emma Mccarthy",
    "Evelyn Kirk",
    "Marilyn Thompson",
    "Albert Mayes",
    "James Murphy",
    "Melvin Riley",
    "Yvonne Velazquez",
    "Dorothy Hairston",
    "Cecile Kaan",
    "Garrett Wright",
    "Florentina Torres",
    "Deborah Rhodes",
    "Donald Cade",
    "Bethany Dominguez",
    "Timothy Harting",
    "Jane Jenkins",
    "Richard Geesey",
    "Robert Sommer",
]


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
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        while count < row_count:
            spamwriter.writerow([NAMES[random.randint(0, 19)],
                                random.uniform(1, 100000),
                                datetime.datetime.utcnow().strftime(FMT)])

            count += 1

    print("Done generating file")


if __name__ == '__main__':
    main()
