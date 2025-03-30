# **🏛️ LegalEase-AI**
   The legal world depends heavily on written case files, judgments, petitions, and other documents. In courts like the Karnataka High Court, these files can stretch to dozens of pages filled with legal jargon, technical terms, and procedural language.For advocates, especially juniors or interns, reading and understanding these documents is not only time-consuming but also mentally exhausting. Every case requires careful reading, summarizing, noting key insights, and preparing responses—repeating this for multiple files daily becomes a major challenge.LegalEase AI was built to make this process smarter. It’s not just a chatbot—it’s a digital assistant for lawyers that helps them read, understand, and engage with Karnataka High Court case files in a faster, simpler, and more interactive way.

# **⚡Features**
- **Legal Document Summarization** – Automatically extracts key insights from lengthy case files, making legal research faster and more efficient.
- **Uploaded PDF File Preview** – Users can upload legal case files in PDF format and preview them directly within the application for quick reference and review.
- **Interactive Q&A** – Allows users to ask legal queries and get instant, AI-driven responses based on case law and legal documents.
- **Language Support** – Supports multiple Indian languages, enabling seamless understanding and translation of legal texts for diverse users.
- **Secured Database Storage** – Ensures case data is stored safely using encryption and authentication protocols, maintaining confidentiality and integrity.
- **Audio Recording in Q&A Interaction** – Enables users to record and submit voice queries, making it easier to interact with the system hands-free. The AI converts speech to text and processes the query.

# **🖥️Tech Stacks**

### **1. Frontend & UI**
- **Streamlit** (`streamlit`) → For creating the web-based UI

### **2. AI & NLP**
- **Google Gemini AI** (`google-generativeai`) → For answering legal queriesk
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

# 📸 Snapshots  

Here are some screenshots of the AI bot in action:  

### **1. Register Page**  
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Register%20Page.jpg )

### **2. Login Page**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Login%20Page.jpg )

### **3. Summary Page**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Summary%20Page.jpg )

### **4. File Upload**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/PDF%20Upload%20Page.jpg)

### **5. PDF Preview**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/PDF%20Preview.jpg)

### **6. Summary Translation (Hindi)**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Multilingual%20Summary%20Translation.jpg)

### **7. Q&A ChatBot Page**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Q%26A%20Page.jpg)

### **8. Menu Sidebar**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Sidebar%20Menu.jpg)

### **9. ChatBot Interface**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Chatbot%20Interface.jpg)

### **10. Regional Language Translation**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/Transalating%20Feature.jpg)


### **12. SQL Database Logs**
![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/44277fcde1856c411206e876109d9031a0033acd/Snapshots/SQL%20Database%20Logs.jpg)

# **📝System Architecture**
The image below provides a clear overview of how LegalEaseAI works and its feature flows. The system architecture is structured into different layers, each performing a critical role in ensuring seamless functionality. These layers work together to handle document processing, AI-based text summarization, question-answering, and multilingual support while maintaining an intuitive and user-friendly experience.

![image.alt](https://github.com/RAJU-2005/LegalEase-AI-/blob/c9e3b467b16d9cda23c66656498309c7572e5248/System_Architecture.png)

## 🎬Demo Video  

Here is the Demo Video of the AI bot in action: 
![video.alt]()

# **✅Who Benefits from This Project?**

**Some of the Key Beneficiaries of LegalEase AI are :**  

- **Advocates & Legal Professionals :** Quickly analyze Karnataka High Court case files, extract key insights, and save time.  
- **Law Students & Interns :** Simplifies complex legal documents for better understanding.  
- **Legal Firms :** Streamlines documentation and client preparation.  
- **Citizens Seeking Legal Help :** Provides easy-to-understand summaries in multiple languages.

# **📈Future Enhancement**

- **Timeline Visualization :** Add interactive case timelines with filters.
- **Speech-to-Speech Interaction :** Enable voice-based responses for a fully conversational experience.
- **Enhanced Security :** Introduce role-based access, two-factor authentication, and encryption.
- **Legal Database Integration :** Automate case extraction from SCC Online, Indian Kanoon, etc.
- **Cross-Jurisdiction Support :** Expand coverage to other Indian courts.
- **Mobile App Version :** Develop an Android/iOS app for legal access on the go.
- **Past Case Matching Engine :** Implement semantic search to fetch similar Karnataka High Court cases.


# **🔎Conclusion**
   LegalEase AI is a practical solution designed to address a major gap in the legal domain—simplifying the process of understanding, summarizing, and interacting with complex legal case files. By integrating cutting-edge LLMs, speech recognition, multilingual translation, and a user-friendly interface, the tool makes legal research more accessible, inclusive, and time-efficient. The project has proven that a combination of AI and thoughtful design can significantly assist legal professionals and common users. From uploading a case file to receiving intelligent answers and summaries in their preferred language, users experience an innovative legal assistant built for the Indian context. This project also helped us learn not just about technical implementation but also about the real-world challenges of building inclusive and practical AI tools. LegalEase AI is a step toward democratizing legal knowledge and making justice a little easier to understand and access.

# **📚References & Citations**
- **OpenAI ChatGPT :** Used to assist with code structure, explanation writing, formatting, and overall guidance during the project.
- **Karnataka High Court Judgments :** [Source of legal case PDFs](https://karnatakajudiciary.kar.nic.in/hck_judgments.php#)












