from transformers import AutoModelForCausalLM, AutoTokenizer
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

rulebook_text = extract_text_from_pdf("rulebook.pdf")


model_name = "gpt-4"  # or "meta-llama/Llama-2-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

inputs = tokenizer("The Game master starts the game", return_tensors="pt")

