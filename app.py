import json
import re
import requests
import streamlit as st
import pandas as pd
import numpy as np
import pytesseract
from image_text import extract_textile
from PIL import Image
from streamlit_lottie import st_lottie

dictionary = {
    "flax": "flax",
    "cotton": "cotton",
    "coton": "cotton",
    "wool": "wool",
    "viscose": "viscose",
    "polypropylene": "polypropylene",
    "polyester": "polyester",
    "acrylic": "acrylic",
    "nylon": "nylon",
    "hemp": "hemp",
}


def load_lottieurl(url: str):
    """Load a Lottie animation from a URL."""
    result = requests.get(url)
    if result.status_code != 200:
        return None
    return result.json()


lottie_fashion = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_gn0tojcq.json"
)

st.title("🐙 Clothes for Good ")

st.write(
    "Show us a clothing tag and we will show you the environmental footprint of this purchase 🌵"
)


left_col, right_col = st.columns([1, 3])
with left_col:
    st.write("")
    st.write("")
    st.subheader("""Your compass for shopping clothes sustainably!""")

with right_col:
    st_lottie(lottie_fashion, speed=1, height=200, key=None)

st.subheader("Take a picture of the clothing tag!")

img_file_buffer = st.camera_input("")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    img = Image.open(img_file_buffer)
    processed_image = pytesseract.image_to_string(img)
    materials = extract_textile(processed_image, dictionary)
    st.write(materials)

st.subheader("Tell us more about this item 👑!")

col1, col2 = st.columns(2)

with col1:
    genre = st.radio(
        "What kind of clothing is it?",
        (
            "T-Shirt",
            "Sweatshirt",
            "Sweater",
            "Jacket",
            "Blazer",
            "Underwear",
            "Dress",
            "Pants",
            "Shorts",
            "Socks",
        ),
        horizontal=True,
    )

with col2:
    size = st.select_slider(
        "What is the size?",
        options=["Kids", "Small", "Medium", "Large", "Extra Large"],
    )
materials = {'cotton': 80, 'polyester': 20}
# Get the weight matrix
weight = pd.read_csv("cloth_type.csv", index_col=0) / 1000
# Get the material matrix
footprint = pd.read_csv("material_cost.csv", index_col=0)
# Get the specific weight of the clothing
clothing_weight = weight.loc['T-Shirt', "Small"]

# Get the specific footprint of the clothing
total_footprint = {"energy": 0, "co2": 0, "water": 0}
for mat, percent in materials.items():
    for cost_type in total_footprint.keys():
        total_footprint["cost_type"] += (
            clothing_weight * percent * footprint.loc[mat, "cost_type"]
        )
print(total_footprint)
st.write(total_footprint)
