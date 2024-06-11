"""
    Function helps to read images and process the data and mark if any string matches with user input.

    Libraries:
     - Yaml --> To read and write yaml files.
     - CV2 --> To process images.

    Parameters:
     - image_int --> Integer passed from domainTest function to process images.

    Usage:
     stringMatch(Integer) --> stringMatch(0) or stringMatch(1).
"""

# Libraries
import modules as md
import os

# Write data to data.yaml.
def open_yaml(arg):
    md.writeYaml(arg)


# Add mask over image.
def process_data(d, i, overlay, image):
    try:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        (x1, y1, w1, h1) = (d['left'][i + 1], d['top'][i + 1], d['width'][i + 1], d['height'][i + 1])
        md.rectangle(overlay, (x, y), (x + w1, y + h1), (0, 255, 0), -1)
        alpha = 0.4
        img_new = md.addWeighted(overlay, alpha, image, 1 - alpha, 0)
        r = 5000.0 / img_new.shape[1]
        dim = (5000, int(img_new.shape[0] * r))
        return md.resize(img_new, dim, interpolation=md.INTER_AREA)
    except IndexError as e:
        pass


# Read and process image.
def stringMatch(image_int):
    data = md.readYaml('data.yaml')

    # tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
    # md.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "Tesseract-OCR/tessdata"'
    md.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

    # Enlarge image to get right data captured for further processing.
    img = md.imread('Images/domainTest_{}.png'.format(image_int))
    new_ratio = 5000.0 / img.shape[1]
    new_dim = (5000, int(img.shape[0] * new_ratio))
    image = md.resize(img, new_dim)

    # Load image to read data.
    d = md.image_to_data(image, output_type=md.Output.DICT, lang='eng', config=tessdata_dir_config)
    n_boxes = len(d['text'])
    overlay = image.copy()

    print('Processing image for necessary data.')

    # Capture data and mark it and pass data to save_image function (calling from domainTest).
    try:
        for i in range(n_boxes):
            text = d['text'][i]

            if image_int == 0:

                data['xdn_{}'.format(image_int)] = 'Imperva setting found' if text == 'Imperva' else 'Not found.'
                if text == data['virtual_ip']:
                    data['virtual_ip_{}'.format(image_int)] = 'The request is reaching the Amadeus origin VIP.'
                    open_yaml(data)
                    resized = process_data(d, i, overlay, image)
                # data['virtual_ip_{}'.format(image_int)] = 'The request is reaching the Amadeus origin VIP.' if text == data['virtual_ip'] else 'The request is not reaching the Amadeus origin VIP.'
                else:
                    data['virtual_ip_{}'.format(image_int)] = 'The request is not reaching the Amadeus origin VIP.'



            elif image_int == 1 and text == 'Imperva' or text == data['web_dom_pub_ip']:

                data['xdn_{}'.format(image_int)] = 'Imperva setting found' if text == 'Imperva' else 'Not found.'
                open_yaml(data)
                resized = process_data(d, i, overlay, image)

    finally:
        if image_int == 0 and (data['virtual_ip'] == '' or data['virtual_ip'] == ' ' or data['virtual_ip'] is None):
            pass
        elif image_int == 1 and (data['web_dom_pub_ip'] is None or data['web_dom_pub_ip'] == '' or data['web_dom_pub_ip'] == ' '):
            pass
        else:
            os.remove('Images/domainTest_{}.png'.format(image_int))
            return resized
