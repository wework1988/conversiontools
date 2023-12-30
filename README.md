# Image Converter Web App

This web app allows users to convert images from JPEG to PNG or PNG to JPEG.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.x recommended)
- Django
- Git

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/wework1988/conversiontools.git
    ```

2. Navigate to the project directory:

    ```bash
    cd image-converter
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the main page at http://127.0.0.1:8000/ to use the image converter.

## Usage

- Visit http://127.0.0.1:8000/ to see the main page.
- Click on "JPEG to PNG Converter" or "PNG to JPEG Converter" to go to the respective conversion pages.
- Follow the on-screen instructions to convert images.