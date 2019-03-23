import in_out


def change_task(json_data):
    """Change task.

    Function asks user input correct date and new task
    to this date while there are no task at the input date.
    Update json file with changed task.
    """
    while True:
        date = in_out.get_correct_date()
        for task in json_data:
            if task['day'] == date["day"] and task['month'] == date['month'] and task['year'] == date['year']:
                task['task'] = input("new task: ")
                return json_data
        in_out.catch_error(True, "No any task in the date. Try input date again...")


def print_task_from_date(json_data):
    """Print tasks from input date.

    Function prints all tasks from the input date.
    If there are no any task it says about it.
    """
    date = in_out.get_correct_date()
    is_not_task_at_data = True
    for task in json_data:
            if task['day'] == date['day'] and task['month'] == date['month'] and task['year'] == date['year']:
                in_out.pretty_print(task)
    in_out.catch_error(is_not_task_at_data, "No any task at the date")


def is_date_from_period(_from, task, _to):
    return _from['day'] <= task['day'] <= _to['day'] \
           and _from['month'] <= task['month'] <= _to['month'] \
           and _from['year'] <= task['year'] <= _to['year']


def print_task_from_period(json_data):
    """Print all tasks from the period.

    Function prints all tasks at the input period.
    If there are no any task it says about it.
    """
    print("Input from: ")
    _from = in_out.get_correct_date()
    print("Input to: ")
    _to = in_out.get_correct_date()
    no_task_from_period = True
    for task in json_data:
        if is_date_from_period(_from, task, _to):
            no_task_from_period = False
            in_out.pretty_print(task)
    in_out.catch_error(no_task_from_period, "No any task at the period")


def add_task(json_data):
    """ Add new task

    User input day,month,year and new task and
    function creates object and add this object
    to JSON file
    """
    add_data = in_out.get_correct_date()
    add_data['task'] = input("Task: ")
    json_data.append(add_data)
    return json_data


def delete_task(json_data):
    """ Remove task

    User input day,month,year and function
    deletes task from this date
    """
    flag = True
    date = in_out.get_correct_date()
    for task in json_data:
        if task['day'] == date['day'] and task['month'] == date['month'] and task['year'] == date['year']:
            json_data.remove(task)
            flag = False
    in_out.catch_error(flag,"No such date")


def print_all(json_data):
    """ Print all tasks """
    for task in json_data:
        in_out.pretty_print(task)
