from PIL import Image
import sys



#Obviously this did not work but I essentially tried pulling hidden pixels which was way more than needed apparently.



# Function to reveal text from an image
def reveal_text_from_image(image_path):
    try:
        # Open the image with hidden text
        img = Image.open(image_path)

        binary_text = ''

        # Loop through each pixel of the image
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))

                # Extract the least significant bit from each color channel
                for color_channel in range(3):
                    binary_text += str(pixel[color_channel] & 1)

        # Convert binary text to characters
        hidden_text = ''.join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8))

        print("Hidden Text:", hidden_text)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reveal_text.py <image_path>")
    else:
        image_path = sys.argv[1]

        # Reveal the hidden text from the image
        reveal_text_from_image(image_path)

