#A pyhton program to calculate the area of a cylinder
pi = 22/7
height = float (input ( ' enter value for height ' ))
radius = float ( input ( ' enter value for radius ' ))
area = ( ( 2 * pi * radius) * height) + (( pi * radius ** 2 ) * 2 )
print ( ' area of a cylinder = ' ,  area)
