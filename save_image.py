"""
     This function helps to save image processed by stringMatch function.

     Libraries:
      - CV2 (opencv-python module)

     Parameters:
      - resized     -->  parameter returned from stringMatch function to add overlay layer.
      - image_int   -->  this is integer passed from domainTest function to save image as DomainText_Integer.jpg.

     Usage:
      save_image(resized, image_int)
"""
# Libraries
import modules as md


def save_image(resized, image_int):

    try:
        md.imwrite('Images/domaintext_{}_img.png'.format(image_int), resized)
        md.waitKey(0)
        md.destroyAllWindows()
    except (md.error, UnboundLocalError) as e:
        if image_int == 0:
            print('The value for virtual_ip is missing in data.yaml.')
        elif image_int == 1:
            print('The value for web_dom_pub_ip is missing in data.yaml.')