import backend
import in_out


def run_menu():
    json_data=in_out.get_json('data.json')
    while True:
        in_out.show_menu()
        key = in_out.get_correct_value("Select action: ")
        if key == 1:
            backend.add_task(json_data)
        elif key == 2:
            backend.delete_task(json_data)
        elif key == 3:
            backend.change_task(json_data)
        elif key == 4:
            backend.print_task_from_date(json_data)
        elif key == 5:
            backend.print_task_from_period(json_data)
        elif key == 6:
            backend.print_all(json_data)
        elif key == 7:
            in_out.update_json('data.json',json_data)
            break
        else:
            print("Not correct choice.Try again...")
        input("Press enter to continue: ")


if __name__=="__main__":
    run_menu()