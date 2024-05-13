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
    graduate_valid = recommend(course_history, tense=True)
    assert graduate_valid == True, "Test Case 1.1 failed"
    graduate_valid = recommend(course_history, tense=False)
    assert graduate_valid == True, "Test Case 1.2 failed"
    graduate_valid = recommend(course_history, tense=False, identity='inter')
    assert graduate_valid == True, "Test Case 1.3 failed"
    graduate_valid = recommend(course_history, tense=True, identity='inter')
    assert graduate_valid == True, "Test Case 1.4 failed"

    print('\n\n')
    
    # test case 2: empty course history
    course_history = {}
    print('+++++++++++++++++Test Case2+++++++++++++++++')
    graduate_valid = recommend(course_history, tense=True)
    assert graduate_valid == True, "Test Case 2.1 failed"
    graduate_valid = recommend(course_history, tense=False)
    assert graduate_valid == True, "Test Case 2.2 failed"
    graduate_valid = recommend(course_history, tense=False, identity='inter')
    assert graduate_valid == True, "Test Case 2.3 failed"
    graduate_valid = recommend(course_history, tense=True, identity='inter')
    assert graduate_valid == True, "Test Case 2.4 failed"
    print('\n\n')

    # test case 3: bf major that cannot transfer to cs
    print('+++++++++++++++++Test Case3+++++++++++++++++')
    with open(os.path.join(settings.BASE_DIR, 'test/course_recommend_test/test_bf_course_history.json'), 'r') as json_file:
        course_history = json.load(json_file)
    graduate_valid = recommend(course_history, tense=True)
    assert graduate_valid == False, "Test Case 3.1 failed"
    graduate_valid = recommend(course_history, tense=False)
    assert graduate_valid == False, "Test Case 3.2 failed"
    graduate_valid = recommend(course_history, tense=False, identity='inter')
    assert graduate_valid == False, "Test Case 3.3 failed"
    graduate_valid = recommend(course_history, tense=True, identity='inter')
    print('\n\n')
