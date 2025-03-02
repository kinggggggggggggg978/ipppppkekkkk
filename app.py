import streamlit as st
import datetime
import time
import base64
from pathlib import Path
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="For My Sweet Ipek 💖",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it look kawaii
def local_css():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Quicksand', sans-serif;
    }
    
    .main {
        background-color: #fff0f5;
    }
    
    h1, h2, h3 {
        color: #ff66b2 !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 100%);
    }
    
    .css-1kyxreq, .css-10trblm {
        color: #ff66b2 !important;
    }
    
    .stButton>button {
        background-color: #ff66b2;
        color: white;
        border: 2px solid white;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(255, 102, 178, 0.3);
    }
    
    .counter-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 20px 0;
    }
    
    .counter-box {
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 10px;
        min-width: 80px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 2px solid rgba(255, 102, 178, 0.3);
    }
    
    .counter-value {
        font-size: 2rem;
        font-weight: 700;
        color: #ff66b2;
    }
    
    .counter-label {
        font-size: 0.8rem;
        color: #ff66b2;
    }
    
    .memory-card {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(255, 102, 178, 0.1);
        border: 2px solid #ffb6c1;
        transition: transform 0.3s;
        height: 100%;
    }
    
    .memory-card:hover {
        transform: translateY(-10px) rotate(2deg);
    }
    
    .reason-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(255, 102, 178, 0.1);
        border: 2px solid #ffb6c1;
        height: 100%;
        transition: transform 0.3s;
    }
    
    .reason-card:hover {
        transform: translateY(-10px);
        border-color: #ff66b2;
    }
    
    .letter {
        background: #fff0f5;
        padding: 30px;
        border-radius: 20px;
        position: relative;
        box-shadow: 0 10px 20px rgba(255, 102, 178, 0.1);
        border: 2px dashed #ff66b2;
        margin: 20px 0;
    }
    
    .bucket-item {
        background: #fff0f5;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(255, 102, 178, 0.1);
        border: 2px solid #ffb6c1;
        transition: all 0.3s;
        height: 100%;
    }
    
    .bucket-item:hover {
        transform: translateY(-10px);
        background: linear-gradient(135deg, #ffb6c1 0%, #ff66b2 100%);
        color: white !important;
    }
    
    .bucket-item:hover h3 {
        color: white !important;
    }
    
    footer {
        text-align: center;
        padding: 20px;
        color: white;
        background: #ff66b2;
        border-radius: 20px 20px 0 0;
        margin-top: 30px;
    }
    
    /* Floating hearts animation */
    @keyframes float-heart {
        0% {
            transform: translateY(100vh) scale(0.5) rotate(0deg);
            opacity: 0.8;
        }
        100% {
            transform: translateY(-10vh) scale(0.1) rotate(360deg);
            opacity: 0;
        }
    }
    
    .floating-heart {
        position: fixed;
        font-size: 24px;
        color: #ff66b2;
        z-index: 1000;
        animation: float-heart 15s linear forwards;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Function to create floating hearts
def create_floating_hearts():
    hearts_js = """
    <script>
    function createHeart() {
        const heart = document.createElement('div');
        const size = Math.floor(Math.random() * 20) + 15;
        const colors = ['#ff66b2', '#ffb6c1', '#ff91a4', '#ff3385', '#ff0066'];
        const color = colors[Math.floor(Math.random() * colors.length)];
        const leftPosition = Math.random() * 100;
        
        heart.innerHTML = '❤️';
        heart.className = 'floating-heart';
        heart.style.left = `${leftPosition}%`;
        heart.style.fontSize = `${size}px`;
        heart.style.color = color;
        
        document.body.appendChild(heart);
        
        setTimeout(() => {
            heart.remove();
        }, 15000);
    }
    
    // Create hearts at random intervals
    setInterval(createHeart, 800);
    
    // Create initial hearts
    for (let i = 0; i < 10; i++) {
        setTimeout(createHeart, i * 300);
    }
    </script>
    """
    st.markdown(hearts_js, unsafe_allow_html=True)

# Calculate time together
def calculate_time_together():
    start_date = datetime.datetime(2024, 1, 27)
    current_date = datetime.datetime.now()
    difference = current_date - start_date
    
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60
    
    return days, hours, minutes, seconds

# Main app
def main():
    local_css()
    create_floating_hearts()
    
    # Header
    st.markdown("<h1 style='text-align: center; color: white; text-shadow: 3px 3px 0px rgba(255, 102, 178, 0.5);'>For My Sweet Ipek 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size: 1.5rem;'>Because you're my everything</p>", unsafe_allow_html=True)
    
    # Love counter
    st.markdown("<div style='text-align: center; margin: 30px 0;'><h2 style='color: white !important;'><i class='fas fa-heart'></i> We've been in love for <i class='fas fa-heart'></i></h2></div>", unsafe_allow_html=True)
    
    days, hours, minutes, seconds = calculate_time_together()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="counter-box">
            <div class="counter-value">{days}</div>
            <div class="counter-label">Days</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="counter-box">
            <div class="counter-value">{hours}</div>
            <div class="counter-label">Hours</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="counter-box">
            <div class="counter-value">{minutes}</div>
            <div class="counter-label">Minutes</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="counter-box">
            <div class="counter-value">{seconds}</div>
            <div class="counter-label">Seconds</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: white;'>Since January 27, 2024 💘</p>", unsafe_allow_html=True)
    
    # Heart animation
    st.markdown("<div style='text-align: center; margin: 30px 0;'><span style='font-size: 5rem; color: #ff66b2; filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.7));'>❤️</span></div>", unsafe_allow_html=True)
    
    # Memories section
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Our Kawaii Memories 💖</h2>", unsafe_allow_html=True)
    
    memory_col1, memory_col2, memory_col3 = st.columns(3)
    
    with memory_col1:
        st.markdown("""
        <div class="memory-card">
            <div style="height: 200px; background-color: #fff0f5; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #ffb6c1;">
                <span style="font-size: 3rem; margin-bottom: 1rem; color: #ff66b2;">🖼️</span>
                <p>Add your first memory here</p>
            </div>
            <div style="padding: 1.5rem; text-align: left; background-color: white; position: relative;">
                <h3>Our First Date</h3>
                <p>Add a description of your first date here.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with memory_col2:
        st.markdown("""
        <div class="memory-card">
            <div style="height: 200px; background-color: #fff0f5; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #ffb6c1;">
                <span style="font-size: 3rem; margin-bottom: 1rem; color: #ff66b2;">🖼️</span>
                <p>Add your favorite adventure</p>
            </div>
            <div style="padding: 1.5rem; text-align: left; background-color: white; position: relative;">
                <h3>Our Adventure</h3>
                <p>Describe a special adventure you had together.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with memory_col3:
        st.markdown("""
        <div class="memory-card">
            <div style="height: 200px; background-color: #fff0f5; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #ffb6c1;">
                <span style="font-size: 3rem; margin-bottom: 1rem; color: #ff66b2;">🖼️</span>
                <p>Add a special moment</p>
            </div>
            <div style="padding: 1.5rem; text-align: left; background-color: white; position: relative;">
                <h3>Special Moment</h3>
                <p>Share a particularly meaningful memory together.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Reasons section
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Reasons Why Ipek Is Amazing 💝</h2>", unsafe_allow_html=True)
    
    reason_col1, reason_col2, reason_col3 = st.columns(3)
    
    with reason_col1:
        st.markdown("""
        <div class="reason-card">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Smile</h3>
                <p>The way you smile lights up my world like nothing else.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="reason-card" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Intelligence</h3>
                <p>Your brilliant mind and creativity constantly amaze me.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with reason_col2:
        st.markdown("""
        <div class="reason-card">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Kindness</h3>
                <p>Your heart is full of kindness that inspires me every day.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="reason-card" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Passion</h3>
                <p>The passion you have for the things you love is incredible.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with reason_col3:
        st.markdown("""
        <div class="reason-card">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Humor</h3>
                <p>Your laugh and sense of humor make every moment better.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="reason-card" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Your Support</h3>
                <p>You're always there for me, no matter what.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Letter section
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>A Letter For You 💌</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="letter">
        <p>Dear Ipek,</p>
        <p>I wanted to create something special to show you how much you mean to me. Every day with you is a gift, and I'm constantly grateful for having you in my life.</p>
        <p>Your smile brightens my darkest days, your laugh is my favorite sound, and your heart is the most beautiful thing I've ever known.</p>
        <p>I cherish every moment we spend together and look forward to creating countless more memories.</p>
        <p>Thank you for being you. Thank you for being in my life.</p>
        <p style="margin-top: 2rem; font-style: italic; text-align: right;">With all my love,<br>[Your Name]</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bucket list section
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Our Kawaii Bucket List 💕</h2>", unsafe_allow_html=True)
    
    bucket_col1, bucket_col2, bucket_col3 = st.columns(3)
    
    with bucket_col1:
        st.markdown("""
        <div class="bucket-item">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Travel to [Dream Destination]</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="bucket-item" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Watch [Movie/Show] Marathon</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with bucket_col2:
        st.markdown("""
        <div class="bucket-item">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Try [Cuisine] Together</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="bucket-item" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>See [Artist] in Concert</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with bucket_col3:
        st.markdown("""
        <div class="bucket-item">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Hike [Mountain/Trail]</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="bucket-item" style="margin-top: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 2.5rem; color: #ff66b2; margin-bottom: 1rem; display: inline-block;">❤️</span>
                <h3>Add more dreams here...</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <footer>
        <p>Made with ❤️ for my sweet Ipek</p>
        <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.8;">Created on """ + datetime.datetime.now().strftime("%B %d, %Y") + """</p>
    </footer>
    """, unsafe_allow_html=True)
    
    # Auto-refresh for the counter
    st.markdown("""
    <script>
        setTimeout(function(){
            window.location.reload();
        }, 60000);
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
