OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    my_stack = []
    result = False
    # Случай "" исключительнй
    if not brackets_row:
        result = True

    for bracket in brackets_row:
        if bracket == OPEN_BRACKET:
            my_stack.append(CLOSE_BRACKET)
        # Если стек не пуст и в нем есть ), то удаляем из него последний элемент
        elif my_stack and bracket == CLOSE_BRACKET:
            my_stack.pop()
        # Если стек пуст, а в brackets_row встретился ")", то это False
        elif not my_stack and bracket == CLOSE_BRACKET:
            return False

    # Если после такой процедуры стэк пуст, то это True
    if not my_stack:
        result = True

    return result

if __name__ == '__main__':
    print(check_brackets("(()))"))