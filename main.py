from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__, template_folder='src')

# Path for the file where data will be stored
DATA_FILE = "listings.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    data = {
        'location': request.form.get('location'),
        'price_range': request.form.get('price_range'),
        'facing': request.form.get('facing'),
        'landmarks': request.form.get('landmarks'),
        'description': request.form.get('description'),
        'email': request.form.get('email'),
        'mobile': request.form.get('mobile'),
        'area': request.form.get('area'),
        'road_width': request.form.get('road_width'),
        'distance_main_road': request.form.get('distance_main_road'),
        'zoning': request.form.get('zoning'),
        'action': request.form.get('submit_action')
    }

    # Read existing data from the JSON file
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                listings = json.load(f)
            except json.JSONDecodeError:
                listings = []
    else:
        listings = []

    # Append the new data
    listings.append(data)

    # Write the updated list back to the file
    with open(DATA_FILE, 'w') as f:
        json.dump(listings, f, indent=4)

    # Redirect to a success page or back to the form
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)