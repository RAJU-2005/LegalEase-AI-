# LegalEase-AI-
LegalEase AI is a smart legal assistant that helps lawyers analyze Karnataka High Court case files. It summarizes documents, answers case-related questions, and supports multilingual processing.

## Features
- **✅Legal Document Summarization** – Automatically extracts key insights from lengthy case files, making legal research faster and more efficient.
- **📄 Uploaded PDF File Preview** – Users can upload legal case files in PDF format and preview them directly within the application for quick reference and review.
- **💬Interactive Q&A** – Allows users to ask legal queries and get instant, AI-driven responses based on case law and legal documents.
- **🌍 Language Support** – Supports multiple Indian languages, enabling seamless understanding and translation of legal texts for diverse users.
- **🔒Secured Database Storage** – Ensures case data is stored safely using encryption and authentication protocols, maintaining confidentiality and integrity.

###Tech Stack

### **Frontend & UI**
- **Streamlit** (`streamlit`) → For creating the web-based UI

### **AI & NLP**
- **Google Gemini AI** (`google-generativeai`) → For answering legal queries
- **SpeechRecognition** (`speech_recognition`) → For converting audio to text
- **Deep Translator** (`deep_translator`) → For language translation

### **PDF Processing**
- **PyMuPDF** (`fitz`) → For extracting text from PDF case files
- **Base64 Encoding** (`base64`) → For embedding PDF previews in the UI

### **Audio Processing**
- **Sounddevice** (`sounddevice`) → For recording audio
- **Wave** (`wave`) → For handling `.wav` audio files
- **NumPy** (`numpy`) → For audio data processing

### **Database & Storage**
- **MySQL** (`mysql.connector`) → For storing user chat logs and sessions
- **JSON** (`json`) → For saving credentials and chat history in local files

### **Security & Authentication**
- **Hashlib** (`hashlib`) → For hashing PDF files
- **Tempfile** (`tempfile`) → For handling temporary audio file storage

### **Other Utilities**
- **Datetime** (`datetime`) → For logging timestamps
- **OS** (`os`) → For file operations and directory management
