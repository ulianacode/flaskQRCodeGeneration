from flask import Flask, render_template

from barcodeGenerator import generate_barcode
from qrGenerator import generate_qr

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/generate_qr', methods=['POST'])
def generator():
    generate_qr()
    return render_template('qr.html')

@app.route('/generate_barcode', methods=['POST'])
def generator_barcode():
    generate_barcode()
    return render_template('barcode.html')

if __name__ == '__main__':
    app.run(debug=True)