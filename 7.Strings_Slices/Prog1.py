#String array and functions
name = "Hai Students"
print(name[0]) # 0 th position character print
print(name[1])# 1 st position character print
print(name[-1]) # Last  position character print
print(name[-2]) # Last to 2nd character print
print(name[0:3]) # read the characters from 0 to 3
print(name[4:]) # read the character 4 to end
print(name[:5]) # read the character 0 to 5 th

print(name.find("Hai"))
# find the word in sentence and print the postion of the word
print(name.find("a")) # get the character postion

name="             Hello SrinivsaRao           "
print(name)
print(name.strip())# it removes the white space before and after the string (Trim)
print(len(name))# return length of the string with spaces
print(len(name.strip()))# return length of the string with out spaces
print(len(name.rstrip()))# return length of the string with out Right spaces
print(len(name.lstrip()))# return length of the string with out Left spaces
print(name.strip().lower()) # it prints lower case
print(name.strip().upper()) # it prints Upper Case
print(name.strip().capitalize()) # it prints Capitalize
print(name.replace('H','h')) # replaces H to small h
print(name.strip().replace('H','h')) # replaces H to small h
name="Ramesh$Kiran-Bharath$Mohan$Praveen"
print(name.split("$"))# split the words using special character
