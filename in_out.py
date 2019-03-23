import json


def get_json(filename):
    """It returns object parsed from json file with filename."""
    with open(filename) as data_file:
        return json.loads(json.load(data_file))


def update_json(filename, data):
    """Dump data to json format and write it to json file with filename."""
    with open(filename, 'w') as outfile:
        return json.dump(json.dumps(data), outfile)


def get_correct_value(string_designator):
    """"Return correct number from input.

    Function asks user to input number while it is not a correct number.
    If value is a correct number it will be returned.
    """
    while True:
        try:
            return int(input(string_designator))
        except ValueError:
            print("Value is not a number. Try again...")


def get_correct_date():
    """Return correct date.

    Function asks user to input correct date while
    it is not a correct date.
    If date is correct it will be returned.
    Date is an object with fields:
    'day','month','year'.
    """
    while True:
        day = get_correct_value("Day: ")
        month = get_correct_value("Month: ")
        year = get_correct_value("Year: ")
        if is_correct_date(day, month, year):
            return {"day": day, "month": month, "year": year}
        else:
            print("Date not correct.Try again...\n")


def is_correct_date(day, month, year):
    """Checks if date is correct.

    Function returns true if input date is correct
    in other case it returns false.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days_in_month[1] = 29
    return year > 2018 and 0 <= (month - 1) <= 12 and day <= days_in_month[month - 1]


def show_menu():
    print("1.Add task.")
    print("2.Delete tasks.")
    print("3.Change task.")
    print("4.Show tasks from the date.")
    print("5.Show tasks from the period")
    print("6.Show all tasks.")
    print("7.Exit.")


def catch_error(is_error_flag, error_message):
    """Function print error_message if is_error_flag is true."""
    if is_error_flag:
        print(error_message)


def pretty_print(task):
    """ Make beautiful form for print """
    if 0 < task['month'] < 10:
        month = "0" + str(task['month'])
    else:
        month = str(task['month'])
    if 0 < task['day'] < 10:
        day = "0" + str(task['day'])
    else:
        day = str(task['day'])
    print("Date: " + day + "/" + month + "/" + str(task['year']) + "\n" + "Task: " + task["task"] + "\n")
