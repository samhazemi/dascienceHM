# List of letters in the alphabet
regularAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                   'g', 'h', 'i', 'j', 'k', 'l', 
                   'm', 'n', 'o', 'p', 'q', 'r', 
                   's', 't', 'u', 'v', 'w', 'x', 
                   'y', 'z']

# Empty list for the shifted letters of the cipher
cipherAlphabet = []

# Sentence to encode
sentence = input("Enter a sentence to be shifted: ")

# Number of letters we will be shifting to create our cipher
shiftNumber = int(input("Enter a shift number: "))

# Variable to hold our encoded sentence
newSentence = ""

# Loop through the alphabet (26 minus the shiftNumber times to account for overage)
for i in range(0, len(regularAlphabet)-shiftNumber):

  # Position each letter shifted from its original position in the alphabet
  cipherAlphabet.append(regularAlphabet[i+shiftNumber])

# Loop through the beginning part of the alphabet and separately add it to the cipher list
for i in range(0, shiftNumber):

  # Position each letter shifted from its original position in the alphabet
  cipherAlphabet.append(regularAlphabet[i])

# Loops through each character in the sentence string
for i in sentence:

  # Handle the space by skipping it
  if i != " ":

    # Determine the index location of the letter in the alphabet 
    letterPosition = regularAlphabet.index(i)

    # Add the encoded letter to the new sentence
    newSentence = newSentence + cipherAlphabet[letterPosition]
  
  # If the character is a space, immediately incorporate it. 
  else:
    newSentence = newSentence+" "

# Print the sentence to the screen
print("Your ciphened sentence is: " + newSentence)
