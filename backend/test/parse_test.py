import os
import pdb

from backend.courses import parse_course_history

def compare_dictionaries(dict1, dict2):
    # Check if the keys are the same
    if sorted(dict1.keys()) != sorted(dict2.keys()):
        return False
    
    # Check if the values for each key are the same
    for key in dict1:
        if sorted(dict1[key]) != sorted(dict2[key]):
            return False
    
    return True

if __name__ == '__main__':
    file_idx = 0
    correct_name = 'Yuxuan Xia'
    correct_gpa = '0.001'

    correct_course_dict = [
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4', '&nbsp;'], ['CSCI-SHU - 410', 'Software Engineering', '4', '&nbsp;'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4', '&nbsp;']]},
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4', '&nbsp;'], ['CSCI-SHU - 410', 'Software Engineering', '4', '&nbsp;'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4', '&nbsp;']], 'Fall 2023': [['MUS-SHU - 152', 'Group Guqin, All Levels', '2', 'A'], ['CCSF-SHU - 123', 'Cont Chinese Political Thought', '4', 'A-'], ['CSCI-SHU - 375', 'Reinforcement Learning', '4', 'A-'], ['CSCI-SHU - 420', 'CS Senior Project', '4', 'A-']]},
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4', '&nbsp;'], ['CSCI-SHU - 410', 'Software Engineering', '4', '&nbsp;'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4', '&nbsp;']], 'Fall 2023': [['MUS-SHU - 152', 'Group Guqin, All Levels', '2', 'A'], ['CCSF-SHU - 123', 'Cont Chinese Political Thought', '4', 'A-'], ['CSCI-SHU - 375', 'Reinforcement Learning', '4', 'A-'], ['CSCI-SHU - 420', 'CS Senior Project', '4', 'A-']], 'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4', 'A'], ['MATH-UA - 120', 'Discrete Mathematics', '4', 'A'], ['CSCI-UA - 202', 'Operating Systems', '4', 'A'], ['NUTR-UE - 119', 'Nutrition and Health', '3', 'A-']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '', 'A'], ['MATH-UA - 120', 'Discrete Mathematics', '4', 'A'], ['CSCI-UA - 202', 'Operating Systems', '4', 'A'], ['NUTR-UE - 119', 'Nutrition and Health', '3', 'A-']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4', 'A'], ['MATH-UA - 120', 'Discrete Mathematics', '4', 'A'], ['CSCI-UA - 202', '', '4', 'A'], ['NUTR-UE - 119', 'Nutrition and Health', '3', 'A-']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4', 'A'], ['MATH-UA - 120', 'Discrete Mathematics', '4', 'A'], ['CSCI-UA - 202', 'Operating Systems', '4', ''], ['NUTR-UE - 119', 'Nutrition and Health', '3', '']]},
    ]
    test_path = True

    for file in ['test_case1.txt', 'test_case2.txt', 'test_case3.txt', 'test_case4.txt', 'test_case5.txt', 'test_case6.txt']:
        # pdb.set_trace()
        with open(os.path.join('./backend/test/course_history_tests', file), 'r') as f:
            text = f.read()
            name, gpa, course_dict = parse_course_history(text)

            test_path = test_path and name == correct_name
            test_path = test_path and gpa == correct_gpa
            test_path = test_path and compare_dictionaries(course_dict, correct_course_dict[file_idx])

            file_idx += 1
    
    if test_path:
        print('All tests passed!')
    else:
        print('Some tests failed!')