def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return ('Error: Too many problems.')
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        removed_spaces = []
        on_right = False
        operator = ""
        left_side = ""
        right_side = ""
        total = 0
        max_value = 0
        for char in problem:
            if char in ['/','*']:
                return ("Error: Operator must be '+' or '-'.")
          
            if char.isalpha():
                return("Error: Numbers must only contain digits.")
            if char == " ":
                removed_spaces          
            else:
                removed_spaces.append(char)
                if char == "+" or char == "-":
                    on_right = True
                    operator =char
                    continue
                                   
                  
                if on_right == False:
                    left_side +=char
                else:
                    right_side+=char
            if len(left_side) > 4 or len(right_side) > 4:
                return("Error: Numbers cannot be more than four digits.")
        if operator == "+":
            total = int(left_side) + int(right_side)
        else:
            total = int(left_side) -int(right_side)
        max_value= (max(len(right_side), len(left_side))+2)      
                        
        first_line.append(" " * (max_value - len(left_side)) + left_side)
        second_line.append(operator + " " + right_side.rjust(max_value - 2))
        dash_line.append("-" * max_value)
        answer_line.append(" " * (max_value - len(str(total))) + str(total))
 
    arranged = "    ".join(first_line) + "\n" + \
            "    ".join(second_line) + "\n" + \
           "    ".join(dash_line)

    if show_answers:
        arranged += "\n" + "    ".join(answer_line)

    return arranged

                       
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')


