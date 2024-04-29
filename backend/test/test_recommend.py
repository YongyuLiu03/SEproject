import pdb
import json
from ..courses.recommendor.recommendor import Recommendor


def recommend(course_history):
    recommendor = Recommendor(course_history, identity='chinese', tense=False)
    
    graduate_valid, recommend_courses = recommendor.recommend()

    if not graduate_valid:
        print("You cannot complete the CS major on a regular 4 courses per semester schedule, consider the overload or summer terms")
    else:
        print(recommend_courses)


if __name__ == "__main__":
    # test case 1: cs major student
    with open('backend/test/course_recommend_test/test_course_history.json', 'r') as json_file:
        course_history = json.load(json_file)
    print('+++++++++++++++++Test Case1+++++++++++++++++')
    recommend(course_history)
    print('\n\n')
    
    # test case 2: empty course history
    course_history = {}
    print('+++++++++++++++++Test Case2+++++++++++++++++')
    recommend(course_history)
    print('\n\n')

    # test case 3: bf major that cannot transfer to cs
    print('+++++++++++++++++Test Case3+++++++++++++++++')
    with open('backend/test/course_recommend_test/test_bf_course_history.json', 'r') as json_file:
        course_history = json.load(json_file)
    recommend(course_history)
    print('\n\n')
