import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# Page configuration
st.set_page_config(
    page_title="💌 Love Messages for Jeru 💌",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 50%, #E6E6FA 100%);
    }
    
    .title-container {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(45deg, #FFE4E1, #FFF0F5);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(255, 105, 180, 0.3);
        border: 3px solid #FF69B4;
    }
    
    .love-message {
        background: linear-gradient(135deg, #FFE4E1, #FFF);
        padding: 2rem;
        border-radius: 15px;
        border-left: 8px solid #FF69B4;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        margin: 2rem 0;
        animation: fadeIn 0.8s ease-in;
    }
    
    .heart-decoration {
        color: #FF69B4;
        font-size: 2rem;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #FF69B4, #FF1493);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(255, 105, 180, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(255, 105, 180, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Love messages collection
love_messages = [
    "My dearest Jeru, you are the sunshine that brightens my every day. Your smile melts my heart and your laugh is my favorite melody. I am so grateful to have you in my life! 💖",
    "Jeru, you are absolutely amazing! Every moment with you feels like magic. You make ordinary days extraordinary just by being you. I love your kindness, your humor, and the way you make everything better! ✨",
    "Sweet Jeru, you are my heart's greatest treasure. Your love fills my world with color and joy. Thank you for being the most wonderful girlfriend anyone could ask for! 🌹",
    "Beautiful Jeru, you are my favorite person in the whole world. Your gentle spirit and loving heart make me fall in love with you more each day. You are truly special! 💕",
    "My lovely Jeru, you bring so much happiness into my life. Your hugs feel like home, and your love gives me strength. I am blessed to call you mine! 🥰",
    "Darling Jeru, you are incredibly special to me. Your intelligence, beauty, and caring nature never cease to amaze me. I love you more than words can express! 💝",
    "Jeru, my love, you light up my world like no one else can. Every day with you is a new adventure filled with laughter and joy. You are my everything! 🌟",
    "Sweet angel Jeru, your presence in my life is the greatest gift I could ever ask for. You make me want to be the best version of myself! 👑",
    "My beautiful Jeru, every day I wake up grateful for your love. You fill my world with laughter, warmth, and endless happiness. You are my perfect match! 💞",
    "Dearest Jeru, you are not just my girlfriend, you are my best friend, my inspiration, and my greatest love. Thank you for being you! 🌺"
]

# Function to generate word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="Reds",
        max_words=100,
        relative_scaling=0.5,
        min_font_size=12
    ).generate(text)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("💕 Words of Love for Jeru 💕", fontsize=20, color='#FF69B4', pad=20, weight='bold')
    plt.tight_layout()
    
    return fig

# Initialize session state
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'current_message' not in st.session_state:
    st.session_state.current_message = random.choice(love_messages)

# Main title with hearts decoration
st.markdown("""
<div class="title-container">
    <div class="heart-decoration">💕 💖 💕</div>
    <h1 style="color: #FF69B4; font-family: 'Comic Sans MS', cursive; font-size: 3rem; margin: 1rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">
        💌 From Me to You 💌
    </h1>
    <h2 style="color: #FF1493; font-family: Arial, sans-serif; margin-bottom: 1rem;">
        Special Love Messages for Jeru
    </h2>
    <p style="color: #8B008B; font-size: 1.3rem; font-style: italic;">
        ✨ Surprise! Your personal love messages are here ✨
    </p>
    <div class="heart-decoration">💕 💖 💕</div>
</div>
""", unsafe_allow_html=True)

# Display current love message
st.markdown(f"""
<div class="love-message">
    <h3 style="color: #FF69B4; margin-bottom: 1rem; font-family: Arial, sans-serif; text-align: center;">
        💖 Your Love Message #{st.session_state.message_count + 1} 💖
    </h3>
    <p style="color: #4B0082; font-size: 1.2rem; font-style: italic; line-height: 1.8; text-align: center; margin: 0;">
        {st.session_state.current_message}
    </p>
</div>
""", unsafe_allow_html=True)

# Create and display word cloud
st.markdown('<h3 style="color: #FF69B4; text-align: center; margin: 2rem 0;">💖 Word Cloud of Love 💖</h3>', unsafe_allow_html=True)

fig = create_wordcloud(st.session_state.current_message)
st.pyplot(fig)
plt.close()

# Center the surprise button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("💕 Surprise Me Again! 💕", key="surprise_btn"):
        # Generate new message
        new_message = random.choice(love_messages)
        # Make sure it's different from current message if possible
        attempts = 0
        while new_message == st.session_state.current_message and attempts < 5:
            new_message = random.choice(love_messages)
            attempts += 1
        
        st.session_state.current_message = new_message
        st.session_state.message_count += 1
        st.rerun()

# Footer with floating hearts
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: rgba(255, 105, 180, 0.1); border-radius: 15px;">
    <p style="color: #FF69B4; font-size: 1.1rem; font-weight: bold;">
        💕 Made with endless love for the most amazing Jeru 💕
    </p>
    <div style="font-size: 2rem; margin-top: 1rem;">
        💖 💕 💗 💖 💕 💗 💖
    </div>
</div>
""", unsafe_allow_html=True)

# Add some floating animation for hearts
st.markdown("""
<style>
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating-hearts {
        animation: float 3s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)