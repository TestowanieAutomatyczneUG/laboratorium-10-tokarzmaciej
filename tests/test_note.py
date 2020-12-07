import unittest
from src.sample.note import Note


class TestNote(unittest.TestCase):
    def test_check_name_positive(self):
        self.assertEqual(Note("myNote", 5.5).get_name(), "myNote")

    def test_check_note_positive(self):
        self.assertEqual(Note("testNote", 2.5).get_note(), 2.5)

    def test_name_type_error(self):
        self.assertRaisesRegex(TypeError, 'Bad type name', Note, False, 3.4)

    def test_name_value_empty(self):
        self.assertRaisesRegex(ValueError, 'Name values can not be '' or none', Note, '', 5.4)

    def test_name_value_null(self):
        self.assertRaisesRegex(ValueError, 'Name values can not be '' or none', Note, None, 4.5)

    def test_note_type_error(self):
        self.assertRaisesRegex(TypeError, 'Bad type note', Note, "test", True)

    def test_note_bad_range(self):
        self.assertRaisesRegex(ValueError, 'Note bad values', Note, "testRange", 6.5)
