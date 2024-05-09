import numpy as np
import math
import random

random.seed()

# Set numeric flag based on user input
def check_whole_num(i):
    try:
        int(i)
        return False
    except:
        print("Please Enter a Whole Number")
        return True
    
# Answer validation
def check_answer(u, a):
    if u == a:
        return True
    return False

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Two real and identical roots
        root = -b / (2 * a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


def central():
    answer = random.randint(0, 360)
    v1 = f"What is the measure of the arc if the central angle is: {answer}"
    v2 = f"What is the central angle if the arc measure is: {answer}"
    version = [v1, v2]
    pick = random.randint(0,1)
    question = version[pick]
    print(question)
    flag = True
    while flag:
        if not pick:
            user_input = input("Enter the arc measure: ")
            flag = check_whole_num(user_input)
        else:
            user_input = input("Enter the central angle: ")
            flag = check_whole_num(user_input)
    correct = check_answer(int(user_input), answer)
    if not correct:
        print("Incorrect, read up on the information and try again")
        print("Use this link to learn more:")
        print("https://www.nagwa.com/en/explainers/819158139295/")
    else:
        print("Congratulations, your answer is correct!")

def intercepted():
    initial = random.randrange(0, 180, 2)
    v1 = f"What is the measure of the arc if the inscribed angle is: {initial}"
    v2 = f"What is the inscribed angle if the arc measure is: {initial}"
    version = [v1, v2]
    
    pick = random.randint(0,1)
    question = version[pick]
    print(question)
    
    answer1 = initial * 2
    answer2 = initial / 2
    answer_list = [answer1, answer2]
    answer = answer_list[pick]
    flag = True
    while flag:
        if not pick:
            user_input = input("Enter the arc measure: ")
            flag = check_whole_num(user_input)
        else:
            user_input = input("Enter the inscribed angle: ")
            flag = check_whole_num(user_input)
    correct = check_answer(int(user_input), answer)
    if not correct:
        print("Incorrect, read up on the information and try again")
        print("Use this link to learn more:")
        print("https://flexbooks.ck12.org/cbook/ck-12-cbse-math-class-9/section/10.3/related/lesson/inscribed-angles-in-circles-bsc-geom/")
    else:
        print("Congratulations, your answer is correct!")

def exterior_angle():
  """Generates a quiz question about exterior angles of a circle.

  This function generates two random arc measures between 0 and 360 degrees,
  calculates the corresponding exterior angle, and asks the user for input.
  It then indicates whether the user's answer is correct.
  """
  arc1 = random.randrange(0, 360, 2)
  max_range = 360-arc1
  arc2 = random.randrange(0, max_range, 2)
  arc_measure_diff = abs(arc1 - arc2)

  # Exterior angle is half the difference between the measures of the intercepted arcs
  exterior_angle = arc_measure_diff / 2

  user_input = int(input(f"What is the exterior angle of a circle formed by two arcs measuring {arc1}° and {arc2}°? "))
  flag = False
  while flag:
      flag = check_whole_num(user_input)
  correct = check_answer(user_input, exterior_angle)
    
  if correct:
    print("Congratulations, your answer is correct!")
  else:
    print(f"Incorrect. The correct answer is {exterior_angle}°")
    print("Use this link to learn more:")
    print("https://k12.libretexts.org/Bookshelves/Mathematics/Geometry/06%3A_Circles/6.17%3A_Angles_Outside_a_Circle")

def interior_angles():
    seed1 = random.randint(0,3)
    options = ["arc RS", "arc ST", "arc TQ", "arc QR"]
    match seed1:
        case 0:
            seed2 = 2
        case 1:
            seed2 = 3
        case 2:
            seed2 = 0
        case 3:
            seed2 = 1
    num1 = random.randrange(0,358, 2)
    max_range = 360 - num1
    num2 = random.randrange(0, max_range, 2)
    print(f'Find all angle measures, given {options[seed1]} = {num1} and {options[seed2]} = {num2}')
    flag = True
    while flag:
        if (seed1 == 0) | (seed1 == 2):
            answer1 = (num1 + num2) / 2
            answer2 = 180 - answer1
            RVS = input("Angle RVS: ")
            SVT = input("Angle SVT: ")
            TVQ = input("Angle TVQ: ")
            QVR = input("Angle QVR: ")
            user_inputs = [RVS, SVT, TVQ, QVR]
            answers = [answer1, answer2, answer1, answer2]
            for i in range(len(user_inputs)):
                flag = check_whole_num(user_inputs[i])
                if flag == True:
                    break
                correct = check_answer(int(user_inputs[i]), int(answers[i]))
                if not correct:
                    break
        else:
            answer2 = (num1 + num2) / 2
            answer1 = 180 - answer2
            RVS = input("Angle RVS: ")
            SVT = input("Angle SVT: ")
            TVQ = input("Angle TVQ: ")
            QVR = input("Angle QVR: ")
            user_inputs = [RVS, SVT, TVQ, QVR]
            answers = [answer1, answer2, answer1, answer2]
            for i in range(len(user_inputs)):
                flag = check_whole_num(user_inputs[i])
                if flag == True:
                    break
                correct = check_answer(int(user_inputs[i]), int(answers[i]))
                if not correct:
                    break
    if not correct:
        print("Incorrect, read up on the information and try again")
        print("Use page 1 of this link to learn more:")
        print("https://www.rcboe.org/cms/lib010/GA01903614/Centricity/Domain/2859/Lesson%204%20Interior%20and%20Exterior%20Angles%20of%20Circles.pdf")
    else:
        print("Congratulations, your answer is correct!")

def complete_squares():
    coef_list = [1, 2, 4, 8, 16, 32, 64]
    num1 = random.choice(coef_list)
    num2 = random.choice(coef_list)
    num3 = random.randrange(0, 128, 2)
    same = True
    while (num1 == num2) | (num1 == num3):
        num2 = random.choice(coef_list)
        num3 = random.randrange(0, 128, 2)
    num_list = [num1, num2, num3]
    min_num = min(num_list)
    num_list.remove(min_num)
    max_num = max(num_list)
    num_list.remove(max_num)
    mid_num = num_list[0]
    formula = f"{min_num}x^2 + {mid_num}x + {max_num} = 0"
    print(f"Complete the square for the formula: {formula}")
    print("Your answer will be based on this format: a(x+b)^2 + c")
    print("If a, b, or c equal 1 or 0, please enter those values")
    ua = input("a: ")
    ub = input("b: ")
    uc = input("c: ")
    user_ans = [int(ua), int(ub), int(uc)]
    a = min_num
    b = (mid_num/(2 * a))
    c = max_num - (mid_num**2 / (4 * min_num))
    answer = [a, b, c]
    correct = check_answer(user_ans, answer)
    if not correct:
        print(f"Incorrect, your answers are {user_ans} the correct answers are: {answer}")
        print("Read up on the information and try again")
        print("https://www.mathsisfun.com/algebra/completing-square.html")
    else:
        print("Congratulations, your answer is correct")

def center_circle():
    coef_list = [1, 2, 4, 8, 16, 32, 64]
    coef_list_multiply = [-1, 1]
    iterations = 4
    num_list = []
    for i in range(iterations):
        num_list.append(random.choice(coef_list) * random.choice(coef_list_multiply))
    abs_list = list(map(abs, num_list))
    min_num = min(abs_list)
    removeable = abs_list.index(min_num)
    num_list.pop(removeable)
    max_num = max(num_list)
    num_list.remove(max_num)
    mid1 = num_list[0]
    mid2 =  num_list[1]
    formula = f"{min_num}x^2 + {mid1}x + {min_num}y^2 + {mid2}y + {max_num} = 0"
    print(f"Find the Center and Radius for a circle with the Formula: {formula}")
    print("Your answer for the Center point is based on the format the format: (h, k)")
    print("All Numbers will be rounded to the tenth place")
    print("Radius will be the absolute value")
    uh = input("h: ")
    uk = input("k: ")
    radius = input("Radius: ")
    user_answer = f"c = ({uh}, {uk}), r = {radius}"
    mid_a = (mid1/(2 * min_num))
    mid_b = (mid2/(2 * min_num))
    r_squared = abs(((max_num * -1) / min_num) + (mid1/2)**2 + (mid2/2)**2)
    answer = f"c = ({-1 * mid_a}, {-1 * mid_b}), r = {round(math.sqrt(r_squared), 1)}"
    if answer == user_answer:
        print("Your answer is correct!!!")
    else:
        print(f"Your answer is incorrect, the correct answer was: {answer} please try again")
        print(f"Your answer was: c = ({uh}, {uk}), r = {radius}")
        print(f"the correct answer was: {answer} please try again")
        print("Use the following link for extra help:")
        print("https://www.kristakingmath.com/blog/center-and-radius-of-a-circle")

def circle_formula():
    """Generates a circle quiz, asking the user to provide the equation"""

    # Generate center coordinates (both positive for simplicity)
    center_x = random.randrange(-10, 10)
    center_y = random.randrange(-10, 10)

    # Generate radius 
    radius = random.randrange(1, 10)

    # Calculate elements for the standard circle equation
    h = -center_x 
    k = -center_y
    r_squared = radius ** 2
    a = 2 * h
    b = 2 * k
    c = h**2 + k**2 - r_squared
    answer = [a, b, c]
    # Prompt the user for the equation 
    print(f"Given a circle with center ({center_x}, {center_y}) and radius {radius}, please provide its equation.")
    print("With the equation in the format: x^2 + Ax + y^2 + By + C = 0")
    print("Enter values for letters A-C")

    # Get user's input
    flag = True
    while flag:
        
        user_a = input("A: ")
        user_b = input("B: ")
        user_c = input("C: ")
        f1 = check_whole_num(user_a)
        f2 = check_whole_num(user_b)
        f3 = check_whole_num(user_c)
        if (f1 == False) & (f2 == False) & (f3 == False):
            flag = False
    user_answer = [int(user_a), int(user_b), int(user_c)]
    correct = check_answer(user_answer, answer)
    if not correct:
        print(f"Incorrect, your answer was {user_answer} the correct answer is: {answer} read up on the information and try again")
        print("Use this link to learn more:")
        print("https://byjus.com/maths/equation-of-a-circle/")
    else:
        print("Congratulations, your answer is correct!")

def find_distance():
    x1 = random.randint(-10,10)
    x2 = random.randint(-10,10)
    y1 = random.randint(-10,10)
    y2 = random.randint(-10,10)

    answer = round(math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2), 2)
    print(f'What is the distance between points ({x1}, {y1}) and ({x2},{y2})?')
    print("Round your answer to two decimal places")
    user_answer = input("Distance: ")
    correct = check_answer(float(user_answer), answer)
    if not correct:
        print(f"Incorrect, your answer was {user_answer} the correct answer is: {answer} read up on the information and try again")
        print("Use this link to learn more:")
        print("https://byjus.com/maths/distance-between-two-points-formula/")
    else:
        print("Congratulations, your answer is correct!")

