#!/usr/bin/python3
"""Flask application that displays items from a JSON file."""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    """Display items loaded from a JSON file."""
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get('items', [])

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
