# task 1

grades = [5, 3, 4, 2, 1, 5, 3]

new_grades = [
    [grade, "bravo" if grade == 5 else "okay" if 5 > grade > 2 else "not good"]
    for grade in grades
]

print(new_grades)


# task 2
strings = ["({[}])", "([({}()){}])"]

def check_brackets(s):

    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char == ")" and (not stack or stack[-1] != "("):
            return False
        elif char == "}" and (not stack or stack[-1] != "{"):
            return False
        elif char == "]" and (not stack or stack[-1] != "["):
            return False
        else:
            if char in ")}]":
                stack.pop()
    return not stack

for e in strings:
    print(f"brackets: {e}\nare valid: {check_brackets(e)}\n")

