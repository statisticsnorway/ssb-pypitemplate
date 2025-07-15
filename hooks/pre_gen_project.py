#!/usr/bin/env python
import csv
import sys
from pathlib import Path


def validate_department_number():
    """Validate the department number before project generation.

    If a department number is set, it is validated against a list of valid
    Statistics Norway departments as listed in `statistics_norway_departments.csv`.
    An updated csv file can be downloaded from this url:
    https://www.ssb.no/klass/klassifikasjoner/83

    Validates the department number provided in the template configuration.
    This function ensures that the department number meets certain criteria:
    it must be a digit and must exist in the lookup table generated from the
    CSV file. If invalid, error messages are displayed, and the process exits.

    Raises:
        SystemExit: If the department number is invalid or the department file is not found.
    """

    department_number = "{{ cookiecutter.department_number }}"
    if not department_number:
        return

    if not department_number.isdigit():
        print(f"Error: Department number '{department_number}' must be a valid number.")
        sys.exit(1)

    # Read the CSV file and create a lookup table
    template_dir = r"{{ cookiecutter._template }}"  # path to the template root dir
    department_file = (
        Path(template_dir).resolve() / "hooks" / "statistics_norway_departments.csv"
    )
    department_lookup = {}
    if department_file.exists():
        with department_file.open(encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                # Only use "departments/seksjoner", not "divisions/avdelinger"
                if row["level"] == "2":
                    department_lookup[row["code"]] = row["name"].rstrip()
    else:
        print(f"Error: Department file '{department_file}' not found.")
        sys.exit(1)

    # Validate that the department number exists in the lookup table and print the list
    # of valid numbers if it fails.
    if department_number not in department_lookup:
        print(f"Error: Department number '{department_number}' is not valid.")
        print("\nValid department numbers:")
        valid_codes = sorted(department_lookup.keys(), key=int)
        for code in valid_codes:
            print(f"  {code}: {department_lookup[code]}")
        sys.exit(1)


if __name__ == "__main__":
    validate_department_number()
