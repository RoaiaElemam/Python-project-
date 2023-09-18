'''Create a function that take a sentence and word and remove the word from the sentencs '''

def sen (sentence,word):
  sentence = sentence.replace(word,"")
  print(sentence)

sentence = input("enter the sentence.....")
word = input("enter the word.....") 
print(sen(sentence,word))
