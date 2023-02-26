#!/usr/bin/env python3

"""_summary_
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    """


def isValid(s: str = '') -> bool:
    """It define if a string is valid or not

    Args:
        s (str, optional): string to check if is valid. Defaults to ''.

    Returns:
        bool: True if valid, False otherwise
    """
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    if len(s) <= 1:
        return False
    stack = []
    for _char in s:
        if _char in close_to_open:
            if stack and stack[-1] == close_to_open[_char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(_char)
    return not bool(stack)


print(isValid("()"))
print(isValid())
print(isValid("{}"))
print(isValid("()[]{}"))
print(isValid("([)]"))
