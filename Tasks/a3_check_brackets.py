def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    open_bracket = '('
    close_bracket = ')'
    my_stack = []

    # Случай "" исключительнй, если "", то ничего уже проверять не надо - сразу заканчиваем выполнение
    if not brackets_row:
        return True

    for bracket in brackets_row:
        if bracket == open_bracket:
            my_stack.append(close_bracket)
        # Если стек не пуст и в нем есть ), то удаляем из него последний элемент
        elif my_stack and bracket == close_bracket:
            my_stack.pop()
        # Если стек пуст, а нам встретился ), то это False
        elif not my_stack and bracket == close_bracket:
            return False

    return True if not my_stack else False

if __name__ == '__main__':
    print(check_brackets("(()))"))