import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave
import tempfile
import os
import base64
import json
import mysql.connector
from deep_translator import GoogleTranslator
from datetime import datetime
import hashlib

def generate_pdf_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

CHAT_HISTORY_DIR = "chat_history"
os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)

def get_user_sessions(username):
    sessions = []
    for file in os.listdir(CHAT_HISTORY_DIR):
        if file.startswith(f"{username}_session") and file.endswith(".json"):
            session_id = file.replace(f"{username}_session", "").replace(".json", "")
            sessions.append(int(session_id))
    return sorted(sessions)

def get_chat_history_path(username, pdf_filename):
    return os.path.join(CHAT_HISTORY_DIR, f"{username}_{pdf_filename}.json")

def save_chat_history(username, pdf_filename, chat_log):
    with open(get_chat_history_path(username, pdf_filename), "w") as file:
        json.dump(chat_log, file)

def load_chat_history(username, pdf_filename):
    path = get_chat_history_path(username, pdf_filename)
    if os.path.exists(path):
        with open(path, "r") as file:
            return json.load(file)
    return []

# Set page config
st.set_page_config(layout="wide")

# Configure Gemini AI
GENAI_API_KEY = "YOUR_API_KEY"
if not GENAI_API_KEY:
    st.error("API key is missing! Set the GENAI_API_KEY as an environment variable.")
    st.stop()

genai.configure(api_key=GENAI_API_KEY)



# MySQL configuration
MYSQL_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database_name'
}

def get_db_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)

