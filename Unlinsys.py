import sympy as sym


def jacobian(v_str, f_list):
    vars_ = sym.symbols(v_str)
    f = sym.sympify(f_list)
    J = sym.zeros(len(f), len(vars_))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars_):
            J[i, j] = sym.diff(fi, s)
    return J


def calculate_exp(exp, vars_, x0):
    return exp.subs((x, x0[i]) for i, x in enumerate(sym.symbols(vars_)))


def newton(vars_, F, x0, e=0.0001, iter_=0):
    """
    vars is str of yours undef variables, example: "x1, x2"
    F is list of functions as str with sympy syntax, example ['2**x1 + x2', 'sin(x1) + 3*x2']
    x0 is your start variables
    """
    # x0 == x from previous iter
    if len(vars_.split(' ')) != len(x0) or len(x0) != len(F):
        raise ValueError("Invalid amount of variables")
    J = jacobian(vars_, F)
    calc_J = sym.zeros(int(len(J)**0.5))
    # calculate J
    for i, exp in enumerate(J):
        calc_J[i] = calculate_exp(exp, vars_, x0)
    # calculate Functions with x0 values
    calc_F = sym.Matrix([calculate_exp(sym.parse_expr(exp), vars_, x0) for exp in F])
    # find delta x
    delta_x = calc_J.inv() * calc_F
    # calculate new x
    new_x = sym.Matrix(x0) - delta_x

    print(f"Iteration {iter_}:")
    print("Jacobian matrix: ")
    print(J)
    print("Solved jacobian: ")
    print([float(j) for j in calc_J])
    print("Calculated functions: ")
    print([float(f) for f in calc_F])
    print("Delta x: ")
    print([float(x) for x in delta_x])
    print("Next x: ")
    print([float(x) for x in new_x])
    print("\n")

    if max([abs(x) for x in delta_x]) <= e:
        return new_x
    else:
        return newton(vars_, F, new_x, e, iter_+1)
