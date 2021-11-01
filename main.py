import Unlinsys as unlin

if __name__ == "__main__":

    # "x1 x2", ['x1 - x2 - 3', 'x1**2 - x2**2 - 9'], [1, 5], 0.000001
    # "x y", ['2*y - cos(x+1)', 'x + sin(y) + 0.4'], [-0.9, 0.5], 0.000001
    # "x y", ['x**4 + y**4 - 5', 'y - exp(-x)'], [1, 2], 0.0001
    solved = unlin.newton("x y", ['x**4 + y**4 - 5', 'y - 2.7**(-x)'], [0, 1.5], 0.0001)
    res = [float(x) for x in solved]
    print("Final result: ")
    print(res)
#     a = np.array([[1], [2]]) #  prev
#     b = np.array([[1, -1], [2, -4]]) # jacobi from prev
#     c = np.array([[-4], [-12]])  # f from prev
#     print(np.dot(np.linalg.inv(b), c), '\n') # delta x
#     print(a - np.dot(np.linalg.inv(b), c))  # next x
