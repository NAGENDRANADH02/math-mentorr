import sympy as sp
from config import VERIFIER_THRESHOLD

def verify(solution):
    try:
        if "=" in solution:
            expr = solution.split("=")[-1].strip()
            sp.sympify(expr)
            return 0.9
        return 0.7
    except:
        return 0.5