from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import Dataset
import PyPDF2
import re
import json


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text


def clean_text(text):
    text = re.sub(r'\n+', ' ', text)  # Remove extra newlines
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    return text

structured_data = {
    "rule": "Combat",
    "description": "During combat, players take turns to attack...",
    "example": "Player rolls a d20 to hit the goblin."
}

with open("combat_rule.json", "w") as f:
    json.dump(structured_data, f)

rulebook_text = extract_text_from_pdf("rulebook.pdf")
cleaned_text = clean_text(rulebook_text)


model_name = "openai-community/gpt2"  # or "meta-llama/Llama-2-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)  # or "meta-llama/Llama-2-7b"

text = "The players enter a dark forest. What happens next?"
inputs = tokenizer(text, return_tensors="pt")

print(inputs)

data = [
    {"input": "The players enter a dark forest. What happens next?", "output": "As you step into the forest, the air grows cold..."},
    {"input": "The rogue tries to pick the lock.", "output": "The rogue carefully inserts the lockpick and feels the tumblers click into place."}
]

dataset = Dataset.from_dict({"input": [d["input"] for d in data], "output": [d["output"] for d in data]})
print(dataset)

dataset.save_to_disk("dnd_dataset")