import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load the image captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Streamlit UI
st.title("Image Captioning with AI 🖼️📝")
st.write("Upload an image, and the AI will generate a caption for it!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    # Allow user to adjust image display size
    img_width = st.slider("Adjust Image Width", min_value=200, max_value=600, value=400, step=50)
    st.image(image, caption="Uploaded Image", width=img_width)  # Display the image with adjustable width
    
    # Select caption style
    caption_style = st.selectbox("Select Caption Style:", ["Short", "Detailed"])
    
    # Process the image and generate a caption
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_length=30 if caption_style == "Short" else 60)
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    # Display the caption
    st.subheader("Generated Caption:")
    st.write(f"**{caption}**")
