import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

file = open('all_lyrics.txt','r')
data = file.read()
file.close()


original_corpus = data.lower().split("\n")
corpus = original_corpus[:500]
print(len(corpus))


token = Tokenizer()
token.fit_on_texts(corpus)

encoded_text = token.texts_to_sequences(corpus)
# vocabulary size should be + 1
vocab_size = len(token.word_counts) + 1

datalist = []
for d in encoded_text:
  if len(d)>1:
    for i in range(2, len(d)):
      datalist.append(d[:i])

max_length = 30
sequences = pad_sequences(datalist, maxlen=max_length, padding='pre')
X = sequences[:, :-1]
y = sequences[:, -1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]
print(seq_length)

model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 64
epochs = 500

model.fit(X, y, batch_size=batch_size, epochs=epochs, shuffle=True, verbose=2)

model.save("lstm.h5")
