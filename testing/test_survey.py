import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        self.question = 'What language did u first learn to speak'
        self.my_survey = AnonymousSurvey(self.question)
        self.responses = ['Telugu', 'English', 'Tamil', 'Kannada']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multiple_responses(self):

        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
        self.my_survey.store_response('Hindi')
        self.assertNotIn('hindi', self.my_survey.responses)

unittest.main()