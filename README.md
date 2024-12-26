# PDF Q&A Chatbot

This application allows users to upload a PDF document, extract its text, and then ask questions related to the content of the document. It uses OpenAI's GPT-3.5-turbo model to provide answers based on the text extracted from the PDF.

## Features

- **PDF Upload:** Upload a PDF file to extract text content.
- **Text Extraction:** Automatically extracts text from the PDF.
- **Interactive Q&A:** Ask questions about the content of the PDF, and the chatbot will provide answers based on the extracted text.
- **OpenAI Integration:** Uses OpenAI's API to process questions and generate responses.

## Requirements

- Python 3.7 or higher
- Streamlit
- PyPDF2
- OpenAI Python library

## Installation

To run this app, you'll need to install the required libraries. Follow the steps below to set up the environment and install dependencies.

### 1. Create a Virtual Environment

Before running the app, it's a good practice to create a virtual environment to isolate the dependencies required for this project. Follow the steps below to set up the environment:

#### Step-by-step instructions:

1. **Install Python** (if not already installed):

   Ensure that you have Python 3.7 or higher installed on your system. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).

2. **Create a Virtual Environment**:

   Open your terminal (or command prompt) and navigate to the directory where you want to store the project. Then, create a virtual environment by running the following command:

   ```bash
   python -m venv pdf-qa-chatbot-env
   ```
   This will create a directory named pdf-qa-chatbot-env in your current folder, which will contain the isolated Python environment.

3. **Activate the Virtual Environment**:

    ```bash
    .\pdf-qa-chatbot-env\Scripts\activate
    ```

    After activation, you should see the environment name in your terminal prompt, like this:
    ```bash
    (pdf-qa-chatbot-env) $
    ```
### 2. Install Required Libraries

Once the virtual environment is activated, install the necessary Python packages (Streamlit, PyPDF2, and OpenAI) by running the following command:

  ```bash
  pip install streamlit PyPDF2 openai
  ```
This will install all the dependencies needed for the app to run.

### 3. Get your OpenAI API Key
To use this app, you will need an OpenAI API key. You can obtain it by signing up on OpenAI's website.

### 4. Running the App
After installing the necessary dependencies, follow these steps:

Save the provided Python script in a file, for example, app.py.

In the terminal (with the virtual environment activated), navigate to the folder where your script is located and run:

  ```bash
  streamlit run app.py
  ```
The app will open in your default web browser.

### 5. Using the App

- Step 1: Enter your OpenAI API key in the sidebar to authenticate your requests.
- Step 2: Upload a PDF file using the file uploader in the app. The text will be automatically extracted from the uploaded PDF.
- Step 3: Ask any question related to the content of the PDF, and the chatbot will provide answers based on the document's text.
- 
### 6. Deactivating the Virtual Environment

When you're done using the app, you can deactivate the virtual environment by running the following command:

  ```bash
  deactivate
  ```

## Code Overview

- **extract_text_from_pdf(pdf_file)**: This function reads the uploaded PDF file and extracts the text from each page using the PyPDF2 library.
- **chat_with_openai(api_key, context, user_question)**: This function sends a request to the OpenAI API using the provided API key, the extracted PDF text as the context, and the user's question. The response is returned to the app and displayed to the user.
- **Streamlit UI**: The app consists of a file uploader to upload the PDF, a text area to display the extracted content, and an input field to ask questions related to the PDF.


## Example

1. **Upload PDF**: Upload a PDF document.
2. **Ask a Question**: After extracting the text, you can ask questions such as:
  -  "What is the summary of the document?"
  -  "Explain the key points discussed on page 3."
  -   What are the main conclusions of the document?"

The chatbot will use the context of the PDF to generate answers.

## Limitations

The quality of the answer depends on the accuracy of the PDF text extraction.
Large PDFs might result in slower responses due to the amount of text being processed.
