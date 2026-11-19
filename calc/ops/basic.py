"""Operaciones aritméticas básicas."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

def min(a, b):
    if a > b:
        return b
    else:
        return a

def max(a, b):
    if a > b:
        return a
    else:
        return b