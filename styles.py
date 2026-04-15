# styles.py

def get_css():
    return """
    <style>
    /* Main background with a calming gradient */
    .stApp {
        background: linear-gradient(to bottom right, #e0f2f1, #ffffff);
    }

    /* Styling the main title */
    h1 {
        color: #00796b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        text-shadow: 1px 1px 2px #cfd8dc;
    }

    /* Modernizing the Text Input Area */
    .stTextArea textarea {
        border-radius: 20px !important;
        border: 2px solid #80cbc4 !important;
        background-color: #ffffff !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05) !important;
    }

    /* Highlighting the Analysis Button */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #00bfa5, #00796b);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 121, 107, 0.3);
    }

    /* Button hover animation */
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 121, 107, 0.4);
        color: #ffffff;
    }

    /* Customizing the Progress/Confidence Bar */
    .stProgress > div > div > div > div {
        background-color: #00bfa5;
    }

    /* Styling the Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f1f8f7;
    }
    </style>
    """