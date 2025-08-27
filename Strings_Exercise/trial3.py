#Indexing of strings
a = "Hello, World!" 
b = "Hello"
c = "World"   
print(a[1]) #prints the character at index 1
print(a[-1]) #prints the last character 

#Slicing of strings
print(a[0:5]) #prints characters from index 0 to 4
print(a[7:]) #prints characters from index 7 to the end
print(a[::2]) #prints every second character
print(a[::-1]) #prints the string in reverse order


#upper case and lower case
print(a.upper()) #prints the string in upper case   
print(a.lower()) #prints the string in lower case   

#Concatenation of strings
print(b + " " + c) #prints "Hello World"

#Repetition of strings
print(b * 4)