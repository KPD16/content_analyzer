from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Function to analyze code
def analyze_code(file_content, language):
    total_lines = 0
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    # Define patterns for single-line comments
    if language == "python":
        single_comment_pattern = r'^\s*#'
    elif language in ["java", "javascript", "c", "cpp"]:
        single_comment_pattern = r'^\s*//'
    else:
        return None  # Unsupported language

    lines = file_content.splitlines()

    for line in lines:
        total_lines += 1
        stripped_line = line.strip()

        if not stripped_line:
            blank_lines += 1
            continue

        # Handle single-line comments
        if re.match(single_comment_pattern, stripped_line):
            comment_lines += 1
        else:
            code_lines += 1

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "code_lines": code_lines
    }

# Route to serve the upload page
@app.route('/')
def upload_page():
    return render_template('file.html')

# Route to handle file uploads and analysis
@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('uploadedFiles')
    result = []

    for file in files:
        content = file.read().decode('utf-8', errors='ignore')
        filename = file.filename
        extension = filename.split('.')[-1].lower()

        # Determine language based on file extension
        if extension == "py":
            language = "python"
        elif extension == "java":
            language = "java"
        elif extension == "js":
            language = "javascript"
        elif extension == "c":
            language = "c"
        elif extension == "cpp":
            language = "cpp"
        else:
            result.append(f"<strong>{filename}</strong>: Unsupported file type<br>")
            continue

        # Analyze the file
        analysis = analyze_code(content, language)
        if analysis:
            result.append(f"<strong>{filename}</strong>:<br>")
            result.append(f"Total Lines: {analysis['total_lines']}<br>")
            result.append(f"Blank Lines: {analysis['blank_lines']}<br>")
            result.append(f"Comment Lines: {analysis['comment_lines']}<br>")
            result.append(f"Code Lines: {analysis['code_lines']}<br>")
            result.append("<br>")
        else:
            result.append(f"<strong>{filename}</strong>: Analysis failed<br>")

    return ''.join(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
