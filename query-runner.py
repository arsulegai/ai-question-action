import sys
from transformers import GPTJForCausalLM, GPT2Tokenizer

# Load model and tokenizer
model_name = 'EleutherAI/gpt-j-6B'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTJForCausalLM.from_pretrained(model_name)

def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    # Read the prompt from command-line arguments
    prompt = sys.argv[1] if len(sys.argv) > 1 else "No prompt provided"
    print(generate_text(prompt))
