from cs50 import get_string, get_float



def main():
    s = get_string("Text:")
    letters = count_letters(s)
    words = count_words(s)
    sentences = count_sentences(s)
    print(letters)
    print(words)
    print(sentences)
    L = (letters * 100)/ words
    S = (sentences * 100) / words
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)
    if grade >= 16:
        print("Grade 16+") 
    if grade < 1:
        print("Before Grade 1")
    if grade >= 1 and grade < 16: 
        print("Grade", grade)    

def count_letters(s):
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    return count

def count_words(s):
    return len(s.split())

def count_sentences(s):
    count = 0
    for i in s:
        if i == '.' or i == '?' or i == '!':
            count +=1
    return count

main()








