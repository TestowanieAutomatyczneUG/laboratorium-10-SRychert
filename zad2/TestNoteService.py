import unittest
from unittest.mock import *
from assertpy import assert_that
from Note import Note
from NoteStorage import NoteStorage
from NotesService import NoteService


class TestNoteService(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = NoteService()

    @patch.object(NoteStorage, 'add')
    def test_note_add(self, mock_method):
        mock_method.return_value = True
        note = Note("Seba", 5.99)
        assert_that(self.temp.add(note)).is_true()

    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_many_notes(self, mock_method):
        mock_method.return_value = [Note("Jan", 3.5), Note("Jan", 4.0), Note("Jan", 2.5), Note("Jan", 2.0)]
        assert_that(self.temp.averageOf("Jan")).is_close_to(3.0, 0.1)

    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_one_note(self, mock_method):
        mock_method.return_value = [Note("Mati", 3.0)]
        assert_that(self.temp.averageOf("Mati")).is_equal_to(3.0)

    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_no_notes(self, mock_method):
        mock_method.return_value = []
        assert_that(self.temp.averageOf("note")).is_equal_to(0.0)

    @patch.object(NoteStorage, "clear")
    def test_clear(self, mock_method):
        mock_method.return_value = True
        assert_that(self.temp.clear()).is_true()

    def tearDown(self) -> None:
        self.temp = None
