The approach followed in the ngrams model is quite restrictive in nature, i.e, it takes a rhyme-scheme from the user. 
We decided to experiment with an LSTM model which will learn rhyme schemes on its own and only take the number of lines and some seed text as input. 
We created an LSTM model with 100 units and two LSTM layers, which takes an embedding of size 50 generated from a sequence length 25. 
We added a Dense layer of 100 neurons and "Relu" activation function. Our output layer is a "Softmax" layer of size equivalent to the vocabulary size.
We used categorical cross-entropy and a batch size of 16. Out of the 31k lines of lyrics, we could only train our model with 3000 lines for 200 epochs on Google Colab TPU at a time. 
We saved the model in a .h5 file and continued training sets for 3000 lines of corpus for 100 epochs.
