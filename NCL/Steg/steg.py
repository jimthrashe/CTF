from PIL import Image

def reveal_hidden_colors(image_path):
    try:
        # Open the BMP image
        image = Image.open(image_path)

        # Get the pixel data
        pixels = list(image.getdata())

        # Print the RGB values of each pixel
        for pixel in pixels:
            print(pixel)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    image_path = "STEG2.bmp"  # Replace with the path to your .bmp image
    reveal_hidden_colors(image_path)

