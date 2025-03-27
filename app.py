from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

SCIENTIFIC_NUMBER_REGEX = r'^-?\d+(\.\d+)?(e[-+]?\d+)?$'

def is_scientific_number(input_str):
    return bool(re.match(SCIENTIFIC_NUMBER_REGEX, input_str.strip()))

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Scientific Number Validator</title>
</head>
<body>
    <h2>Enter a number:</h2>
    <form method="POST">
        <input type="text" name="number" required>
        <button type="submit">Check</button>
    </form>
    {% if result is not none %}
        <p><strong>Message:</strong> {{ 'Yes, it is a number' if result else 'No, it is not a number' }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form.get('number', '')
        result = is_scientific_number(user_input)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
