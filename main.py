import math
radians = float(input('Enter radians to convert to degrees: '))
result = math.radians(radians)
# or
# result = (radians*180)/math.pi 
# although according to online the above equation should be correct, 1 radian does not equal pi in this equation
print(f'{radians} Radians in degrees is {result}')