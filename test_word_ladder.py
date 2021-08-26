from word_ladder_testable import *
import unittest

class WordLadderTest(unittest.TestCase):



    def test_getNeighbours(self):
        self.pattern = 'a.'
        self.viableWords = ['aa', 'ae', 'be']
        self.seenWords = set(['aa'])
        self.potentialWords = []

        #Test normal
        self.assertEqual(getNeighbours(self.pattern, self.viableWords, self.seenWords, self.potentialWords), ["ae"])

if __name__ == '__main__':
    unittest.main()