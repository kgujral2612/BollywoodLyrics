For the "adventures" part of our project, we wanted to explore decoder models to attain our goal. 
Due to the ease of access of the HuggingFace library : https://huggingface.co/, and its available models, we were able to conduct our experiment on Hing-GPT
- https://huggingface.co/l3cube-pune/hing-gpt a multi-lingual transformer model based on GPT-2 that is pre-trained on Hinglish (code-mixed Hindi and English). 

The dataset used to train the model consists of nearly 52.93M sentences (1.04B tokens) gathered from twitter. 
We fine-tuned the model on the data and used Google Colab GPU to further train the model for 5 epochs. 
Due to the unavailability of free resources, and timeout after the 5th epoch, we couldn't continue our experiment to reach valuable results and metrics. 
