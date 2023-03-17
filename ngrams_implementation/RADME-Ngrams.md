At first, we wanted to create a model that generates lyrics for a potential Bollywood song in romanized Hindi for a given rhyme scheme. 
For an n-grams-based model, we follow the rhyme-scheme conditioned solution used in  \cite{jain2020bollyrics}, Jain et al. 
Much like the work by \cite{xue-etal-2021-deeprapper} Xue et al., this method uses a reverse mechanism to generate lyrics in an auto-regressive manner. 
We create a .json file consisting of rhyme endings such that each rhyme ending contains exactly 5 characters. 
We also map sample bigrams with those rhyme endings. For example, some entries in our file look like " piya" : ["re piya"], "ne do": ["jaane do", "rahane do", "rehne do"], and so on. 
The rhyme-scheme and number of stanzas to be generated are taken as user input. The rhyme-scheme decided the number of lines each stanza will have. 
For example, lyrics with the rhyme-scheme "AACBBC" will have 6 lines per stanza whereas lyrics with the rhyme-scheme "ABAB" will have 4 lines per stanza. 
Next, with the given corpus, we create trigrams. For a given rhyme-scheme, we identify the types and randomly associate a rhyme ending for each type. 
For example, for a user input with rhyme-scheme "AACBBC", the model associates the types with rhyme-ending as: A: "e ham", B: "kasam", C: " ar ke". 
With that, the model assigns tokens and sets the last two words.
Now that the model knows the endings for each line, the line is completed by predicted the previous word in an auto-regressive fashion.
