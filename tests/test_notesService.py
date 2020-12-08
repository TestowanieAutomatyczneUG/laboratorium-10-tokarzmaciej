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


if __name__ == '__main__':
    main()
