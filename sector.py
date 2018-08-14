#program to calculate the area of a sector
pi=22/7
radius = float ( input ( ' enter value for radius  \n  '))
angle = float (input ( ' enter value for angle  \n '  ))
sector = ( pi * radius ** 2 ) * ( angle / 360 )
print  ( ' area of a sector = ' , round (sector , 2 ))
