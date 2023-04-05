# Text to Morse Code Converter

# Import morse code dictionary
from code import morse

# Display welcome and instruction messages
print("Welcome to the Morse Code Converter\n\n\n")
print("This converter accepts letters and numbers. No symbols or punctuation.\n")

# Ask for input string
text = input("Enter text string to convert: ").upper()

# Convert to morse code
output = "".join([morse[letter] + " " for letter in text])

print(output)



