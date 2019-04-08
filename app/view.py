import backend


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


def get_correct_date(message="Date: "):
    """Return correct date.

    Function asks user to input correct date while
    it is not a correct date.
    If date is correct it will be returned.
    Date is an object with fields:
    'day','month','year'.
    """
    print(message)
    while True:
        date = {"day": get_correct_value("Day: "),
                "month": get_correct_value("Month: "),
                "year": get_correct_value("Year: ")}
        if backend.is_correct_date(date):
            return date
        else:
            print("Date not correct.Try again...\n")


def show_menu_buttons():
    """Shows menu buttons"""
    print("1.Add task.")
    print("2.Delete tasks.")
    print("3.Change task.")
    print("4.Show task with the id.")
    print("5.Show tasks from the date.")
    print("6.Show tasks from the period")
    print("7.Show all tasks.")
    print("8.Exit.\n")


def show_authorization_buttons():
    """Show authorization buttons"""
    print("1.Add new user.")
    print("2.Choose an existing user.")
    print("3.Exit.\n")


def report_success_add():
    """Reports about successful adding new task"""
    print("The task has been successful added")


def report_success_change():
    """Reports about successful changing the task"""
    print("The task has been successful changed")


def report_success_delete():
    """Reports about successful deleting the task"""
    print("The task has been successful deleted")


def report_success_end_program():
    """Reports about successful end of the program"""
    print("The program has been successful ended\n"
          "and new data has been dumped into the file.")


def report_error_change():
    """Reports about error change"""
    print("There are no task with the id to change")


def report_error_delete():
    """Reports about error delete"""
    print("There are no task with the id to delete")


def report_no_task_from_date():
    """Reports about no task from date"""
    print("There are not any task from the date.")


def report_no_task_with_id():
    """Report about no task with the id"""
    print("There are not any task with the id")


def report_no_task_from_period():
    """Reports about no task from period"""
    print("There are not any task from the period.")


def report_zero_task():
    """Report about user does not have any task"""
    print("There are not any task in your planes.")


def report_user_exist():
    """Report about user exist."""
    print("There is a such user with the username.")


def report_user_not_exist():
    """Report about user doesn't exist."""
    print("There is not a such user with the username.")


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
    print("Date: " + day + "/" + month + "/" + str(task['year']))
    print("Task: " + task["task"])
    print("id: " + str(task['id']))
