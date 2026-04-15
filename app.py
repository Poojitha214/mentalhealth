import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# --- NEW: Import the style from your separate file ---
from styles import get_css

st.set_page_config(page_title=" MENTAL HEALTH DETECTION", page_icon="🧠")

# --- APPLY THE CSS ---
st.markdown(get_css(), unsafe_allow_html=True)

# ... (rest of your model training and UI code continues here)

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MENTAL HEALTH DETECTION 🌈", page_icon="🧠", layout="centered")

# --- 2. THE AI BRAIN (Training) ---
@st.cache_resource
def train_ai_model():
    try:
        # Load your dataset (Make sure columns are 'text' and 'sentiment')
        df = pd.read_csv('sentiment_dataset.csv')
        model = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english')),
            ('classifier', LogisticRegression(max_iter=1000))
        ])
        model.fit(df['text'], df['sentiment'])
        return model
    except:
        return None

# Load model
model = train_ai_model()

# --- 3. FRONTEND UI (The Webpage) ---
st.title("🌈 MindCare: Mental Health Status Detector 🌿")
st.markdown("### Share your thoughts below, and our AI will listen. ✨")

# Sidebar with info
st.sidebar.header("Project Info ℹ️")
st.sidebar.write("This app uses NLP 🤖 to detect emotional patterns in your text.")

# Input Area
user_text = st.text_area("How are you feeling today? 💭", placeholder="Type here...", height=150)

# Prediction Button
if st.button("Analyze My Sentiment 🔍"):
    if user_text.strip() != "":
        # Perform Prediction
        prediction = model.predict([user_text])[0]
        
        # Calculate Confidence
        probs = model.predict_proba([user_text])[0]
        confidence = np.max(probs) * 100
        
        st.divider()
        
        # --- 4. EMOJI LOGIC BASED ON RESULT ---
        status = prediction.lower()
        
        if any(word in status for word in ['depress', 'anxiety', 'sad', 'negative']):
            st.subheader(f"Analysis Result: {prediction} 😔")
            st.error(f"Confidence: {confidence:.2f}% 📉")
            st.warning("It looks like you're going through a tough time. Please reach out to a loved one or a professional. You are not alone! ❤️🤝")
            
        elif 'stress' in status:
            st.subheader(f"Analysis Result: {prediction} 😫")
            st.error(f"Confidence: {confidence:.2f}% 📊")
            st.info("You seem quite stressed. Remember to take deep breaths and rest. 🧘‍♂️☕")
            
        elif 'neutral' in status:
            st.subheader(f"Analysis Result: {prediction} 😐")
            st.info(f"Confidence: {confidence:.2f}% ⚖️")
            st.write("Your sentiment seems balanced. Keep observing your thoughts! ☁️")
            
        else: # Positive / Happy
            st.subheader(f"Analysis Result: {prediction} 🌟")
            st.success(f"Confidence: {confidence:.2f}% 📈")
            st.balloons() # Celebtation effect!
            st.write("You are in a great headspace! Keep spreading the positivity! ☀️✨")

    else:
        st.error("Oops! Please type something first so I can analyze it! ✍️")

st.markdown("---")
st.caption("Built with ❤️ for Mental Health Awareness.")