import modules as md


def tcp_connections(*args):
    try:

        driver = md.driver_call(args[1])

        findElement = driver.find_element
        username = args[0]
        pas = md.getenv('RVR_PAS')
        password = str(md.dec(pas))
        wait = md.ww(driver, 120)
        wait.until(md.EC.presence_of_element_located((md.b.ID, 'loginButtonContainer')))

        findElement(md.b.ID, "usernameField").send_keys(username)
        findElement(md.b.ID, "passwordField").send_keys(password)
        del password
        findElement(md.b.ID, "loginButtonContainer").click()

        wait.until(
            md.EC.presence_of_element_located((md.b.XPATH, "//*[contains(text(), 'User Response Time (Max 1-min)')]")))
        driver.fullscreen_window()
        md.sleep(10)
        image = md.screenshot()
        image.save('Images/trafficflow_img.png')

    finally:
        md.sleep(2)
