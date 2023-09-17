'''Create a function that take a sentence and prints how many words in the sentence (do not count the space)'''
def sen_w (sentence):
  words=len(sentence.split())
  print(str(words))


sentence = "my name is roaia"
print(sen_w(sentence))