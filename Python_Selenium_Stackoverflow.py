from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Markus\Downloads\23_01_2019\geckodriver-v0.24.0-win64\geckodriver.exe') # launch Firefox browser

browser.get('http://stackoverflow.com/questions?sort=votes')
title = browser.find_element_by_css_selector('h1').text # page title (first h1 element)
questions = browser.find_elements_by_css_selector('.question-summary') # question list
for question in questions: # iterate over questions
    question_title = question.find_element_by_css_selector('.summary h3 a').text
    question_excerpt = question.find_element_by_css_selector('.summary .excerpt').text
    question_vote = question.find_element_by_css_selector('.stats .vote .votes .vote-countpost').text

    print( "%s\n%s\n%s votes\n-----------\n" % (question_title, question_excerpt, question_vote))
