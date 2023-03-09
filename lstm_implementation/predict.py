import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras


token = Tokenizer()
seq_length = 29
model = keras.models.load_model("lstm.h5")
poetry_length = 10


def generate_poetry(seed_text, n_lines):
  poem = ""
  for i in range(n_lines):
    text = []
    for _ in range(poetry_length):
      encoded = token.texts_to_sequences([seed_text])
      encoded = pad_sequences(encoded, maxlen=seq_length, padding='pre')

      y_pred = np.argmax(model.predict(encoded), axis=-1)

      predicted_word = ""
      for word, index in token.word_index.items():
        if index == y_pred:
          predicted_word = word
          break

      seed_text = seed_text + ' ' + predicted_word
      text.append(predicted_word)

    seed_text = text[-1]
    text = ' '.join(text)
    print(text)
    poem += text + "\n"
  print(poem)

  
print("Please enter a seed phrase")
seed = input()
print("Please enter the number of lines")
lines = int(input())

generate_poetry(seed, lines)