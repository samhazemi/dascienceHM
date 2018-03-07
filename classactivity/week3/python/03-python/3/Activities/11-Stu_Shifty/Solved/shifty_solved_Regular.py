import string

# List of letters in the alphabet
regularAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                   'g', 'h', 'i', 'j', 'k', 'l', 
                   'm', 'n', 'o', 'p', 'q', 'r', 
                   's', 't', 'u', 'v', 'w', 'x', 
                   'y', 'z']

# Empty list for the shifted letters of the cipher
cipherAlphabet = []

# Sentence to encode
word = input("Word to be ciphered: ")

# Number of letters we will be shifting to create our cipher
shiftNumber = int(input("Shift number? "))

# Variable to hold our encoded sentence
new_word = ""

# Build the Encoder (Cipher) List
# ---------------------------------------------------------------------------------

# Loop through the alphabet 
for i in range(0, len(regularAlphabet)-shiftNumber):

  # Position each letter shifted 
  cipherAlphabet.append(regularAlphabet[i+shiftNumber])

print(cipherAlphabet)

# Loop through the beginning and add  to  cipher list
for i in range(0, shiftNumber):

  # Position each letter shifted from its original position in the alphabet
  cipherAlphabet.append(regularAlphabet[i])

print(cipherAlphabet)

# Encode the Original Sentence
# ---------------------------------------------------------------------------------

# Loops through each character in the sentence string
for i in word:

  # Determine the index location of the letter in the alphabet 
  letterPosition = regularAlphabet.index(i)

  # Add the encoded letter to the new sentence
  new_word = new_word + cipherAlphabet[letterPosition]

# Print the sentence to the screen
print("Your ciphered word it " + new_word)
