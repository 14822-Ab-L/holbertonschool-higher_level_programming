#!/usr/bin/python3
"""Flask application that displays products from JSON, CSV or SQLite."""

import csv
import json
import sqlite3
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


def read_sql():
    """Read product data from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products_list = [dict(row) for row in cursor.fetchall()]
        return products_list
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            products_list = read_json()
        elif source == 'csv':
            products_list = read_csv()
        elif source == 'sql':
            products_list = read_sql()
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

    except sqlite3.Error:
        return render_template(
            'product_display.html',
            error="Database error",
            products=[]
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
