"""
    This function is to test the domain accessibility and other network elements.

    Libraries:
     - pyautogui    --> For enabling keyboard functionalities.
     - time         --> For driver to wait till expected results to capture.

    Usage:
        domainTest(web_domain, image_int)

"""
# Libraries
import modules as md

# Save image.
def match_mark(image_int):
    try:
        image = md.stringMatch(image_int)
        md.save_image(image, image_int)
    except UnboundLocalError as e:
        print('The value for web_dom_pub_ip is missing in data.yaml.')

# Traffic check
def domainTest(*args):

    driver = md.driver_call(args[0])

    md.hotkey('f12')
    with md.hold('ctrl'):
        md.press([']', ']', ']'])

    md.sleep(5)
    with md.hold('ctrl'):
        md.press([']', ']', ']'])
    md.sleep(2)


    md.hotkey('ctrl', 'R')
    md.sleep(10)
    md.press('tab', presses=10)
    driver.fullscreen_window()
    md.sleep(2)

    md.press('down', presses=2)
    md.press('enter')

    md.hotkey('ctrl', 'shift', '-', pressess=2)


    md.sleep(5)
    image = md.screenshot()
    image.save('Images/domainTest_{}.png'.format(args[1]))
    driver.close()

    # Mark the match text.
    match_mark(args[1])











