'''Create a function that take a sentence and prints the sentencs without duplicated words'''


def remove_dupli(sentence):
	word=sentence.split(" ")
	R=[]
	for i in word:
		if i not in R:
			R.append(i)
	return " ".join (R)		

sentence = "my name is is roaia"
print(remove_dupli(sentence))

















