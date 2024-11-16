"""
    I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    Any code taken from other sources is referenced within my code solution.
    Student ID: 20232173 (IIT ID) w20520610 (UOW ID) 
    Date: 11th December 2023
"""
from graphics import *
frequency = [] # This empty list stores the frequency of which the outcomes are repeated
coordinates = [] # This empty list stores the y coordinates of the histogram
outcome_list = [] # part 2 of the coursework is stores in this empty list
student_or_teacher = 0 # To figure out if the user is a student or staff
preferred_outcome = 0 # To figure out which output method the staff would like to see
exit_or_continue = '' # sentinel variable to exit the loop which enables the staff to enter more than one credits
range_check_success = False # This variable checks the success of the range check function
total_check_success = False # This variable checks the success of the total check function
progress_count = 0 # Keeps count of the number of students that progress
module_trailer_count = 0 # Keeps count of the number of students that progress module trailer
module_retriever_count = 0 # Keeps count of the number of students that do not progress
exclude_count = 0 # Keeps count of the number of students that are excluded
failed_outcome_count = 0 # Keeps count of the failed attempts when entering the credits
total_outcome_count = 0 # overall total outcome count of everything

def student_format():
    """ This Function is for the student to check his/her progression outcome """
    global range_check_success, total_check_success
    while True:
        while True:
            try:
                pass_credits = int(input('\nPlease enter your credits at pass: '))
                defer_credits = int(input('Please enter your credits at defer: '))
                fail_credits = int(input('Please enter your credits at fail: '))
                break
            except ValueError:
                print('Integer Required')
                continue

        range_check(pass_credits, defer_credits, fail_credits)
        total_check(pass_credits, defer_credits, fail_credits)
        progression_outcome(pass_credits, defer_credits, fail_credits)
        if (range_check_success and total_check_success) == True:
            break

def range_check(pass_credits, defer_credits, fail_credits):
    """ This function is to check if pass, defer and fail credits fit the range """
    global range_check_success
    if pass_credits % 20 == 0 and defer_credits % 20 == 0 and fail_credits % 20 == 0:
        range_check_success = True
    else:
        range_check_success = False

def total_check(pass_credits, defer_credits, fail_credits):
    """ This function is to check if pass, defer and fail credits sum up to 120 """
    global total_check_success
    if pass_credits + defer_credits + fail_credits == 120:
        total_check_success = True
    else:
        total_check_success = False

def progression_outcome(pass_credits, defer_credits, fail_credits):
    """ This function will display the progression outcome and add the result to the outcome_list """
    global range_check_success, total_check_success, progress_count, module_trailer_count, module_retriever_count, exclude_count, failed_outcome_count,outcome_list
    if range_check_success == True and total_check_success == True:
        if pass_credits == 120:
            print('Progress')
            progress_count += 1
            outcome_list.append(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}")
            
        elif pass_credits == 100:
            print('Progress (module trailer)')
            module_trailer_count += 1
            outcome_list.append(f"Module Trailer - {pass_credits}, {defer_credits}, {fail_credits}")
            
        elif fail_credits >= 80 and fail_credits <= 120:
            print('Exclude')
            exclude_count += 1
            outcome_list.append(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}")
            
        else:
            print('Do not progress - module retriever')
            module_retriever_count += 1
            outcome_list.append(f"Module Retriever - {pass_credits}, {defer_credits}, {fail_credits}")
            
    elif range_check_success == True and total_check_success == False:
        print('Total incorrect')
        failed_outcome_count += 1
        
    elif range_check_success == False and total_check_success == True:
        print('Out of range')
        failed_outcome_count += 1
        
    else:
        print('Out of range and Total incorrect')
        failed_outcome_count += 1

