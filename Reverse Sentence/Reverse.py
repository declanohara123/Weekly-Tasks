# file to take an input sentence and return every second letter in reverse

sentence = (input("Enter a sentence : "))
sentence = sentence [::-1]
print ("Here is your sentence in reverse, and every second letter is:", sentence[::2])