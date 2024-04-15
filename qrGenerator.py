import qrcode
from flask import request
import segno


def generate_qr():
    text = request.form['text']
    color = request.form['color']
    colorBack = request.form['colorBack']
    qr = segno.make(text, error='h', micro=False, version=10)
    qr.save('static/qrcode.png', scale=5, dark=color, light=colorBack)
