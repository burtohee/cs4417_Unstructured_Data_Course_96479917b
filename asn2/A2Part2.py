import torch
from transformers import AutoTokenizer, GPT2LMHeadModel

def generate_story():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    # add the EOS token as PAD token to avoid warnings
    model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

    torch.manual_seed(0)
    input_text = "Winter is coming,"
    model_inputs = tokenizer(input_text, return_tensors='pt')

    sample_outputs = model.generate(
        **model_inputs,
        max_new_tokens=100,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1
    )

    # Decode and print the generated text
    generated_text = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)
    return generated_text


print("My GPT-2 Story:")

story = generate_story()

print(story)

with open("A2Part2.txt", "w") as file:
        file.write(story)

print("---------------")