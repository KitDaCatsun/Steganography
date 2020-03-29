from PIL import Image


def ASCII_to_text(ascii):
    text = ''
    for i in range(0, len(ascii), 3):
        v = ascii[i] + ascii[i + 1] + ascii[i + 2]
        text += chr(int(v))

    return text


def hide(fileName, imageName, outputName):
    file = open(fileName).read()
    image = Image.open(imageName)

    outputImage = image.copy()
    message = ''.join([str(ord(c)).zfill(3) for c in file])

    for i in range(0, len(message), 3):
        x = i % outputImage.size[0]
        y = i // outputImage.size[0]

        pixel = image.getpixel((x, y))
        newPixel = []
        for j in range(3):
            v = str(pixel[j]).zfill(3)
            newPixel.append(int(v[0] + v[1] + message[i+j]))

        outputImage.putpixel((x, y), tuple(newPixel))

    outputImage.save(outputName)
    return message


def extract(imageName, end):
    image = Image.open(imageName)

    message = ''

    for i in range(0, image.size[0] * image.size[1], 3):
        x = i % image.size[0]
        y = i // image.size[0]

        pixel = image.getpixel((x, y))
        for j in range(3):
            message += str(pixel[j])[-1]

        if ASCII_to_text(message).endswith(end):
            break

    return ASCII_to_text(message).strip(end)


print('This should work with any ascii characters')
print('The message can be as large as the image resolution')
print('Output as a .png so that there is no compression')
print('Add some unique characters to the end of the input text so that it knows when to stop')
print('To learn about Steganography: https://www.youtube.com/watch?v=TWEXCYQKyDc')

print()

while True:
    task = input('Hide or Extract: ').upper()
    if task == 'HIDE':
        text = input('Text file to hide (Text.txt): ')
        inputFile = input('Input image file (Image.jpg): ')
        outputFile = input('Output image name (Output.png): ')
        print('Hiding...')
        hide(text, inputFile, outputFile)
        print('Done\n')
    else:
        image = input('Image to extract from (Output.png): ')
        end = input('Ending characters (END): ')
        print('Extracting...')
        message = extract(image, end)
        print('Done. Message:\n')
        print(message)
        print()
