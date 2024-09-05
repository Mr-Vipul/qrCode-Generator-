# QR Code Generator

This project demonstrates how to generate QR codes using Python's qrcode library. You can generate a QR code for any URL and save it as an image file. The project allows customization of the QR code's size, error correction level, and colors.


# Features
Generate QR codes for any URL.
Customize QR code size, error correction, and colors.
Save the QR code as an image file (e.g., PNG format).
Easy to use and lightweight.

## Installation


1. qrcode library
2. Pillow library (used internally by qrcode for image generation).

```bash
pip install qrcode
```

# Usage
## Simple QR Code
You can generate a basic QR code using a URL and save it as an image file:

```python
import qrcode

# Generate a simple QR code
img = qrcode.make('https://www.add_your_link_here')

# Save the QR code as an image file
img.save("QRCode.png")
```

# Advanced QR Code Customization
For more control over the QR code's size, error correction, and appearance, use the QRCode object:

```python
import qrcode

# Create a QRCode object with customization options
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction (7% of data can be restored)
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (in boxes)
)

# Add your data (the URL you want to encode)
qr.add_data('https://www.add_your_link_here')
qr.make(fit=True)  # Adjusts the dimensions of the QR code to fit the data

# Generate the image with specific colors (default: black QR code on a white background)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("CustomQRCode.png")

```

## Explanation of Parameters

1. version: Controls the size of the QR code. Higher values mean larger QR codes. Version 1 is the smallest.
2. error_correction: Determines how much of the QR code can be recovered if damaged. The options are:
3. ERROR_CORRECT_L: About 7% error recovery.
4. ERROR_CORRECT_M: About 15% error recovery.
5. ERROR_CORRECT_Q: About 25% error recovery.
6. ERROR_CORRECT_H: About 30% error recovery.
7. box_size: The size of each square (box) in the QR code grid.
8. border: The width of the border (measured in boxes) around the QR code.
9. fill_color: The color of the QR code itself (default is black).
10. back_color: The background color of the QR code (default is white).

# Example
When you generate a QR code for ```https://www.example.com``` with the advanced method, it will output a file named ```CustomQRCode.png```.

You can adjust the version, error correction level, box size, and colors to customize the QR code to your preference.
