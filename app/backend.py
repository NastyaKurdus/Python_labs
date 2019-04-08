import utils

options = {}


def set_fields_options(username):
    """Set fields of options from input username."""
    options['path'] = 'data/' + username + ".json"
    options['json_data'] = utils.get_json(options['path'])
    options['username'] = username
    return True


def is_correct_date(date):
    """Checks if the date is correct.

    Function returns true if input date is correct
    in other case it returns false.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if date["year"] % 4 == 0:
        days_in_month[1] = 29
    return date["year"] > 2018 \
        and 0 <= (date["month"] - 1) < 12 \
        and date["day"] <= days_in_month[date["month"] - 1]


def is_date_equal(date1, date2):
    """Returns true if dates are equal"""
    return date1['day'] == date2['day']\
        and date1['month'] == date2['month'] \
        and date1['year'] == date2['year']


def is_date_from_period(_from, task, _to):
    """Returns true if _from <= task <= _to"""
    return _from['year'] < task['year'] < _to['year']\
        or (_from['year'] == task['year']
            and _from['month'] < task['month'])\
        or (_to['year'] == task['year']
            and task['month'] < _to['month'])\
        or (_from['year'] == task['year']
            and _from['month'] == task['month']
            and _from['day'] <= task['day'])\
        or (task['year'] == _to['year']
            and task['month'] == _to['month']
            and task['day'] <= _to['day'])


def change_task(task_id, new_task):
    """Change task.

    Function changes task with the input id.
    If there are no task with the input id
    returns false, in successful case returns changed object.
    """
    for task in options['json_data']:
        if task['id'] == task_id:
            task['task'] = new_task
            return task
    return False


def get_task_with_id(task_id):
    """Returns task with the input id."""
    for task in options['json_data']:
        if task['id'] == task_id:
            return task
    return {}


def get_task_from_date(date):
    """Returns tasks from input date.

    Function returns list of all tasks from the input date.
    If there are no any task it returns empty list in other case
    return list.
    """
    tasks_from_date = []
    for task in options['json_data']:
            if is_date_equal(task, date):
                tasks_from_date.append(task)
    return tasks_from_date


def get_task_from_period(_from, _to):
    """Returns all tasks from the period.

    Function returns list of all tasks at the input period.
    If there are no any task it returns empty array.
    """
    tasks_from_period = []
    for task in options['json_data']:
        if is_date_from_period(_from, task, _to):
            tasks_from_period.append(task)
    return tasks_from_period


def add_task(date, new_task):
    """ Add new task

    User input day,month,year and new task and
    function creates object and add this object
    to JSON array.Returns created object.
    """
    date['task'] = new_task
    if options['json_data']:
        date['id'] = options['json_data'][-1]['id'] + 1
    else:
        date['id'] = 1
    options['json_data'].append(date)
    return date


def delete_task(task_id):
    """ Remove task

    User input id and function
    deletes task from this id.Returns task
    if the was and empty object if was not.
    """
    for task in options['json_data']:
        if task['id'] == task_id:
            options['json_data'].remove(task)
            return task
    return {}


def add_user(username):
    """Function adds new user with username.

    If user exist - return false, if user doesn't
    exist it creates json file with 'username'.json name
    and writes to it an empty array.
    Sets active user to new user."""
    if utils.is_user_exist(username):
        return False
    else:
        utils.update_json([], 'data/' + username + ".json")
        set_fields_options(username)
        return True


def activate_user(username):
    """Function set active user to the existing user with username.

    If user doesn't exist - return false, if user
    exist it sets fields of options.
    Set active user to this user."""
    if utils.is_user_exist(username):
        return set_fields_options(username)
    else:
        return False


def get_all_tasks():
    """Function returns all task of the active user"""
    return options['json_data']


def update_user_info():
    """Function dump to file json_data of the active user"""
    return utils.update_json(options['json_data'], options['path'])