def find_midpoint():
    x1 = random.randrange(-10,10, 2)
    x2 = random.randrange(-10,10, 2)
    y1 = random.randrange(-10,10, 2)
    y2 = random.randrange(-10,10, 2)
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2
    answer = f'({int(x3)},{int(y3)})'
    print(f'What is the midpoint between points ({x1}, {y1}) and ({x2},{y2})?')
    print("Type in the X and Y values for that point")
    flag = True
    while flag:
        ux = input("X: ")
        uy = input("Y: ")
        if not check_whole_num(ux) & check_whole_num(uy):
            flag = False
    user_answer = f"({ux},{uy})"
    correct = check_answer(user_answer, answer)
    if not correct:
        print(f"Incorrect, your answer was {user_answer} the correct answer is: {answer} read up on the information and try again")
        print("Use this link to learn more:")
        print("https://thirdspacelearning.com/us/math-resources/topic-guides/algebra/how-to-find-midpoint/")
    else:
        print("Congratulations, your answer is correct!")

def bonus_tangent_secant_segment():
  """Generates a quiz question about the Tangent Secant Segment Theorem.

  This function randomly selects two segments, assigns them random values,
  calculates the third segment, and prompts the user for input. It provides
  feedback on whether the answer is correct.
  """

  # Limit segment sizes to avoid excessively large calculations
  segment_limit = 20  

  segments = ['A', 'B', 'C']
  selected_segments = random.sample(segments, 2)

  # Assign random values to the selected segments
  segment_values = {
      selected_segments[0]: random.randint(1, segment_limit),
      selected_segments[1]: random.randint(1, segment_limit)
  }

  # Calculate the missing segment based on the theorem
  if 'C' not in selected_segments:  # C is the missing segment
      segment_values['C'] = round((segment_values['A']**2 - segment_values['B']**2) / segment_values['B'], 1)
  elif 'B' not in selected_segments:  # B is missing
      segment_values['B'] = round(max(solve_quadratic(1, segment_values['C'], (-1 * segment_values['A']**2))), 1)
  else:  # A is missing
      segment_values['A'] = round(math.sqrt(segment_values['B']**2 + (segment_values['B'] * segment_values['C'])), 1)
                                                                            
  # Ask the question
  question = f"In a tangent-secant segment theorem scenario, segments {selected_segments[0]} and {selected_segments[1]} measure {segment_values[selected_segments[0]]} and {segment_values[selected_segments[1]]} respectively. What is the measure of segment {segments[0] if 'A' not in selected_segments else segments[1] if 'B' not in selected_segments else segments[2]}?"
  print(question)
  user_input = float(input("Round Answer to Nearest Tenth Place: "))  # Allow for decimal answers

  answer = segment_values[segments[0] if 'A' not in selected_segments else segments[1] if 'B' not in selected_segments else segments[2]]

  correct = check_answer(user_input, answer)
  if not correct:
      print(f"Incorrect, your answer was {user_input} the correct answer is: {answer} read up on the information and try again")
      print("Use this link to learn more:")
      print("https://flexbooks.ck12.org/cbook/ck-12-basic-geometry-concepts/section/9.11/primary/lesson/segments-from-secants-and-tangents-bsc-geom/")
  else:
      print("Congratulations, your answer is correct!")