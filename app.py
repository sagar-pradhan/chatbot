from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

# Set up Gemini API key
my_api_key_gemini = "AIzaSyBzbHr3BeHtoRY8P9bf2dMaJOpF-mfw5dQ"  # Replace with your valid API key
genai.configure(api_key=my_api_key_gemini)

# Initialize Gemini Model
model = genai.GenerativeModel('gemini-pro')

# Initialize Flask app
app = Flask(__name__)

# 404 Error handler
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

# Main route
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Get prompt from the user
            prompt = request.form['prompt']

            # Get response from Gemini
            response = model.generate_content(prompt)

            # Check for valid response
            if response and hasattr(response, 'text'):
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        
        except Exception as e:
            print("Error while generating content:", e)
            return "An error occurred while fetching the Gemini response."

    # Render the main template
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
