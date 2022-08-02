import unittest
import translator



class testE2FTranslation(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.englishToFrench(None), ""
        , "Failed to translate correctly")
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour"
        , "Failed to translate correctly")



class testF2Etranslation(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.frenchToEnglish(None), ""
        , "Failed to translate correctly")
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello"
        , "Failed to Translate Correctly")


unittest.main()
