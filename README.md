# BollywoodLyrics

Project for CS510- Adventures in NLP class by Prof. Ameeta Agrawal @ Portland State University.

This is an automatic Lyrics Generator for Romanized Hindi based on [this research paper](https://arxiv.org/pdf/2007.12916.pdf). 
The original implementation of the paper can be found on [this github repository](https://github.com/lingo-iitgn/Bollyrics).

The journey behind this repo has been summarized in [this medium article](https://medium.com/@kgujral_49148/lyrics-generation-in-romanized-hindi-using-n-grams-lstm-gpt-models-29c9fbb73829). Be sure to check that out!

This code contains 3 implementations for lyrics generation.

1) ngrams-based model
2) LSTM
3) GPT-2 (Hing GPT)

The project report contains details about the model implementation, results, conclusion and direction for future work. It can be found at [this link](https://drive.google.com/file/d/1X1PLt1ncoadn44EdO2PlUgGAGV0D1Urm/view?usp=share_link).

### Sample Results
##### NGrams
```diff
Kishmish Varga Meetha Sa Dard Hone Lagaa
Katil Aankhon Wale Dilbur Matwale Dil Hai Mushkil Hai
Chaahe Jo Maang Le Tu Ragon Mein Hone Lagaa
Doob Ke Phir Jise Mushkil Hai

Ye Dil Hai Dil Kaa Kasam Aisa Lagaa
Tell Me Baby Kyaa Khayaal Hai
Har Karam Chaaha Tujhe Aisa Lagaa
Now Tell Me Baby Kyaa Khayaal Hai
```

##### LSTM
```diff

Pahale Kabhi Ajanabi The Ab Khud Hi Door Hai
Ladkhadaaye Kadam Chale Aaye Ab Door Hai
Duaoon Ki Mujhe Zarurat Hai
Kyun Tu Itani Door Hai
Woh Paas Jo Door Hai
Hai Kisi Aur Kaa Mujhe Sochta Koi Aur Hai
Saanso Me Tu Aur Hai
Kuch Tum Kehna Inaki Aadat Hai
Tumhein Jo Maine Dekha Nahi Hai Koi Aur Hai
Jaan Chali Naa Jaaye Koyi Aur Hai
```



##### GPT-2

```diff
soona sa main 
hain suuni see bahen ye meri 
teri taraf hee jaati raahen ye meri 
main chal raha bin tere tanhai mein 
ek too hee mujko dikhe parchaai mein 
main bhul sa gaya hoon muskuraana 
bar is hon ke sang tum bhee aa jan aa 
main bhul sa gaya hoon muskuraana 
bar is hon ke sang tum bhee aa jan aa 

```


