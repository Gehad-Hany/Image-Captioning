# Image Captioning with AI 🖼️📝

This project uses a pre-trained image captioning model to generate captions for uploaded images. The user can upload an image, adjust the display size, and select the caption style (short or detailed). The project is built using Streamlit for the UI and the BLIP model from Hugging Face's Transformers library for image captioning.

## Features

- Upload an image in JPG, PNG, or JPEG format.
- Adjust the display width of the uploaded image.
- Select between short and detailed caption styles.
- Generate and display a caption for the uploaded image.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/project3_cv.git
    cd project3_cv
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` includes the following packages:
    ```txt
    streamlit
    transformers
    pillow
    torch
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run project3_cv.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

3. Upload an image, adjust the display size, select the caption style, and view the generated caption.

## Model

This project uses the BLIP (Bootstrapping Language-Image Pre-training) model from Salesforce for image captioning. The model and processor are loaded from the Hugging Face Transformers library.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.