from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_from_disk

# Load the preprocessed dataset
dataset = load_from_disk("dnd_dataset")

# Load the tokenizer and model
model_name = "openai-community/gpt2"  # or "meta-llama/Llama-2-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Add a custom padding token
tokenizer.add_special_tokens({"pad_token": "[PAD]"})
model.resize_token_embeddings(len(tokenizer))

# Tokenize the dataset
def tokenize_function(examples):
    # Tokenize the input text
    tokenized_input = tokenizer(
        examples["input"],
        padding="max_length",
        truncation=True,
        max_length=512,  # Adjust as needed
    )

    # For causal language modeling, labels are the same as input_ids
    tokenized_input["labels"] = tokenized_input["input_ids"].copy()
    return tokenized_input


# Apply the tokenization function to the dataset
tokenized_dataset = dataset.map(tokenize_function, batched=True)



# Split the dataset
split_dataset = tokenized_dataset.train_test_split(test_size=0.1)
train_dataset = split_dataset["train"]
eval_dataset = split_dataset["test"]


print(train_dataset[0])

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./dnd_gm_model",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    save_total_limit=2,
    fp16=True,
)

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./dnd_gm_model")
tokenizer.save_pretrained("./dnd_gm_model")

# Test the model
def generate_response(prompt, model, tokenizer, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

prompt = "The players enter a dark forest. What happens next?"
response = generate_response(prompt, model, tokenizer)
print(f"GM: {response}")


eval_results = trainer.evaluate()
print(f"Evaluation results: {eval_results}")