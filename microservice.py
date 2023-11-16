from flask import Flask, jsonify
from random import choice
from NP_Program import NationalParks  # Assuming your partner's program is in a file named partner_program.py

app = Flask(__name__)

# Create an instance of the NationalParks class
national_parks_instance = NationalParks()

@app.route('/generate_random_park', methods=['GET'])
def generate_random_park():
    # Get the list of national parks
    nat_parks_list = national_parks_instance.get_all_parks(national_parks_instance.current_page, national_parks_instance.per_page)

    # Choose a random park
    random_park = choice(nat_parks_list)

    return jsonify({"random_park": random_park})

if __name__ == '__main__':
    app.run(debug=True)
