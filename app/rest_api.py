from flask import Flask
from flask_restful import Resource, reqparse, abort, Api
import backend

app = Flask(__name__)
api = Api(app)


class UserApi(Resource):
    def __init__(self):
        """Function for initialization args that will be parsed
        in json data that is in the body of a request."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username",
                                 type=str,
                                 required=True,
                                 help="No username provided",
                                 location='json')
        super(UserApi, self).__init__()

    @staticmethod
    def get():
        """Get request for get name of the current active user"""
        return {'username': backend.options['username']}, 200

    def put(self):
        """Put request for changing active user.
        Returns code - 200 if user has been successful changed,
        code - 400 if user hasn't been successful changed."""
        username = self.parser.parse_args()['username']
        if backend.activate_user(username):
            return {"message": "user has been successful changed."}, 200
        else:
            return {"error": "there is no such user."}, 400

    def post(self):
        """Post request for adding a new user.
        Returns code - 201 if user has been successful added,
        code - 400 if user hasn't been successful added"""
        username = self.parser.parse_args()['username']
        if backend.add_user(username):
            return {"message": "user has been successful created"}, 201
        else:
            return {"error": "user has been exist."}, 400


class TaskListApi(Resource):
    def __init__(self):
        """Function for initialization args that will be parsed
           in json data that is in the body of a request."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("date",
                                 type=dict,
                                 required=True,
                                 help='No date provided',
                                 location='json')
        self.parser.add_argument("task",
                                 type=str,
                                 required=True,
                                 help="No task provided",
                                 location='json')
        super(TaskListApi, self).__init__()

    @staticmethod
    def get():
        """Get request to get all tasks of the active user"""
        return backend.get_all_tasks()

    def post(self):
        """Post request to add a new task for the active user"""
        args = self.parser.parse_args()
        if backend.is_correct_date(args['date']):
            req = backend.add_task(args['date'],
                                   args['task'])
            backend.update_user_info()
            return req, 201
        abort(422)


class TaskApi(Resource):
    def __init__(self):
        """Function for initialization args that will be parsed
           in json data that is in the body of a request."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('task',
                                 type=str,
                                 required=True,
                                 help="No task provided",
                                 location='json')
        super(TaskApi, self).__init__()

    @staticmethod
    def get(task_id):
        """Get request for get task with the task_id.

        Returns empty object if there is no any task with the task_id,
        and if it's returns object."""
        return backend.get_task_with_id(task_id)

    def put(self, task_id):
        """Put request for change the task with the task_id.

        Returns empty object if there is no any task with the task_id,
        and if it's returns changed object."""
        args = self.parser.parse_args()
        req = backend.change_task(task_id,
                                  args['task'])
        backend.update_user_info()
        return req

    @staticmethod
    def delete(task_id):
        """Delete request for delete the task with the task_id.

        Returns empty object if there is no any task with the task_id,
        and if it's returns deleted object."""
        req = backend.delete_task(task_id)
        backend.update_user_info()
        return req


class TasksActions(Resource):
    def __init__(self):
        """Function for initialization args that will be parsed
           in json data that is in the body of a request."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("from",
                                 type=dict,
                                 location='json')
        self.parser.add_argument("to",
                                 type=dict,
                                 location='json')
        self.parser.add_argument("day",
                                 type=int,)
        self.parser.add_argument("month",
                                 type=int,)
        self.parser.add_argument("year",
                                 type=int,)
        super(TasksActions, self).__init__()

    def get(self):
        """Get request to get all tasks from the date.

        Day,month,year are the parameters of the url.
        If there are no any task at the date return empty list,
        in other case returns list with the task objects."""
        args = self.parser.parse_args()
        if args["day"] and args["month"] and args["year"]:
            date = {"day": args["day"],
                    "month": args["month"],
                    "year": args["year"]}
            if backend.is_correct_date(date):
                return backend.get_task_from_date(date)
            abort(422)
        abort(404)

    def post(self):
        """Post request to get all tasks from the period.

        From and to are in the json data of the request.
        If there are no any task at the period return empty list,
        in other case returns list with the task objects."""
        args = self.parser.parse_args()
        if args["from"] and args["to"] \
                and backend.is_correct_date(args["from"]) \
                and backend.is_correct_date(args["to"]):
            return backend.get_task_from_period(args["from"],
                                                args["to"]), 200
        abort(400)


api.add_resource(TaskListApi, '/tasks', endpoint='tasks')
api.add_resource(TaskApi, '/tasks/<int:task_id>', endpoint='task')
api.add_resource(TasksActions, '/tasks/actions', endpoint='actions')
api.add_resource(UserApi, '/user', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
