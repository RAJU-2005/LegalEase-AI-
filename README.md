# 🏛️ LegalEase-AI-
LegalEase AI is a smart legal assistant that helps lawyers analyze Karnataka High Court case files. It summarizes documents, answers case-related questions, and supports multilingual processing.

## Features
- **✅Legal Document Summarization** – Automatically extracts key insights from lengthy case files, making legal research faster and more efficient.
- **📄 Uploaded PDF File Preview** – Users can upload legal case files in PDF format and preview them directly within the application for quick reference and review.
- **💬Interactive Q&A** – Allows users to ask legal queries and get instant, AI-driven responses based on case law and legal documents.
- **🌍 Language Support** – Supports multiple Indian languages, enabling seamless understanding and translation of legal texts for diverse users.
- **🔒Secured Database Storage** – Ensures case data is stored safely using encryption and authentication protocols, maintaining confidentiality and integrity.
- **🎙️ Audio Recording in Q&A Interaction** – Enables users to record and submit voice queries, making it easier to interact with the system hands-free. The AI converts speech to text and processes the query.

# **Tech Stacks**

### **1. Frontend & UI**
- **Streamlit** (`streamlit`) → For creating the web-based UI

### **2. AI & NLP**
- **Google Gemini AI** (`google-generativeai`) → For answering legal queries
- **SpeechRecognition** (`speech_recognition`) → For converting audio to text
- **Deep Translator** (`deep_translator`) → For language translation

### **3. PDF Processing**
- **PyMuPDF** (`fitz`) → For extracting text from PDF case files
- **Base64 Encoding** (`base64`) → For embedding PDF previews in the UI

### **4. Audio Processing**
- **Sounddevice** (`sounddevice`) → For recording audio
- **Wave** (`wave`) → For handling `.wav` audio files
- **NumPy** (`numpy`) → For audio data processing

### **5. Database & Storage**
- **MySQL** (`mysql.connector`) → For storing user chat logs and sessions
- **JSON** (`json`) → For saving credentials and chat history in local files

### **6. Security & Authentication**
- **Hashlib** (`hashlib`) → For hashing PDF files
- **Tempfile** (`tempfile`) → For handling temporary audio file storage

### **7. Other Utilities**
- **Datetime** (`datetime`) → For logging timestamps
- **OS** (`os`) → For file operations and directory management

# 📦 Packages Required  

### **Frontend & UI**
```bash
   pip install streamlit


### ** AI & NLP**
```bash
   pip install google-generativeai speechrecognition deep-translator

### ** PDF Processing **
```bash
pip install pymupdf

### ** Audio Processing**
```bash
pip install sounddevice wave numpy

### ** Database & Storage **
```bash
pip install mysql-connector-python



