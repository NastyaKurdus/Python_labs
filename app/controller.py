import backend
import view


def authorization():
    """Function realises input authorization for an user."""
    view.show_authorization_buttons()
    while True:
        ch = view.get_correct_value("Your choice: ")
        if ch == 1:
            return helper_authorization(backend.add_user,
                                        view.report_user_exist)
        elif ch == 2:
            return helper_authorization(backend.activate_user,
                                        view.report_user_not_exist)
        elif ch == 3:
            return
        else:
            print("Bad choice... Try again.")


def helper_authorization(handler_fn, error_input_fn):
    """Helper function for authorization."""
    while True:
        username = input("Input username: ")
        if handler_fn(username):
            return run_menu()
        else:
            error_input_fn()
        if without_continue():
            return


def run_menu():
    """Function realises an interactive menu"""
    while True:
        view.show_menu_buttons()
        if without_action() or without_continue():
            break
    backend.update_user_info()
    view.report_success_end_program()


def without_continue():
    """Returns true if user does not want to continue."""
    ch = input("Do you want to continue?(y/n)...")
    while True:
        if ch == "n" or ch == "N":
            return True
        elif ch == "y" or ch == "Y":
            return False
        else:
            ch = input("Please input only y/n...")


def without_action():
    """Returns true if user selects exit

    In functions call functions from user`s input value.
    Returns true if user want to exit, and false in
    other case"""
    key = view.get_correct_value("Select action: ")
    if key == 1:
        run_add_task()
    elif key == 2:
        run_delete_task()
    elif key == 3:
        run_change_task()
    elif key == 4:
        run_print_task_from_id()
    elif key == 5:
        run_print_task_from_date()
    elif key == 6:
        run_print_task_from_period()
    elif key == 7:
        run_print_all()
    elif key == 8:
        return True
    else:
        print("Not correct choice.Try again...")
    return False


def run_add_task():
    """Wrapper function for add_task"""
    if backend.add_task(view.get_correct_date(), input("Task: ")):
        view.report_success_add()


def run_delete_task():
    """Wrapper function for delete task"""
    if backend.delete_task(view.get_correct_value("Input id:")):
        view.report_success_delete()
    else:
        view.report_error_delete()


def run_change_task():
    """Wrapper function for change task"""
    if backend.change_task(view.get_correct_value("Input id: "),
                           input("New task: ")):
        view.report_success_change()
    else:
        view.report_error_change()


def run_print_task_from_id():
    """Wrapper function for get_task_with_id"""
    task = backend.get_task_with_id(view.get_correct_value("Input id: "))
    if task:
        view.pretty_print(task)
    else:
        view.report_no_task_with_id()


def run_print_task_from_date():
    """Wrapper function for get_task_from_date"""
    tasks = backend.get_task_from_date(view.get_correct_date())
    if tasks:
        for task in tasks:
            view.pretty_print(task)
    else:
        view.report_no_task_from_date()


def run_print_task_from_period():
    """Wrapper function for get_task_from_period"""
    tasks = backend.get_task_from_period(view.get_correct_date("From:"),
                                         view.get_correct_date("To:"))
    if tasks:
        for task in tasks:
            view.pretty_print(task)
    else:
        view.report_no_task_from_period()


def run_print_all():
    """Wrapper function for print_all_task"""
    json_data = backend.get_all_tasks()
    if json_data:
        for task in json_data:
            view.pretty_print(task)
    else:
        view.report_zero_task()


if __name__ == "__main__":
    authorization()
