import os
from ..courses.parse_course_history import parse_course_history

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

    correct_course_dict = [
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4'], ['CSCI-SHU - 410', 'Software Engineering', '4'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4']]},
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4'], ['CSCI-SHU - 410', 'Software Engineering', '4'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4']], 'Fall 2023': [['MUS-SHU - 152', 'Group Guqin, All Levels', '2'], ['CCSF-SHU - 123', 'Cont Chinese Political Thought', '4'], ['CSCI-SHU - 375', 'Reinforcement Learning', '4'], ['CSCI-SHU - 420', 'CS Senior Project', '4']]},
        {'Spring 2024': [['CSCI-SHU - 220', 'Algorithms', '4'], ['CSCI-SHU - 410', 'Software Engineering', '4'], ['CSCI-SHU - 997', 'Computer Sci Independent Study', '4']], 'Fall 2023': [['MUS-SHU - 152', 'Group Guqin, All Levels', '2'], ['CCSF-SHU - 123', 'Cont Chinese Political Thought', '4'], ['CSCI-SHU - 375', 'Reinforcement Learning', '4'], ['CSCI-SHU - 420', 'CS Senior Project', '4']], 'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4'], ['MATH-UA - 120', 'Discrete Mathematics', '4'], ['CSCI-UA - 202', 'Operating Systems', '4'], ['NUTR-UE - 119', 'Nutrition and Health', '3']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', ''], ['MATH-UA - 120', 'Discrete Mathematics', '4'], ['CSCI-UA - 202', 'Operating Systems', '4'], ['NUTR-UE - 119', 'Nutrition and Health', '3']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4'], ['MATH-UA - 120', 'Discrete Mathematics', '4'], ['CSCI-UA - 202', '', '4'], ['NUTR-UE - 119', 'Nutrition and Health', '3']]},
        {'Fall 2022': [['CAMS-UA - 110', 'The Science of Happiness', '4'], ['MATH-UA - 120', 'Discrete Mathematics', '4'], ['CSCI-UA - 202', 'Operating Systems', '4'], ['NUTR-UE - 119', 'Nutrition and Health', '3']]},
    ]
    test_pass = [True for i in range(6)]
    test_idx = 0

    for file in ['test_case1.txt', 'test_case2.txt', 'test_case3.txt', 'test_case4.txt', 'test_case5.txt', 'test_case6.txt']:

        with open(os.path.join('./backend/test/course_history_tests', file), 'r') as f:
            text = f.read()
            course_dict = parse_course_history(text)

            test_pass[test_idx] = compare_dictionaries(course_dict, correct_course_dict[file_idx])

            file_idx += 1
            
        test_idx += 1
    
    for i in range(6):
        if test_pass[i]:
            print(f"Test case {i+1} passed")
        else:
            print(f"Test case {i+1} failed")