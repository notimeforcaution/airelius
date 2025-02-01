from transformers import GPT2Tokenizer, GPT2LMHeadModel

def main():
    # Initializers.
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Token
    with open("medications.txt", "r") as f:
        text = f.read()
    
    inputs = tokenizer(text)

    print(inputs)




def __main__():
    main()