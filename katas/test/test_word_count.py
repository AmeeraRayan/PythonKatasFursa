import unittest
from katas.word_count import count_words  # adjust path if needed

class TestCountWords(unittest.TestCase):
    def test_regular_sentence(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("   Too   many    spaces    here   "), 4)

    def test_sentence_with_punctuation(self):
        self.assertEqual(count_words("Hello, world! How are you?"), 5)

    def test_only_spaces(self):
        self.assertEqual(count_words("        "), 0)
