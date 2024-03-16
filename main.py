from stack import Stack


def finish_string(string):
    open_string = ['(', '{', '[']
    close_string = [')', '}', ']']
    stack = Stack()

    if len(string) % 2 > 0:
        return 'Несбалансированно'

    for i, j in enumerate(string):
        if j in open_string:
            stack.push(j)
        elif j in close_string:
            if stack.is_empty():
                return 'Несбалансированно'
            elif open_string.index(stack.peek()) != close_string.index(j):
                return 'Несбалансированно'
            else:
                stack.pop()
                if stack.is_empty() and i == len(string) - 1:
                    return 'Сбалансированно'


if __name__ == '__main__':
    print(finish_string(input('Введите строку: ')))