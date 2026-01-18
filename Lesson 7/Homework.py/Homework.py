ord() #function returns ASCII Value
print(ord('A'))     #Output:65
print(ord('a'))     #Output:97
print(ord('O'))     #Output:48
print(ord('@'))     #Output:64


# chr()  function converts ASCII back to character
print(chr(65))       #Output:A      
print(chr(97))       #Output:a

# Get input from user
char = input("Enter a single character: ")


#Validate: Check if exactly one character
if type (char) is str and len(char) == 1:
    print(" Valid input!")
else:
    print("Please enter exactly ONE character")


# Get ASCII value
ascii_val = ord(char)

# Display the result
print(f"Character: (char)")
print(f"ASCII Value: ascii_val)
      

#Identify character type using ASCII ranges
if ascii_val >= and ascii<= 90:
    
