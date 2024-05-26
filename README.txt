# Image Text and Visual Element Extraction

This project analyzes images to extract text using Optical Character Recognition (OCR) and segment visual elements using the Google Cloud Vision API. It includes a simple web interface for uploading images and viewing the extracted content.

## Table of Contents

- [Description](#description)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Description

The project:
- Analyzes an uploaded image.
- Extracts text using OCR.
- Segments visual elements in the image.
- Displays the extracted text and elements on a web page.

## Setup

### Prerequisites

- Python 3.x
- Google Cloud Platform account with Vision API enabled
- A billing account set up on Google Cloud Platform

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Set up a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Google Cloud credentials**:

    - Create a service account and download the JSON key file.
    - Save the JSON key file to the `keys` directory.
    - Set the environment variable to the path of your JSON key file:

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="keys/your-service-account-file.json"
    ```

    On Windows:

    ```sh
    set GOOGLE_APPLICATION_CREDENTIALS=keys\your-service-account-file.json
    ```

5. **Create necessary directories**:

    ```sh
    mkdir images output
    ```

## Usage

1. **Run the Flask application**:

    ```sh
    python app.py
    ```

2. **Open your web browser and go to** `http://localhost:5000`.

3. **Upload an image** using the web interface.

4. **View the extracted text and visual elements** on the output page.

## Project Structure

