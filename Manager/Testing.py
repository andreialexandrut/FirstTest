import unittest
from Validate import ValidateActions
from Persistence import DataPersistence
from ProgramManager import todo_list_obj


class TestProgramManager(unittest.TestCase):
    def test_todo_title_len(self):
        self.assertEqual(ValidateActions.check_title("Test"), 0)

    def test_file_persistence(self):  # I'mma check the data persistence
        self.assertEqual(len(DataPersistence.read_json()), len(todo_list_obj.todo_list))
