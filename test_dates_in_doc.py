import re
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable


class HeaderError(Exception):
    pass


class FormatError(HeaderError):
    pass


class DateError(HeaderError):
    pass


class DayNumberError(HeaderError):
    pass


class DayRangeError(DayNumberError):
    pass


def get_headers(text: str):
    return (line for line in text.split("\n") if line.startswith("##"))


only_day_number_header_regex = re.compile(r"^(\d+)$")
one_day_header_regex = re.compile(r"^(\d+) - (\d{1,2})\.(\d{1,2})\.(\d{4})$")
multi_day_header_regex = re.compile(
    r"^(\d+) \((\d{1,2})\.(\d{1,2})\.(\d{4})\) - Tag (\d+) \((\d{1,2})\.(\d{1,2})\.(\d{4})\)$"
)


def validate(headers: Iterable[str]):
    last_date = date(2024, 8, 20)  # The date before the diary started.
    last_day_number = 0
    for header_raw in headers:
        header = header_raw.removeprefix("## Tag ")
        if matched := only_day_number_header_regex.match(header):
            if int(matched.group(0)) != last_day_number + 1:
                raise DayNumberError(
                    f"Invalid day number {matched.group(0)}! Should be {last_day_number + 1}\n{header_raw}"
                )
            last_day_number += 1
            last_date += timedelta(1)

        elif matched := one_day_header_regex.match(header):
            day_number, day, month, year = map(int, matched.groups())
            if int(day_number) != last_day_number + 1:
                raise DayNumberError(f"Invalid day number {day_number}! Should be {last_day_number + 1}\n{header_raw}")

            if date(year, month, day) != last_date + timedelta(1):
                raise DateError(
                    f"Date {date(year, month, day)} does not match the required date {last_date + timedelta(1)}\n{header_raw}"
                )

            last_day_number = day_number
            last_date += timedelta(1)

        elif matched := multi_day_header_regex.match(header):
            (day_one_number, day_one, month_one, year_one,
             day_two_number, day_two, month_two, year_two) = map(int, matched.groups())

            date_one = date(year_one, month_one, day_one)
            date_two = date(year_two, month_two, day_two)

            if date_one != last_date + timedelta(1):
                raise DateError(
                    f"Date {date_one} does not match the required date {last_date + timedelta(1)}\n{header_raw}"
                )
            if day_one_number != last_day_number + 1:
                raise DayNumberError(f"Invalid day number {day_one_number}! Should be {last_day_number + 1}\n{header_raw}")

            date_difference = (date_two - date_one).days
            day_number_difference = day_two_number - day_one_number

            if date_difference != day_number_difference:
                raise DayRangeError(
                    f"Date range not correct: Date's difference is {date_difference},"
                    f" but the number's difference is {day_number_difference}\n{header_raw}"
                )
            last_day_number += date_difference + 1
            last_date += timedelta(date_difference + 1)

        else:
            raise FormatError(f"Header does not match regex!\n{header_raw}")


validate(get_headers((Path(__file__).parent / "docs/diary.md").read_text("utf-8")))
print("Diary headers are valid!")
