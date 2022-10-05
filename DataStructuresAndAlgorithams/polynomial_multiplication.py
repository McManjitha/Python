def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result


def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly


def multiply_optimized(poly1, poly2):
    new_poly = []
    if len(poly1) == 0 or len(poly2) == 0:
        return 0

    if len(poly1) == 1:
        for i in poly2:
            new_poly.append(i*poly1[0])
        return new_poly

    if len(poly2) == 1:
        for i in poly1:
            new_poly.append(i*poly2[0])
        return new_poly


    (poly1_0, poly1_1), (poly2_0, poly2_1) = split(poly1, poly2)

    
    v_x = multiply_optimized(poly1_0, poly2_1)
    u_x = multiply_optimized(poly1_0, poly2_0)
    w_x = multiply_optimized(poly1_1, poly2_0)
    z_x = multiply_optimized(poly1_1, poly2_1)

    expression_1 = increase_exponent(add(v_x, w_x), max(len(poly1), len(poly2))//2)
    new_z_x = increase_exponent(z_x, (len(poly1) + len(poly2)) - len(z_x) - 1)
    addition = add(u_x, expression_1)
    return add(addition, new_z_x)


poly1 = [0, 2, 4, 3, 9]
poly2 = [0, 1, 1]
print(multiply_optimized(poly1, poly2))
