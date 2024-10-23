import argparse
import random
import csv
import os
"""
Osoba 1: Jakub Graczyk
Osoba 2: Hubert Szymański
Osoba 3: Konrad Czarnecki
EXAMPLE USE: -m "styczeń, luty" -d "pn-wt, śr-czw, czw" -o create -f csv
"""
# Osoba 1 Jakub Graczyk
ALLOWED_MONTHS = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", 
                  "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

ALLOWED_DAYS = ["pn", "wt", "śr", "czw", "pt", "sb", "nd"]

def validate_months(months):
    months_list = months.split(', ')
    for month in months_list:
        if month not in ALLOWED_MONTHS:
            raise argparse.ArgumentTypeError(f"Invalid month: {month}. Allowed values are: {', '.join(ALLOWED_MONTHS)}")
    return months_list

def validate_days(days):
    days_list = days.split(', ')
    for day_range in days_list:
        for day in day_range.split('-'):
            if day not in ALLOWED_DAYS:
                raise argparse.ArgumentTypeError(f"Invalid day: {day}. Allowed values are: {', '.join(ALLOWED_DAYS)}")
    return days_list

def validate_timeofday(times):
    time_list = times.split(', ')
    for time in time_list:
        if time not in ['r', 'w']:
            raise argparse.ArgumentTypeError(f"Invalid time of day: {time}. Allowed values are: r, w")
    return time_list

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process and generate file structures.")
    
    parser.add_argument('-m', '--months', required=True, type=validate_months, 
                        help='Comma-separated list of months (e.g., styczeń,luty)')
    parser.add_argument('-d', '--days', required=True, type=validate_days, 
                        help='Comma-separated list of day ranges corresponding to each month (e.g., pn-wt,pt)')
    parser.add_argument('-t', '--timeofday', default='r', type=validate_timeofday, 
                        help='Comma-separated list of times of day (r for rano, w for wieczór), default is rano')
    parser.add_argument('-o', '--operation', choices=['create', 'read'], required=True, 
                        help='Operation mode: create or read')
    parser.add_argument('-f', '--format', choices=['csv', 'json'], required=True, 
                        help='File format: csv or json')

    args = parser.parse_args()

    if len(args.months) != len(args.days):
        parser.error("The number of days must match the number of months.")

    return args

def writefiles(paths):
    for path in paths:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        print(f"Writing file to {path}")
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Model', 'Wynik', 'Czas'])
            model = random.choice(['A', 'B', 'C'])
            score = random.randint(0, 1000)
            time = f"{random.randint(0, 1000)}s"
            writer.writerow([model, score, time])

def readfiles(paths):
    sum = 0
    for path in paths:
        if os.path.exists(path):
            print(f"Reading file from {path}")
            with open(path, mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    if row[0] == 'A':
                        sum += int(row[2][:-1])
        else:
            print(f"File does not exist: {path}")
    print(f"Sum of times {sum}")
    return sum

args = parse_arguments()

if args.operation == 'create':
    # Osoba 2

    # TODO
    paths = create_paths()
    
    writefiles(paths)

elif args.operation == 'read':
    # Osoba 2

    # TODO
    paths = read_paths()

    readfiles(paths)
