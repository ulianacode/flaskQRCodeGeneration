from flask import request
import barcode
from barcode.writer import ImageWriter


def generate_barcode():
    text = request.form['text1']
    sample_barcode = barcode.get('code128', text, writer=ImageWriter())
    sample_barcode.save('static/barcode')
