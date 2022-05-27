from survey import AnonymousSurvey

question = 'What language did you first learn to speak'

anonymous_survey = AnonymousSurvey(question)
anonymous_survey.show_question()
print("print q to quit.\n")

while True:
    answer = input('Language:')
    if 'q'==answer:
        break
    anonymous_survey.store_response(answer)

anonymous_survey.show_responses()