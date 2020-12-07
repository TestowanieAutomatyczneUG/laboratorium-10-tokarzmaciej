import unittest
from src.sample.note import Note


class TestNote(unittest.TestCase):
    def test_check_name_positive(self):
        self.assertEqual(Note("myNote", 5.5).get_name(), "myNote")