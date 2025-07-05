from PIL import Image

def convert_to_grayscale(input_path, output_path):
    try:
        # Open image
        image = Image.open(input_path)
        
        # Convert to grayscale
        grayscale = image.convert("L")
        
        # Save new image
        grayscale.save(output_path)
        print(f"Grayscale image saved as '{output_path}'.")

    except FileNotFoundError:
        print(f"Error: '{input_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    convert_to_grayscale("fish.jpg", "output.jpg")