# -*- coding: utf-8 -*-
import streamlit as st
import datetime

# Page setup
st.set_page_config(page_title="For Ipek 💖", page_icon="💕")

# Title
st.title("For My Sweet Ipek 💖")
st.write("Because you're my everything")

# Calculate time together
start_date = datetime.datetime(2024, 1, 27)
current_date = datetime.datetime.now()
difference = current_date - start_date
days = difference.days

# Show counter
st.header(f"We've been in love for {days} days 💘")
st.write("Since January 27, 2024")

# Message
st.markdown("""
## A Letter For You 💌

Dear Ipek,

I wanted to create something special to show you how much you mean to me. 
Every day with you is a gift, and I'm constantly grateful for having you in my life.

With all my love,
[Your Name]
""") 
