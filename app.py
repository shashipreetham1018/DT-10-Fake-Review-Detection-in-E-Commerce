from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Serve the homepage

# Route for the prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the review from the form
        review = request.form.get('review')
        # Simulate prediction logic (replace with your ML model)
        is_fake = len(review) % 2 == 0  # Example logic: fake if review length is even
        result = "FAKE" if is_fake else "REAL"
        return render_template('predict.html', result=result)  # Pass the result to the template
    return render_template('predict.html')  # Serve the prediction page

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)  # Ensure it binds to 0.0.0.0
