import json
from courses.recommendor.recommendor import Recommendor
from django.conf import settings

import os, sys
sys.path.append('../../backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'se_project.settings')

import django
django.setup()


def recommend(course_history, tense=False, identity='chinese'):
    recommendor = Recommendor(course_history, identity=identity, tense=tense)

    graduate_valid, recommend_courses = recommendor.recommend()

    return graduate_valid


if __name__ == "__main__":
    # test case 1: cs major student
    with open(os.path.join(settings.BASE_DIR, "test/course_recommend_test/test_course_history.json"), 'r') as json_file:
        course_history = json.load(json_file)
    print('+++++++++++++++++Test Case1+++++++++++++++++')
    graduate_valid = recommend(course_history.copy(), tense=True)
    print('Test Case 1.1 failed') if graduate_valid == False else print('Test Case 1.1 passed')
    graduate_valid = recommend(course_history.copy(), tense=False)
    print('Test Case 1.2 failed') if graduate_valid == False else print('Test Case 1.2 passed')
    graduate_valid = recommend(course_history.copy(), tense=False, identity='inter')
    print('Test Case 1.3 failed') if graduate_valid == False else print('Test Case 1.3 passed')
    graduate_valid = recommend(course_history.copy(), tense=True, identity='inter')
    print('Test Case 1.4 failed') if graduate_valid == False else print('Test Case 1.4 passed')
    print('\n')
    
    # test case 2: empty course history
    course_history = {}
    print('+++++++++++++++++Test Case2+++++++++++++++++')
    graduate_valid = recommend(course_history.copy(), tense=True)
    print('Test Case 2.1 failed') if graduate_valid == False else print('Test Case 2.1 passed')
    graduate_valid = recommend(course_history.copy(), tense=False)
    print('Test Case 2.2 failed') if graduate_valid == False else print('Test Case 2.2 passed')
    graduate_valid = recommend(course_history.copy(), tense=False, identity='inter')
    print('Test Case 2.3 failed') if graduate_valid == False else print('Test Case 2.3 passed')
    graduate_valid = recommend(course_history.copy(), tense=True, identity='inter')
    print('Test Case 2.4 failed') if graduate_valid == False else print('Test Case 2.4 passed')
    print('\n')

    # test case 3: bf major that cannot transfer to cs
    print('+++++++++++++++++Test Case3+++++++++++++++++')
    with open(os.path.join(settings.BASE_DIR, 'test/course_recommend_test/test_bf_course_history.json'), 'r') as json_file:
        course_history = json.load(json_file)
    graduate_valid = recommend(course_history.copy(), tense=True)
    print('Test Case 3.1 failed') if graduate_valid == True else print('Test Case 3.1 passed')
    graduate_valid = recommend(course_history.copy(), tense=False)
    print('Test Case 3.2 failed') if graduate_valid == True else print('Test Case 3.2 passed')
    graduate_valid = recommend(course_history.copy(), tense=False, identity='inter')
    print('Test Case 3.3 failed') if graduate_valid == True else print('Test Case 3.3 passed')
    graduate_valid = recommend(course_history.copy(), tense=True, identity='inter')
    print('Test Case 3.4 failed') if graduate_valid == True else print('Test Case 3.4 passed')
    print('\n')
