import json


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


def get_json(filename):
    """It returns object parsed from json file with filename."""
    with open(filename) as data_file:
        return json.loads(json.load(data_file))


def update_json(filename, data):
    """Dump data to json format and write it to json file with filename."""
    with open(filename, 'w') as outfile:
        return json.dump(json.dumps(data), outfile)


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


def change_task():
    """Change task.

    Function asks user input correct date and new task
    to this date while there are no task at the input date.
    Update json file with changed task.
    """
    json_data = get_json('data.json')
    while True:
        date = get_correct_date()
        for task in json_data:
            if task['day'] == date["day"] and task['month'] == date['month'] and task['year'] == date['year']:
                task['task'] = input("new task: ")
                return update_json('data.json', json_data)
        catch_error(True, "No any task in the date. Try input date again...")


def print_task_from_date():
    """Print tasks from input date.

    Function prints all tasks from the input date.
    If there are no any task it says about it.
    """
    json_data = get_json('data.json')
    date = get_correct_date()
    is_not_task_at_data = True
    for task in json_data:
            if task['day'] == date['day'] and task['month'] == date['month'] and task['year'] == date['year']:
                pretty_print(task)
    catch_error(is_not_task_at_data, "No any task at the date")


def is_date_from_period(_from, task, _to):
    return _from['day'] <= task['day'] <= _to['day'] \
           and _from['month'] <= task['month'] <= _to['month'] \
           and _from['year'] <= task['year'] <= _to['year']


def print_task_from_period():
    """Print all tasks from the period.

    Function prints all tasks at the input period.
    If there are no any task it says about it.
    """
    json_data = get_json('data.json')
    print("Input from: ")
    _from = get_correct_date()
    print("Input to: ")
    _to = get_correct_date()
    no_task_from_period = True
    for task in json_data:
        if is_date_from_period(_from, task, _to):
            no_task_from_period = False
            pretty_print(task)
    catch_error(no_task_from_period, "No any task at the period")

def add_task():
    """ Add new task

    User input day,month,year and new task and
    function creates object and add this object
    to JSON file
    """
    add_data = get_correct_data()
    add_data['task'] = input("Task: ")
    json_data = get_json('data.json')
    json_data.append(add_data)
    update_json('data.json', json_data)


def delete_task(day, month, year):
    """ Remove task

    User input day,month,year and function
    deletes task from this date
    """
    json_data = get_json('data.json')
    flag = True
    for task in json_data:
        if task['day'] == day and task['month'] == month and task['year'] == year:
            json_data.remove(task)
            flag = False
            update_json('data.json', json_data)
    if flag:
        print("No such data")


def print_all():
    """ Print all tasks """
    json_data = get_json('data.json')
    for task in json_data:
        pretty_print(task)

