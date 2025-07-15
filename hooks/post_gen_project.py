#!/usr/bin/env python
import csv
import json
import sys
from pathlib import Path


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


def set_department_name():
    """Set the department name in `pyproject.toml` based on the department number.

    If a Statistics Norway department number is set and is valid, the department name
    placeholder in `pyproject.toml` is replaced by the real department name.
    The department name if found by looking up the department number in the
    `statistics_norway_departments.csv` file.
    An updated csv file can be downloaded from this url:
    https://www.ssb.no/klass/klassifikasjoner/83
    """
    department_number = "{{ cookiecutter.department_number }}"
    if department_number and department_number.isdigit():
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

        department_name = f"Statistics Norway, {department_lookup.get(department_number, 'Unknown')} Department ({department_number})"

        # Replace __DEPARTMENT_NAME__ in the pyproject.toml file
        pyproject_file = Path("pyproject.toml")
        if pyproject_file.exists():
            content = pyproject_file.read_text(encoding="utf-8")
            updated_content = content.replace("__DEPARTMENT_NAME__", department_name)
            pyproject_file.write_text(updated_content, encoding="utf-8")


if __name__ == "__main__":
    reindent_cookiecutter_json()
    set_department_name()
