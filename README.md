# 🏛️ LegalEase-AI-
LegalEase AI is a smart legal assistant that helps lawyers analyze Karnataka High Court case files. It summarizes documents, answers case-related questions, and supports multilingual processing.

## ⚡Features
- **✅Legal Document Summarization** – Automatically extracts key insights from lengthy case files, making legal research faster and more efficient.
- **📄 Uploaded PDF File Preview** – Users can upload legal case files in PDF format and preview them directly within the application for quick reference and review.
- **💬Interactive Q&A** – Allows users to ask legal queries and get instant, AI-driven responses based on case law and legal documents.
- **🌍 Language Support** – Supports multiple Indian languages, enabling seamless understanding and translation of legal texts for diverse users.
- **🔒Secured Database Storage** – Ensures case data is stored safely using encryption and authentication protocols, maintaining confidentiality and integrity.
- **🎙️ Audio Recording in Q&A Interaction** – Enables users to record and submit voice queries, making it easier to interact with the system hands-free. The AI converts speech to text and processes the query.

# **🖥️Tech Stacks**

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

# **📦 Packages Required** 

   ### **1. Frontend & UI**
   ```bash
      pip install streamlit
   ```
   
   
   ### **2. AI & NLP**
   ```bash
      pip install google-generativeai speechrecognition deep-translator
   ```
   
   ### **3. PDF Processing**
   ```bash
      pip install pymupdf
   ```
   
   ### **4. Audio Processing**
   ```bash
      pip install sounddevice wave numpy
   ```
   
   ### **5. Database & Storage**
   ```bash
      pip install mysql-connector-python
   ```

# **🎯 Steps to Use the AI Bot**

### **1. Create a Jupyter Notebook File**
- Open Jupyter Notebook and create a new file.
- Save it as (`project_name.py`).

### **2. Copy & Paste the Code**
- Copy the provided Python script and paste it into (`project_name.py`).

### **3. Add Your Gemini API Key**
- Locate line 49 in the code and replace the placeholder with your API key.

### **4. Configure Database Credentials**
- Find lines 60-63 and update the username and SQL password.

### **5. Save the File**
- Press (`Ctrl + S`) to save your work.

### **6. Open Anaconda Prompt**
- Launch Anaconda Prompt on your system.

 ### **7. Run the Streamlit App**
 - Run this command in Anaconda Prompt:
   ```bash
      streamlit run project_name.py
   ```

### **8. View the Output**
- The app will launch in your browser, and you can start using it!

## 📸 Snapshots  

Here are some screenshots of the AI bot in action:  

### **1️⃣ Home Page**  
![image.alt]()

# **📝System Architecture**
The image below provides a clear overview of how LegalEaseAI works and its feature flows. The system architecture is structured into different layers, each performing a critical role in ensuring seamless functionality. These layers work together to handle document processing, AI-based text summarization, question-answering, and multilingual support while maintaining an intuitive and user-friendly experience.

![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/c9e3b467b16d9cda23c66656498309c7572e5248/System_Architecture.png)

## 🎬Demo Video  

Here is the Demo Video of the AI bot in action: 
![video.alt]()

## 📈Future Enhancement

- **Past Case Matching Engine** : Implement semantic search to fetch similar Karnataka High Court cases.
- **Timeline Visualization** : Add interactive case timelines with filters.
- **Speech-to-Speech Interaction** : Enable voice-based responses for a fully conversational experience.
- **Enhanced Security** : Introduce role-based access, two-factor authentication, and encryption.
- **Legal Database Integration** : Automate case extraction from SCC Online, Indian Kanoon, etc.
- **Cross-Jurisdiction Support** : Expand coverage to other Indian courts.
- **Mobile App Version** : Develop an Android/iOS app for legal access on the go.