def histogram():
    """ This function will generate the histogram """
    global progress_count, module_trailer_count, module_retriever_count, exclude_count, total_outcome_count
    try:
        win = GraphWin('Histogram', 480, 480)

        progress = Rectangle(Point(25, 420), Point(125, coordinates[0]))
        progress.setFill(color_rgb(174,248,160))
        progress.draw(win)
        progress_text = Text(Point(75, 435), 'Progress')
        progress_text.setStyle('bold')
        progress_text.setSize(12)
        progress_text.draw(win)
        display_progress_count = Text(Point(75, (coordinates[0]-10)), str(progress_count))
        display_progress_count.setSize(10)
        display_progress_count.draw(win)

        module_trailer = Rectangle(Point(135, 420), Point(235, coordinates[1]))
        module_trailer.setFill(color_rgb(160,198,137))
        module_trailer.draw(win)
        trailer_text = Text(Point(185, 435), 'Trailer')
        trailer_text.setStyle('bold')
        trailer_text.setSize(12)
        trailer_text.draw(win)
        display_module_trailer_count = Text(Point(185, (coordinates[1]-10)), str(module_trailer_count))
        display_module_trailer_count.setSize(10)
        display_module_trailer_count.draw(win)

        module_retriever = Rectangle(Point(245, 420), Point(345, coordinates[2]))
        module_retriever.setFill(color_rgb(166,188,118))
        module_retriever.draw(win)
        retriever_text = Text(Point(295, 435), 'Retriever')
        retriever_text.setStyle('bold')
        retriever_text.setSize(12)
        retriever_text.draw(win)
        display_module_retriever_count = Text(Point(295, (coordinates[2]-10)), str(module_retriever_count))
        display_module_retriever_count.setSize(10)
        display_module_retriever_count.draw(win)

        exclude = Rectangle(Point(355, 420), Point(455, coordinates[3]))
        exclude.setFill(color_rgb(209,182,180))
        exclude.draw(win)
        exclude_text = Text(Point(405, 435), 'Exclude')
        exclude_text.setStyle('bold')
        exclude_text.setSize(12)
        exclude_text.draw(win)
        display_exclude_count = Text(Point(405, (coordinates[3]-10)), str(exclude_count))
        display_exclude_count.setSize(10)
        display_exclude_count.draw(win)

        x_axis = Line(Point(10, 420), Point(470, 420))
        x_axis.draw(win)

        title = Text(Point(130, 20), 'Histogram Results')
        title.setSize(20)
        title.setStyle('bold')
        title.draw(win)

        total_outcome_text = Text(Point(240, 460), str(total_outcome_count)+' Outcomes in total.')
        total_outcome_text.setStyle('bold')
        total_outcome_text.setSize(17)
        total_outcome_text.draw(win)

        win.getMouse()
        win.close()
    except GraphicsError:
        pass

def y_coordinates():
    """ This function will generate the necessary Y coordinates for the histogram """
    try:
        maximum_value = (max(frequency))
        gradient = 360//maximum_value
    except ZeroDivisionError:
        gradient = 0
    for i in range(len(frequency)):
        y = 420 - (gradient*int(frequency[i]))
        coordinates.append(y)    
    
def part_2_list():
    """ This function will print the elements of the list """
    for i in range(len(outcome_list)):
        print(outcome_list[i])

def part_3_file_handling():
    """ This function will save the outcomes in a text and print them back """
    text_file = open('Coursework.txt', 'a')
    for i in range(len(outcome_list)):
        text_file.write(f"{outcome_list[i]}\n")
    text_file.close()

    text_file = open('Coursework.txt', 'r')
    for line in text_file:
        print(line, end='')
    text_file.close()

while True: # while loop to check if it's student or staff
    try:    
        student_or_teacher = int(input('\n1. Student format\n2. Staff format\nEnter preferred number: '))
    except ValueError:
        print('\nPlease enter either 1 or 2')
    if student_or_teacher == 1:
        student_format()
        break
    elif student_or_teacher == 2:
        while True:
            try:
                preferred_outcome = int(input('\n1. Histogram (Part 1)\n2. List extension (Part 2)\n3. File handling (Part 3)\nEnter a preferred output method: '))
            except ValueError:
                print('\nPlease enter a valid output method')
            if preferred_outcome == 1 or preferred_outcome == 2 or preferred_outcome == 3:
                break
            else:
                print('\nPlease enter a valid output method')
        while exit_or_continue != 'q':
            while True:
                try:
                    pass_credits = int(input('\nPlease enter your credits at pass: '))
                    defer_credits = int(input('Please enter your credits at defer: '))
                    fail_credits = int(input('Please enter your credits at fail: '))
                    break
                except ValueError:
                    print('Integer Required')
                    continue
            
            range_check(pass_credits, defer_credits, fail_credits)
            total_check(pass_credits, defer_credits, fail_credits)
            progression_outcome(pass_credits, defer_credits, fail_credits)

            total_outcome_count = progress_count + module_trailer_count + module_retriever_count + exclude_count + failed_outcome_count

            exit_or_continue = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view the results: ")
        else:
            frequency.insert(0, progress_count)
            frequency.insert(1, module_trailer_count)
            frequency.insert(2, module_retriever_count)
            frequency.insert(3, exclude_count)
            match preferred_outcome:
                case 1:
                    y_coordinates()
                    histogram()
                case 2:
                    part_2_list()
                case 3:
                    part_3_file_handling()
            break
    else:
        print('\nPlease enter either 1 or 2')
