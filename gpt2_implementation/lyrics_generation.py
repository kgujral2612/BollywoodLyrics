from transformers import AutoTokenizer, AutoModelForCausalLM
import torch



# user input
'''
print("Please enter a rhyme scheme. For eg: AABB, ABAB, ABCABC, AACBBC, etc: ")
rhyme_scheme = input()
print("The number of lines per stanza will be ", len(rhyme_scheme))
print("Please enter the number of stanzas you'd like to generate: ")
stanza = int(input())
# identify types such as 'A', 'B', 'C', et cetera
types = list(set(i for i in rhyme_scheme))'''

def file_content(path):
    file = open(path, encoding="utf-8")
    content = json.load(file)
    file.close()
    return content

def read_text():
    with open("all_lyrics.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text

text = read_text()
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
encoded_text = tokenizer.encode(text, truncation=True, max_length=10)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# set model to training mode
model.train()

# convert encoded_text to PyTorch tensor
input_ids = torch.tensor(encoded_text).unsqueeze(0).to(device)

# set training hyperparameters
num_epochs = 5
learning_rate = 1e-5

# set optimizer and learning rate scheduler
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="min", factor=0.5, patience=2)

# fine-tune the model
for epoch in range(num_epochs):
    loss = 0
    model.zero_grad()
    output = model(input_ids, labels=input_ids)
    loss = output.loss
    loss.backward()
    optimizer.step()
    scheduler.step(loss)
    print("Epoch:", epoch, " Loss:", loss.item())



# set model to evaluation mode
model.eval()

# generate lyrics
prompt = "meri aankhon mein"
generated_text = ""
max_length = 100

# tokenize prompt and convert to PyTorch tensor
prompt_tokens = tokenizer.encode(prompt, add_special_tokens=False)
prompt_tensor = torch.tensor(prompt_tokens).unsqueeze(0).to(device)

# generate lyrics using the fine-tuned GPT-2 model
with torch.no_grad():
    output = model.generate(prompt_tensor, max_length=max_length)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)