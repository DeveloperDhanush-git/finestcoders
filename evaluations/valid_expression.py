def is_operand(ch):
    return ch.isalpha() or ch.isdigit()


def is_operator(ch):
    return ch in "+-*/%"


def is_valid(expr):
    stack = []
    prev = None

    openbrackets = "([{"
    closebrackets = ")]}"

    open_count = 0
    close_count = 0

    if not expr:
        return False

    if is_operator(expr[0]) or is_operator(expr[-1]):
        return False

    for ch in expr:
        if prev:
            if is_operand(prev) and is_operand(ch):
                return False
            if is_operator(prev) and is_operator(ch):
                return False
            if is_operand(prev) and ch in openbrackets:
                return False
            if prev in closebrackets and is_operand(ch):
                return False
            if is_operator(prev) and ch in closebrackets:
                return False
            if prev in openbrackets and is_operator(ch):
                return False
            if prev in openbrackets and ch in closebrackets:
                return False
            if prev in closebrackets and ch in openbrackets:
                return False

        if ch in openbrackets:
            open_count += 1
            stack.append(ch)
        elif is_operand(ch) or is_operator(ch):
            stack.append(ch)
        elif ch in closebrackets:
            close_count += 1
            if close_count > open_count:
                return False

            temp_operands = 0
            temp_operators = 0
            reduced_operands = 0

            while stack:
                top = stack.pop()
                if top in openbrackets:
                    break
                elif top == 'X':
                    temp_operands += 1
                    reduced_operands += 1
                elif is_operand(top):
                    temp_operands += 1
                elif is_operator(top):
                    temp_operators += 1

            if temp_operands != temp_operators + 1:
                return False
            if temp_operands == 1 and reduced_operands == 1:
                return False
            stack.append('X')

        prev = ch

    if open_count != close_count:
        return False

    operands = 0
    operators = 0

    for item in stack:
        if is_operand(item) or item == 'X':
            operands += 1
        elif is_operator(item):
            operators += 1

    return operands == operators + 1

expr = input("Enter an expression: ")
print(is_valid(expr))