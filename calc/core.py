"""Lógica de la calculadora. Este módulo nunca debe importar tkinter."""

from calc.ops.basic import add, divide, multiply, subtract
from calc.ops.percentage import percentage
from calc.ops.maximum import maximum
from calc.ops.floor_divide import floor_divide
from calc.ops.hypotenuse import hypotenuse

# Asocia la etiqueta de cada botón con la función que la implementa.
# La interfaz dibuja un botón por entrada, en este mismo orden.
OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": percentage,
    "max": maximum,
    "//": floor_divide,
    "hyp": hypotenuse,
}


def parse_number(text):
    """Convierte lo que escribe el usuario en un float. Acepta '3.5' y '3,5'."""
    cleaned = text.strip().replace(",", ".")
    if not cleaned:
        raise ValueError("Falta un número")
    try:
        return float(cleaned)
    except ValueError:
        raise ValueError(f"'{text}' no es un número") from None


def format_result(value):
    """Muestra 4.0 como '4' y evita ruido como 0.30000000000000004."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.10g}"


def calculate(a, symbol, b):
    """Aplica a `a` y `b` la operación identificada por `symbol`."""
    if symbol not in OPERATIONS:
        raise ValueError(f"Operación desconocida: {symbol}")
    operation = OPERATIONS[symbol]
    return operation(a, b)
