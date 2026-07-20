#Rounded 2 decimals
print('{:.2f}'.format(5.39120))

#Percentage format
print('{:.3f}Grms'.format(10.12345))

# make the total string size AT LEAST 9 (including digits and points),
# fill with zeros to the left
print('{:0>9}'.format(3.499))
# make the total string size AT LEAST 2 (all included), fill with zeros to the left
print('{:0>2}'.format(3))
#right pading with zeros
#make the full size equal to 11, filling with zeros to the right
print('{:0<11}'.format(3.499))
#Use commas as thousands separator
print("{:,}".format(199556))

