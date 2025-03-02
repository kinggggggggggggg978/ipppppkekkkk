# -*- coding: utf-8 -*-
import streamlit as st
import datetime
import time

# Page setup with cute background
st.set_page_config(page_title="For Ipek 💖", page_icon="💕", layout="centered")

# Custom CSS for kawaii styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Quicksand', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 100%);
    }
    
    h1, h2, h3 {
        color: #ff66b2 !important;
    }
    
    .pulsing-heart {
        font-size: 80px;
        color: #ff3385;
        animation: pulse 1.5s infinite;
        text-align: center;
        margin: 20px 0;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    .counter-box {
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 10px;
        margin: 5px;
        text-align: center;
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
    
    .letter {
        background: #fff0f5;
        padding: 30px;
        border-radius: 20px;
        position: relative;
        box-shadow: 0 10px 20px rgba(255, 102, 178, 0.1);
        border: 2px dashed #ff66b2;
        margin: 20px 0;
    }
    
    .pandas {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    
    .panda {
        font-size: 40px;
        margin: 0 10px;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    .panda:nth-child(2) {
        animation-delay: 0.3s;
    }
    
    .panda:nth-child(3) {
        animation-delay: 0.6s;
    }
</style>
""", unsafe_allow_html=True)

# Title with love message
st.markdown("<h1 style='text-align: center; color: white; text-shadow: 3px 3px 0px rgba(255, 102, 178, 0.5);'>For My Sweet Ipek 💕</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 1.5rem;'>Hi Ipek, I love you! 💖</p>", unsafe_allow_html=True)

# Pulsing heart
st.markdown("<div class='pulsing-heart'>❤️</div>", unsafe_allow_html=True)

# Calculate time together
start_date = datetime.datetime(2024, 1, 27)
current_date = datetime.datetime.now()
difference = current_date - start_date

days = difference.days
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60
seconds = difference.seconds % 60

# Display timer
st.markdown("<h2 style='text-align: center;'>We've been in love for</h2>", unsafe_allow_html=True)

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

# Cute pandas
st.markdown("<div class='pandas'><div class='panda'>🐼</div><div class='panda'>🐼</div><div class='panda'>🐼</div></div>", unsafe_allow_html=True)

# Sweet letter
st.markdown(
    """
    <div class="letter">
        <h2 style="text-align: center; color: #ff66b2;">For My Love Ipek... 💌</h2>
        <p style="color: #ff66b2;">My dearest Ipek,</p>
        <p style="color: #ff66b2;">Every moment with you feels like a dream come true. Your smile brightens my darkest days, and your laugh is the sweetest melody I've ever heard.</p>
        <p style="color: #ff66b2;">You are my sunshine, my heart, my everything. I cherish every second we spend together and look forward to creating countless more beautiful memories.</p>
        <p style="color: #ff66b2;">Thank you for being the amazing person you are. I fall in love with you more and more each day.</p>
        <p style="margin-top: 2rem; font-style: italic; text-align: right; color: #ff66b2;">Forever yours,<br>Zarkan</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Add a little footer
st.markdown("<p style='text-align: center; margin-top: 50px; color: white;'>Made with ❤️ just for you</p>", unsafe_allow_html=True)

# Auto-refresh to keep timer updated
st.markdown("""
<script>
    setTimeout(function(){
        window.location.reload();
    }, 60000);
</script>
""", unsafe_allow_html=True) 
