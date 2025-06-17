import sys
import os
from PIL import Image

def encode_image(image_path, message):
    # Kiểm tra file có tồn tại không
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' không tồn tại.")
        return
    
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Đánh dấu kết thúc thông điệp
    data_index = 0

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    # In ra thư mục hiện tại để bạn biết đang chạy ở đâu
    print("Current working directory:", os.getcwd())

    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    print("Image path received:", image_path)
    message = sys.argv[2]

    encode_image(image_path, message)

if __name__ == "__main__":
    main()