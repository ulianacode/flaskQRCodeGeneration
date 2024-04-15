# Flask Barcode and QR Code Generator

This is a simple web application built with Flask that generates QR codes and barcodes.


## Usage

1. Run the Flask application by executing `app.py`.
2. Access the web application in your browser at `http://localhost:5000`.
3. Click on the "Generate QR Code" or "Generate Barcode" buttons to generate the respective code.
4. The generated QR code or barcode will be displayed on a new page.

## File Structure

- `app.py`: Contains the Flask application code.
- `barcodeGenerator.py`: Module for generating barcodes.
- `qrGenerator.py`: Module for generating QR codes.
- `templates/`: Contains HTML templates for rendering the web pages.
  - `index.html`: Home page template.
  - `qr.html`: Template for displaying generated QR code.
  - `barcode.html`: Template for displaying generated barcode.

## Libraries Used

- Flask: Web framework for Python.
- [Barcode Generator Library]([https://python-barcode.readthedocs.io/en/stable/index.html]): Library for generating barcodes.
- [QR Code Generator Library]([https://pypi.org/project/qrcode/]): Library for generating QR codes.
