import unittest
from assertpy import assert_that
from modules.Note import Note


class NoteTest(unittest.TestCase):
    def test_Name(self) -> None:
        note = Note("testowanie", 5)
        assert_that(note.get_name()).is_equal_to("testowanie")

    def test_Note(self) -> None:
        note = Note("testowanie", 5)
        assert_that(note.get_note()).is_equal_to(5)

    def test_Note_Lower(self) -> None:
        note = Note("testowanie", 2)
        assert_that(note.get_note()).is_equal_to(2)

    def test_Note_Upper(self) -> None:
        note = Note("testowanie", 6)
        assert_that(note.get_note()).is_equal_to(6)

    def test_Note_Float_Lower(self) -> None:
        note = Note("testowanie", 2.0001)
        assert_that(note.get_note()).is_equal_to(2.0001)

    def test_Note_Float_Upper(self) -> None:
        note = Note("testowanie", 5.9999)
        assert_that(note.get_note()).is_equal_to(5.9999)

    def test_Empty_Name(self) -> None:
        self.assertRaises(ValueError, Note, "", 5)

    def test_None_Name(self) -> None:
        self.assertRaises(TypeError, Note, None, 4)

    def test_Note_Out_Of_Range_Lower(self) -> None:
        self.assertRaises(ValueError, Note, "testowanie", 1.9999)

    def test_Note_Out_Of_Range_Upper(self) -> None:
        self.assertRaises(ValueError, Note, "testowanie", 6.0001)
