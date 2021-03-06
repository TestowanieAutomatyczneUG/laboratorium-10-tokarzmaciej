from src.sample.notesStorage import NotesStorage
from src.sample.notesService import NotesService
from src.sample.note import Note
from unittest.mock import *
from unittest import TestCase, main


class testNotesService(TestCase):

    @patch.object(NotesStorage, 'add')
    def test_add_note(self, mock_method):
        mock_method.return_value = Note("Maciej", 4.5).note
        test_object = NotesService()
        result = test_object.add(Note("Maciej", 4.5))
        self.assertEqual(result, Note("Maciej", 4.5).note)

    @patch.object(NotesStorage, 'add')
    def test_add_note_type_error(self, mock_method):
        mock_method.side_effect = TypeError
        test_object = NotesService()
        result = test_object.add
        self.assertRaises(TypeError, result, False)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_average(self, mock_method):
        mock_method.return_value = [Note("Maciej", 4.0), Note("Maciej", 5.0), Note("Maciej", 3.0)]
        test_object = NotesService()
        result = test_object.averageOf("Maciej")
        self.assertEqual(result, 4)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_average_exception(self, mock_method):
        mock_method.return_value = []
        test_object = NotesService()
        result = test_object.averageOf
        self.assertRaisesRegex(Exception, "This person has not notes", result, "Maciej")

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_average_value_error(self, mock_method):
        mock_method.side_effect = ValueError
        test_object = NotesService()
        result = test_object.averageOf
        self.assertRaises(ValueError, result, 13)

    @patch.object(NotesStorage, 'clear')
    def test_clear(self, mock_method):
        mock_method.return_value = "data cleaned"
        test_object = NotesService()
        result = test_object.clear()
        self.assertEqual(result, "data cleaned")


if __name__ == '__main__':
    main()
