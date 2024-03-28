# Special Pythag Triple as defined in parameters given in Project Euler Problem #9
# 1) a + b + c = 1000
# 2) a < b < c     -- this condition is taken care of in main double for loop
# 3) a^2 + b^2 = c^2
import math


def is_special_pythag_triple(a: int, b: int) -> bool:
    c_squared = a**2 + b**2
    if a + b + int(c_squared**0.5) == 1000:
        return True
    return False

if __name__ == "__main__":
    print(' P I M P ')

    pythag_triple_vals = []
    broke = False

    # from work on paper, we know that (1000 - a)(1000 - b) = 500K
    # 500000 ~ 490000 = 700^2
    # so a and b must sum to be approx 2*700.
    # therefore: a and be must be somewhere in the range of 200 - 400 ~ (1000 - 200)(1000 - 400)
    for a in range(200, 401):
        for b in range(a + 1, 401):
            if is_special_pythag_triple(a, b):
                pythag_triple_vals.append(a)
                pythag_triple_vals.append(b)
                pythag_triple_vals.append(int((a**2 + b**2)**0.5))    # c
                broke = True
                break
        if (broke):
            break
    print(pythag_triple_vals)
    print(f'Product: {pythag_triple_vals[0] * pythag_triple_vals[1] * pythag_triple_vals[2]}')