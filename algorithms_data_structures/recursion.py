"""
1. Function should call itself.
2. Strong base case, prevent infinite recursion.
3. Alter n every iteration.

Expected output:

LINE 13 Running recursive(2)
I am in line 2
I am in line 7 and the value of n is 2 before -1
I am in line 2
I am in line 7 and the value of n is 1 before -1
I am in line 2
I am in line 4 and the value of n is 0 so recursion ends.
I am in line 9. After -1, the value of n is 1
Ran recursive(1), result is 0
I am in line 9. After -1, the value of n is 2
Ran recursive(2), result is 0
LINE 14 The result of recursive(2) is 0
"""

def recursive(n):
  print('I am in line 2')
  if n <= 0:
    print('I am in line 4 and the value of n is {} so recursion ends.'.format(n))
    return n
  else:
    print('I am in line 7 and the value of n is {} before -1'.format(n))
    result = recursive(n - 1)
    print('I am in line 9. After -1, the value of n is {}'.format(n))
    print('Ran recursive({}), result is {}'.format(n, result))
    return result

print('LINE 13 Running recursive(2)')  
print('LINE 14 The result of recursive(2) is {}'.format(recursive(2)))