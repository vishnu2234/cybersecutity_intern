from PIL import Image

def encrypt_image(image, key):
   
    # Get image size
    width, height = image.size

    # Encrypt each pixel
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(image.mode, image.size)
    encrypted_img.putdata(encrypted_pixels)

    return encrypted_img

def decrypt_image(encrypted_image, key):
    
    # Get image size
    width, height = encrypted_image.size

    # Decrypt each pixel
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)

    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_img.putdata(decrypted_pixels)

    return decrypted_img

# Prompt user for image dimensions
width = int(input("Enter the width of the image: "))
height = int(input("Enter the height of the image: "))

# Create a simple red image with user-defined dimensions
image = Image.new('RGB', (width, height), color='red')

# Ask user for encryption key
key = int(input("Enter the encryption key: "))

# Encrypt the image
encrypted_image = encrypt_image(image, key)
encrypted_image.show()

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)
decrypted_image.show()