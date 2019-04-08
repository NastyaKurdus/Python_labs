import unittest
import backend


class TestBackend(unittest.TestCase):
    """Class for implementation tests for module backend"""

    def test_01_activate_user(self):
        self.assertTrue(backend.activate_user('test'))

    def test_02_add_task(self):
        self.assertEqual(backend.add_task({"day": 2, "month": 1, "year": 2020},
                                          "go to the birthday", ),
                         {"day": 2,
                          "month": 1,
                          "year": 2020,
                          "task": "go to the birthday",
                          'id': 1})

    def test_03_add_task(self):
        self.assertEqual(backend.add_task({"day": 1, "month": 1, "year": 2019},
                                          "go to the birthday", ),
                         {"day": 1,
                          "month": 1,
                          "year": 2019,
                          "task": "go to the birthday",
                          'id': 2})

    def test_04_change_task(self):
        self.assertEqual(backend.change_task(1,
                                             "go to the cinema", ),
                         {"day": 2,
                          "month": 1,
                          "year": 2020,
                          "task": "go to the cinema",
                          'id': 1})

    def test_05_change_task(self):
        self.assertFalse(backend.change_task(3, "go to the cinema", ))

    def test_06_get_tasks_from_date(self):
        self.assertEqual(backend.get_task_from_date({"day": 1,
                                                     "month": 1,
                                                     "year": 2019}, ),
                         [{"day": 1,
                           "month": 1,
                           "year": 2019,
                           "task": "go to the birthday",
                           "id": 2}])

    def test_07_get_tasks_from_period(self):
        self.assertEqual(backend.get_task_from_period({"day": 1,
                                                       "month": 1,
                                                       "year": 2019},
                                                      {"day": 1,
                                                       "month": 1,
                                                       "year": 2020}, ),
                         [{"day": 1,
                           "month": 1,
                           "year": 2019,
                           "task": "go to the birthday",
                           "id": 2}])

    def test_08_get_tasks_with_id(self):
        self.assertEqual(backend.get_task_with_id(2),
                         {"day": 1,
                          "month": 1,
                          "year": 2019,
                          "task": "go to the birthday",
                          "id": 2})

    def test_09_get_tasks_with_id(self):
        self.assertEqual(backend.get_task_with_id(3), {})

    def test_10_is_date_from_period(self):
        self.assertTrue(backend.is_date_from_period({"day": 1,
                                                     "month": 3,
                                                     "year": 2019},
                                                    {"day": 2,
                                                     "month": 3,
                                                     "year": 2019},
                                                    {"day": 1,
                                                     "month": 2,
                                                     "year": 2021}))

    def test_11_is_date_from_period(self):
        self.assertTrue(backend.is_date_from_period({"day": 1,
                                                     "month": 3,
                                                     "year": 2019},
                                                    {"day": 2,
                                                     "month": 3,
                                                     "year": 2019},
                                                    {"day": 1,
                                                     "month": 2,
                                                     "year": 2021}))

    def test_12_get_all_tasks(self):
        self.assertEqual(backend.get_all_tasks(),
                         [{"day": 2,
                           "month": 1,
                           "year": 2020,
                           "task": "go to the cinema",
                           "id": 1},
                          {"day": 1,
                           "month": 1,
                           "year": 2019,
                           "task": "go to the birthday",
                           'id': 2}])

    def test_13_delete_task(self):
        self.assertFalse(backend.delete_task(3))

    def test_14_delete_task(self):
        self.assertEqual(backend.delete_task(1),
                         {"day": 2,
                          "month": 1,
                          "year": 2020,
                          "task": "go to the cinema",
                          "id": 1})

    def test_15_add_user(self):
        self.assertFalse(backend.add_user('test'))

    def test_16_activate_user(self):
        self.assertFalse(backend.activate_user('some_no_exist_user'))

    def test_is_date_equal(self):
        self.assertTrue(backend.is_date_equal({"day": 1,
                                               "month": 2,
                                               "year": 2019},
                                              {"month": 2,
                                               "day": 1,
                                               "year": 2019}))

    def test_is_correct_date(self):
        self.assertTrue(backend.is_correct_date({"day": 1,
                                                 "month": 2,
                                                 "year": 2020}))


if __name__ == "__main__":
    unittest.main()
