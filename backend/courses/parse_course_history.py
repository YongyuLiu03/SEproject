import pdb

def parse_semester(semester, content):
    semester_lst = []

    # iterate through lines
    for line in range(len(content)):
        if '"Catalog Number"' in content[line]:
            # get the course number
            course_num = content[line][88+len(semester)-1:]
            course_num = course_num[:course_num.find("<")]
            
            # get the course name
            course_name = content[line+1][71+len(semester)-1:]
            course_name = course_name[:course_name.find("<")]

            # get the credits
            course_credits = content[line+3][75+len(semester)-1:]
            course_credits = course_credits[:course_credits.find("<")]

            # get the Grade
            course_grade = content[line+5][77+len(semester)-1:]
            course_grade = course_grade[:course_grade.find("<")]

            semester_lst.append([course_num, course_name, course_credits, course_grade])

    return semester_lst


def parse_course_history(text):
    lst = text.split("\n")

    # find the name
    rough_location = text.find('class="IS_BB_LINKS_MENU_DESKTOP"')
    rough_name_parse = text[rough_location+38:rough_location+38+20]
    precise_name = rough_name_parse[:rough_name_parse.find('<')]

    # update text
    text = text[rough_location:]

    # parse GPA
    text = text[text.find("Cumulative"):]  # update text
    gpa = text[len("Cumulative GPA: "):text.find('<')]

    # find the courses
    text = text[:text.find("End target:")].split("\n")

    # every <h3> is a semester indication, so we count the size
    semester_dict = {}
    semester = None

    i = 0
    while i < len(text):
        line = text[i]

        if line[:4] == '<h3>':
            increment = 1
            semester = line[4:line.find('</')]
            
            # get the semester
            end = False
            while not end:
                if "</table>" in text[increment+i]:
                    end = True
                increment += 1
            
            semester_content = text[i:increment+i]

            semester_dict[semester] = parse_semester(semester, semester_content)

            i += increment

        i += 1

    return precise_name, gpa


if __name__ == '__main__':
    # Open the file in read mode ('r')
    with open('./test.txt', 'r') as file:
        # Read all lines into a list
        file_contents = file.read()

    parse_albert(file_contents)

    # {'Fall 2022': [['Course Num', 'Course Name', 'Final Grade', 'Credits'], ['Course Num', 'Course Name', 'Final Grade'], ['Course Num', 'Course Name', 'Final Grade']]}
    

