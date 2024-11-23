import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image  


def create_qr_code(data, filename="qrcode.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

def decode_qr_code(filename):
    img = cv2.imread(filename)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(f"Decoded Data: {obj.data.decode('utf-8')}")


if __name__ == "__main__":  
    print("1. Encode QR Code")
    print("2. Decode QR Code")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        data = input("Enter the data to encode: ")
        create_qr_code(data)
    elif choice == 2:
        filename = input("Enter the filename of the QR code to decode: ")
        decode_qr_code(filename)
    else:
        print("Invalid choice!")
