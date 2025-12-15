# Using the reduction technique propose an algorithm that computes the maximum number of
#squares of size 2 × 2 that can be fit in a right angled isosceles triangle of base B. One side
#of the square must be parallel to the base of the isosceles triangle. Base is the shortest side
#of the triangle.

# B = 1, 2, 3 the number of squares is 0;
# B = 4, 5 the number of squares is 1; 
# B = 6, 7 the number of squares is 3; 
# B = 8, 9 the number of squares is 6; 
# B = 10, 11 the number of squares is 10 


def max_squares_in_triangle(b):
    if b < 4:       #critical case
        return 0
    
    n = b // 2 - 1  #number of squares that can fit in the current base

    nrSquares = n + max_squares_in_triangle(b - 2)  #recursive call reducing the base by 2
    return nrSquares

B = int(input("Enter the base of the triangle: "))
nr = max_squares_in_triangle(B)
print(nr)
