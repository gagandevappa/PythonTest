"""Add Function"""
def add(a, b):
    return a+b

"""subtract Function"""
def subtract(a, b):
    return a-b

"""Multiply Function"""
def multiply(a, b):
    return a*b

"""Divide Function"""
def divide(a, b):
    if (b == 0):
        raise ValueError("The number not divisible by zero")
    else:
        return a/b