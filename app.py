from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the fine-tuned model and tokenizer
model_path = "./dnd_gm_model"  # Path to your fine-tuned model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Define the input schema for the API
class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 100  # Default max length for response

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  # Allow requests from your frontend
    allow_credentials=True,
    allow_methods=["POST"],  # Allow only POST requests
    allow_headers=["*"],  # Allow all headers
)

# Define the API endpoint
@app.post("/generate")
async def generate_response(request: PromptRequest):
    try:
        # Tokenize the input prompt
        inputs = tokenizer(request.prompt, return_tensors="pt")

        # Generate response
        outputs = model.generate(
            inputs.input_ids,
            max_length=request.max_length,
            pad_token_id=tokenizer.eos_token_id,  # Use EOS token as padding token
        )

        # Decode the generated tokens to text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)