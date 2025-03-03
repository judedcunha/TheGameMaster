
# **Dungeons & Dragons Game Master LLM**

This project is a **Large Language Model (LLM)** fine-tuned to act as a **Game Master (GM)** for the tabletop role-playing game **Dungeons & Dragons (D&D)**. The LLM can generate dynamic narratives, enforce game rules, and interact with players in real-time.

The application consists of:
1. An LLM model trainer 
2. A **FastAPI backend** that serves the fine-tuned LLM.
3. A **simple web interface** for players to interact with the GM.

---

## **Features**
- **Dynamic Storytelling**: Generate immersive narratives, NPCs, and quests.
- **Rule Enforcement**: Understand and apply D&D rules (e.g., combat, skill checks).
- **Player Interaction**: Respond dynamically to player actions and decisions.
- **Web Interface**: A simple interface for players to interact with the GM.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher
- GPU (recommended for faster inference)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

Install the required libraries:
```bash
pip install fastapi uvicorn transformers
pip install transformers datasets torch
pip install transformers[torch]
```

---

### **2. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/judedcunha/TheGameMaster
cd TheGameMaster
```

---

### **3. Fine-Tune the Model**
If you haven’t already fine-tuned the model, follow these steps:

1. **Preprocess the Data**:
   - Place your D&D rulebooks, adventure modules, and other data in the main directory.
   - Run the preprocessing script:
     ```bash
     python preprocess.py
     ```

2. **Fine-Tune the Model**:
   - Fine-tune the model using the preprocessed data:
     ```bash
     python main.py
     ```
   - The fine-tuned model will be saved in the `dnd_gm_model/` directory.

---

### **4. Run the Backend**
Start the FastAPI backend:
```bash
python app.py
```

The backend will start at `http://127.0.0.1:8000`.

---

### **5. Run the Frontend**
Serve the frontend using a simple HTTP server:
```bash
python -m http.server 8080
```

The frontend will be available at `http://127.0.0.1:8080`.

---

### **6. Interact with the GM**
1. Open your browser and navigate to `http://127.0.0.1:8080`.
2. Enter a prompt in the text area (e.g., "The players enter a dark forest. What happens next?") and click **Ask the GM**.
3. The response from the GM will be displayed below.

---

## **Project Structure**
```
TheGameMaster/
├── app.py                  # FastAPI backend
├── main.py                 # Script to fine-tune the model
├── preprocess.py           # Script to preprocess the data
├── dnd_gm_model/           # Fine-tuned model and tokenizer
├── index.html              # Frontend interface
└── README.md               # Project documentation
```

---

## **Deployment**
To deploy the application:
1. **Local Network**: Share your local IP address to allow others to access the application.
2. **Cloud Platforms**: Deploy the backend and frontend on platforms like **Heroku**, **AWS**, or **Google Cloud**.
3. **Docker**: Containerize the application for easy deployment.

---

## **Contributing**
Contributions are welcome! If you’d like to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

---


## **Acknowledgments**
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the LLM framework.
- [FastAPI](https://fastapi.tiangolo.com/) for the backend.
- [Dungeons & Dragons](https://www.dndbeyond.com/) to lean about DND.

---

## **Contact**
For questions or feedback, please contact Jude at [judedcunha3117@gmail.com].

---

