# Code Analysis Web Application

This web application allows users to upload multiple code files, and it analyzes them to count the number of lines, blank lines, comment lines, and code lines. The supported programming languages are Python, Java, JavaScript, C, and C++.

## Features

- Upload multiple code files at once.
- Analyze the following for each file:
  - Total number of lines.
  - Number of blank lines.
  - Number of comment lines.
  - Number of code lines.
- Supported programming languages:
  - Python (`.py`)
  - Java (`.java`)
  - JavaScript (`.js`)
  - C (`.c`)
  - C++ (`.cpp`)

## Technologies Used

- Backend: Flask (Python Web Framework)
- Frontend: HTML, CSS, JavaScript
- Regular Expressions: For comment and blank line detection.

## Requirements

- Python 3.x
- Flask
- A modern web browser

## Project Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/code-analysis-web-app.git
   cd code-analysis-web-app

2. Install the required dependencies:
    pip install -r requirements.txt

3. Start the Flask development server:
    python3 app.py

4. Open your browser and go to http://127.0.0.1:5001/ to access the application.

Usage
    Upload Files: Click the "Choose files" button to select one or more code files. The application supports multiple file uploads at once.

    Analyze Code: After selecting the files, click the "Get Count" button. The application will process the files and display the following results for each file:
        Total Lines
        Blank Lines
        Comment Lines
        Code Lines

    Clear All: You can clear all file inputs and results by clicking the "Clear All" button.

    Select More: You can add additional file input fields by clicking the "Select More" button.

