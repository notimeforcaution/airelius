from transformers import GPT2Tokenizer, GPT2LMHeadModel

def main():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    with open("medications.txt", "r") as f:
        text = f.read()

    # TODO(ntfc): Replicate the changes in notebook to over here, as much as possible.

def __main__():
    main()
