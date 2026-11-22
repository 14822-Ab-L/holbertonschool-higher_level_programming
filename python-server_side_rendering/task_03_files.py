#!/usr/bin/python3
"""Flask application that displays products from JSON or CSV files."""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read product data from a JSON file."""
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    """Read product data from a CSV file."""
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


@app.route('/products')
def products():
    """Display products from JSON or CSV, with optional ID filtering."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[]
        )

    if product_id is not None:
        products_list = [
            product for product in products_list
            if str(product['id']) == product_id
        ]

        if not products_list:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[]
            )

    return render_template(
        'product_display.html',
        products=products_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
