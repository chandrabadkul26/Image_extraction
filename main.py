import os
from google.cloud import vision
import io
import cv2
import numpy as np

# Set the environment variable to the correct path of your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/your-service-account-file.json"

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

def load_image(file_path):
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
    return content

def load_image_cv(file_path):
    return cv2.imread(file_path)

def detect_text(client, image_content):
    image = vision.Image(content=image_content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f"{response.error.message}")

    return texts

def segment_visual_elements(image_cv):
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    segmented_elements = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        segmented_element = image_cv[y:y+h, x:x+w]
        segmented_elements.append(segmented_element)

    return segmented_elements

def save_visual_elements(segmented_elements):
    paths = []
    for i, element in enumerate(segmented_elements):
        path = f'output/element_{i}.png'
        cv2.imwrite(path, element)
        paths.append(path)
    return paths

def generate_html(texts, element_paths):
    html_content = "<html><body>\n"
    html_content += "<h1>Output</h1>\n"
    html_content += "<div>\n"
    html_content += "<h2>Text Content:</h2>\n"
    for text in texts:
        html_content += f"<p>{text}</p>\n"
    html_content += "</div>\n"
    html_content += "<div>\n"
    html_content += "<h2>Visual Elements:</h2>\n"
    for path in element_paths:
        html_content += f'<img src="{path}" alt="Visual Element">\n'
    html_content += "</div>\n"
    html_content += "</body></html>"

    with open("output/output.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def main(image_path):
    image_content = load_image(image_path)
    image_cv = load_image_cv(image_path)

    text_annotations = detect_text(client, image_content)
    texts = [text.description for text in text_annotations]

    segmented_elements = segment_visual_elements(image_cv)
    element_paths = save_visual_elements(segmented_elements)

    generate_html(texts, element_paths)

if __name__ == "__main__":
    image_path = 'images/your-image.jpg'  # Ensure this matches the actual image file name
    main(image_path)
