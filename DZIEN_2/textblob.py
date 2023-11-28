from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose pragramming language.")
print(wiki.tags)
print(wiki.noun_phrases)

test = TextBlob("Texblob is amazingly simple to use.What great fun!")
print(test.sentiment)

print(test.sentiment.polarity)

#polaryzacja [-1.0, 1.0]
#subjectivity [0,1.0]

#Tokenzacja
zen = TextBlob("Beautiful is better then ugly. "
               "Explicit is better then implicit. "
               "Simple is better then complex. "
               "abc123 {{{{45345}}}}")

print(zen.words)
print(zen.sentences)
print("_________________________________________________")

sentence = TextBlob("Use 4 spaces per indentation level.")
print(sentence.words)
print(sentence.words[2].singularize())
print(sentence.words[-1].pluralize())

print("_________________________________________________")

from textblob import Word

w = Word("octopi")

nw = w.lemmatize()
print(nw)

w2 = Word("went")
print(w2.lemmatize("v"))

print("_________________________________________________")

b= TextBlob("I havv goood speling!")
print(b.correct())