def save_full_session_to_db(username, password, pdf_filename, chat_log):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        questions_answers = json.dumps(chat_log)

        query = """
            INSERT INTO chat_session (username, password, pdf_filename, start_time, questions_answers)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, pdf_filename, start_time, questions_answers))

        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        st.error(f"Database Error while saving session: {err}")
      
def save_chat_to_db(username, question, answer):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chats (username, question, answer) VALUES (%s, %s, %s)", (username, question, answer))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")

CREDENTIALS_FILE = "credentials.json"

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_credentials(username, password):
    credentials = load_credentials()
    credentials[username] = password
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file)


# PDF text extraction
def extract_text_from_pdf(file_bytes):
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + "\n\n"
    return text

# Preview single scrollable PDF view
def preview_pdf_scrollable(uploaded_file):
    base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# High Court file check
def is_valid_high_court_case(text):
    keywords = [
        "High Court of Karnataka",
        "Karnataka High Court",
        "IN THE HIGH COURT OF KARNATAKA",
        "IN THE HON'BLE HIGH COURT OF KARNATAKA",
        "Bengaluru Bench",
        "Dharwad Bench",
        "Kalaburagi Bench"
    ]
    return any(keyword.lower() in text.lower() for keyword in keywords)

# Chat with Gemini
def chat_with_ai(user_query, context=""):
    model = genai.GenerativeModel("gemini-1.5-flash")

    instruction = (
       "You are LegalEase AI, a highly trained legal assistant. "
        "You are only allowed to answer questions related to *Indian law, legal concepts, legal procedures, or court cases*. "
        "You must only answer questions that are directly related to the uploaded case document from the Karnataka High Court. "
        "If the question is not about this specific case or doesn't relate to the legal issues in the document, reply with:\n"
        "'❌ This question is outside the scope of the uploaded Karnataka High Court case file.'\n"
        "Do not provide general legal information. Do not answer anything about other courts, general law, or unrelated topics."
    )

    # Optional: show past interactions to maintain context
    past_qas = "\n".join([f"Q: {x['question']}\nA: {x['answer']}" for x in st.session_state.chat_log])

    prompt = f"{instruction}\n\nUploaded Case Context:\n{context}\n\nPrevious Q&A:\n{past_qas}\n\nNew Question: {user_query}\nAnswer:"

    response = model.generate_content(prompt)
    return response.text

# Audio recording
def record_audio_to_file():
    temp_audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    fs = 44100
    duration = 10
    st.info("🎙 Recording for 10 seconds... Speak now!")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    with wave.open(temp_audio_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())
    st.success("✅ Recording completed!")
    return temp_audio_path

lang_code_map = {
    "English": "en-US", "Hindi": "hi-IN", "Bengali": "bn-IN", "Telugu": "te-IN", "Marathi": "mr-IN",
    "Tamil": "ta-IN", "Urdu": "ur-IN", "Gujarati": "gu-IN", "Malayalam": "ml-IN",
    "Kannada": "kn-IN", "Odia": "or-IN", "Punjabi": "pa-IN", "Assamese": "as-IN",
    "Maithili": "hi-IN", "Santali": "hi-IN", "Kashmiri": "hi-IN", "Konkani": "hi-IN",
    "Sindhi": "hi-IN", "Nepali": "ne-NP", "Manipuri": "hi-IN", "Bodo": "hi-IN",
    "Dogri": "hi-IN", "Sanskrit": "hi-IN", "Tulu": "hi-IN"
}

def recognize_and_translate(audio_path, target_language):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=lang_code_map.get(target_language, "en-US"))
        return text
    except:
        return "Could not transcribe."

def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    USER_CREDENTIALS = load_credentials()

    if st.button("Login"):
        if USER_CREDENTIALS.get(username) == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.page = "main"
            st.session_state.sessions = get_user_sessions(username)
            st.session_state.chat_log = []
            st.rerun()
        else:
            st.error("❌ Incorrect username or password")

    if st.button("New User? Register"):
        st.session_state.show_login = False
        st.rerun()


def register():
    st.title("📝 Register")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if username in load_credentials():
            st.error("Username already exists.")
        elif password != confirm:
            st.error("Passwords do not match.")
        else:
            save_credentials(username, password)
            st.success("Registration successful. Please login.")
            st.session_state.show_login = True
            st.rerun()
            
def summarize_document(prompt, document_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{prompt}\n\n{document_text}")
    return response.text
    
def summary_page():
    st.title("📄 LegalEase AI")
    left, right = st.columns([1, 2])

    with left:
        uploaded_file = st.file_uploader("📂 Upload a PDF File", type="pdf")
        if uploaded_file:
            st.write("### PDF Preview")
            preview_pdf_scrollable(uploaded_file)
            st.session_state.uploaded_file = uploaded_file
            st.session_state.pdf_filename = uploaded_file.name

    with right:
        uploaded_file = st.session_state.get("uploaded_file")
        if uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            st.session_state.pdf_filename = uploaded_file.name 
            uploaded_file.seek(0)
            file_bytes = uploaded_file.read()
            st.session_state.pdf_filename = uploaded_file.name  # ✅ Store filename
            st.session_state.text = extract_text_from_pdf(file_bytes)
            st.session_state.active_pdf_text = st.session_state.text
            st.session_state.active_pdf_name = st.session_state.pdf_filename
            
            if not is_valid_high_court_case(st.session_state.text):  # ✅ Use session text
                st.error("❌ Not a valid Karnataka High Court document.")
                return
            
            st.write("### Summary")
            summary = summarize_document("Summarize this Karnataka High Court legal document clearly and briefly.", st.session_state.text)
            st.write(summary)
            
            st.write("### Key Insights")
            insights = summarize_document("Provide key legal insights and findings from this Karnataka High Court judgment.", st.session_state.text)
            st.write(insights)


            translate_target = st.selectbox("Translate Summary & Key Insights To", list(lang_code_map.keys()))
            if st.button("Translate"):
                lang_code = lang_code_map.get(translate_target, 'en')[:2]
                translated_summary = GoogleTranslator(source='auto', target=lang_code).translate(summary)
                translated_insights = GoogleTranslator(source='auto', target=lang_code).translate(insights)
                st.write("#### Translated Summary")
                st.write(translated_summary)
                st.write("#### Translated Key Insights")
                st.write(translated_insights)


            if st.button("➡ Q&A ChatBot"):
                # Reset state for the new PDF session
                st.session_state.page = "chat"
                st.session_state.messages = []
                st.session_state.chat_log = []
                st.rerun()

            if "current_question" not in st.session_state:
                st.session_state.current_question = ""
            if "current_response" not in st.session_state:
                st.session_state.current_response = ""
                
def get_next_session_index(username, chat_history_dir="chat_history"):
    existing_files = [
        f for f in os.listdir(chat_history_dir)
        if f.startswith(f"{username}_session") and f.endswith(".json")
    ]
    indices = [
        int(f.split("_session")[1].split(".json")[0])
        for f in existing_files if "_session" in f
    ]
    return max(indices, default=0) + 1

def chat_page():
    st.title("LegalEase AI Q&A")

    with st.sidebar:
        st.title("Menu")
        if st.button("Back to Summary Page"):
            st.session_state.page = "main"
            st.rerun()
        if st.button("Exit"):
            # Clear all session-related variables on logout
            keys_to_clear = [
                "logged_in", "uploaded_file", "pdf_filename", "text",
                "active_pdf_text", "active_pdf_name", "chat_log",
                "chat_log", "messages", "current_question", "current_response",
                "sessions"
            ]
            for key in keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]
            
            st.session_state.show_login = True
            st.session_state.page = "main"
            st.success("Logged out successfully.")
            st.rerun()
        

        if "chat_log" not in st.session_state:
            st.session_state.chat_log = []
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # ✅ Step 1: Make sure PDF was uploaded from Summary Page
        if "active_pdf_name" not in st.session_state or not st.session_state.get("active_pdf_name"):
            st.warning("Please upload a PDF from the Summary page to start a new session.")
            return
        
        # ✅ Step 2: Load previous sessions if available
        existing_sessions = [
            f.replace(f"{st.session_state.username}_", "").replace(".json", "")
            for f in os.listdir(CHAT_HISTORY_DIR)
            if f.startswith(f"{st.session_state.username}_") and f.endswith(".json")
        ]
        
        # ✅ Step 3: If no previous sessions, add the current one so the dropdown still works
        if st.session_state.active_pdf_name not in existing_sessions:
            existing_sessions.append(st.session_state.active_pdf_name)


        selected_pdf = st.sidebar.selectbox("Choose PDF Session", sorted(existing_sessions))

        if selected_pdf:
            st.session_state.pdf_filename = selected_pdf
        
            # ✅ Block to ensure only active PDF can be used for Q&A
            pdf_filename = st.session_state.get("pdf_filename")
            
            if not pdf_filename:
                st.warning("No PDF selected. Please upload a PDF from the Summary page.")
                return
        
            if pdf_filename != st.session_state.get("active_pdf_name"):
                st.warning("⚠ The selected PDF is not the one currently uploaded in the Summary Page. Please go back and re-upload it.")
                return
        
            # ✅ Load history & messages only if active PDF matches
            st.session_state.chat_log = load_chat_history(st.session_state.username, selected_pdf)
        
            st.session_state.messages = []
            for item in st.session_state.chat_log:
                question_text = item["question"].split(" (")[0]
                st.session_state.messages.append({"role": "user", "content": question_text})
                st.session_state.messages.append({"role": "assistant", "content": item["answer"]})


    # Remove this redundant line if already loading based on selected_pdf
    # But if you want to reload using current filename separately, then keep it
    st.session_state.chat_log = load_chat_history(st.session_state.username, st.session_state.pdf_filename)

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.markdown("### 💬 Ask Your Question")

        selected_lang = st.selectbox("Select Language", list(lang_code_map.keys()), key="multi_lang")
        target_lang_code = lang_code_map.get(selected_lang, "en-US")[:2]

        if "messages" not in st.session_state:
            st.session_state.messages = []

        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        user_query = ""

        # 🎙 Voice Input
        if st.button("🎙 Record Voice"):
            audio_path = record_audio_to_file()
            user_query = recognize_and_translate(audio_path, selected_lang)

        # Text input fallback
        typed_input = st.chat_input("💬 Ask a question about the PDF:")
        if typed_input:
            user_query = typed_input

        if user_query:
            st.session_state.current_question = user_query
            st.session_state.messages.append({"role": "user", "content": user_query})
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(user_query)

            context = st.session_state.get("text", "")
            ai_response = chat_with_ai(user_query, context)
            translated_response = GoogleTranslator(source='auto', target=target_lang_code).translate(ai_response)
            st.session_state.current_response = translated_response

            st.session_state.messages.append({"role": "assistant", "content": translated_response})
            st.session_state.chat_log.append({
                "question": f"{user_query} ({selected_lang})",
                "answer": translated_response
            })

            with chat_container:
                with st.chat_message("assistant"):
                    st.markdown(translated_response)

        save_full_session_to_db(
            st.session_state.username,
            st.session_state.password,
            st.session_state.pdf_filename,  # use PDF filename as session_id for clarity
            st.session_state.chat_log
        )
    save_chat_history(
        st.session_state.username,
        st.session_state.pdf_filename,
        st.session_state.chat_log
    )

    with right_col:
        st.markdown("### Session Chat History")
        if st.session_state.chat_log:
            with st.expander("🗨 Chat History", expanded=True):
                for entry in st.session_state.chat_log:
                    st.markdown(f"*You:* {entry['question']}")
                    st.markdown(f"*AI:* {entry['answer']}")



    save_chat_history(st.session_state.username, st.session_state.pdf_filename, st.session_state.chat_log)



# App Controller
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_login" not in st.session_state:
    st.session_state.show_login = True
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.logged_in:
    if st.session_state.page == "main":
        summary_page()
    elif st.session_state.page == "chat":
        chat_page()
elif st.session_state.show_login:
    login()
else:
    register()