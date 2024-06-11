"""
    This function helps to validate the URL of airline against the data present in the Imperva.
    This helps to connect Imperva management site and capture the screens for Origin, SSL certs data and WAF settings.

    Libraries used and their functionalities:
        Selenium:- To connect management site and capture screens.

    Parameters required in order to capture data and declared:
        email_id & password --> (To login Imperva site).
        url                 --> (of airline to filter and capture data).

    Usage:
        imperva(email_id, imprv_url, web_dom)

"""

# Libraries
import modules as md


# Initiate connectivity to management site and capture data required.
def imperva(email_id, imprv_url, dom_test):
    driver = md.driver_call(imprv_url)
    findElement = driver.find_element

    wait = md.ww(driver, 300)
    wait.until(md.EC.presence_of_element_located((md.b.ID, 'ssoLoginCheck')))
    findElement(md.b.ID, 'ssoLoginCheck').click()
    wait.until(md.EC.presence_of_element_located((md.b.ID, 'username')))
    findElement(md.b.ID, 'username').send_keys(email_id)
    findElement(md.b.ID, 'submitSsoLogin').click()

    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'input[placeholder="someone@example.com"]')))
    findElement(md.b.CSS_SELECTOR, 'input[placeholder="someone@example.com"]').send_keys(email_id)
    findElement(md.b.CSS_SELECTOR, 'input[value="Next"]').click()
    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'input[placeholder="Password"]')))
    pas = md.dec(md.getenv('IMPRV_PAS'))
    findElement(md.b.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys(pas)
    del pas
    findElement(md.b.CSS_SELECTOR, 'input[value="Sign in"]').click()
    # wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'button[data-testid="MainButton"]')))
    # md.sleep(10)
    driver.switch_to.default_content()

    # Added try except in case imperva under maintenance (for closing maintenance pop-ups)
    try:
        new_not = findElement(md.b.XPATH, "//button[text()='Close']")

        if new_not.is_displayed():
            new_not.click()

    except md.NoSuchElementException:
        pass

    try:
        skip_not = findElement(md.b.XPATH, "//a[text()='Skip']")
        if skip_not.is_displayed():
            skip_not.click()

    except md.NoSuchElementException:
        pass

    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'button[data-testid="MainButton"]')))
    wait.until(md.EC.frame_to_be_available_and_switch_to_it(findElement(md.b.CSS_SELECTOR, 'iframe[data-testid="iframe"]')))
    wait.until(md.EC.visibility_of_element_located((md.b.CSS_SELECTOR, 'input[type="search"]')))
    findElement(md.b.CSS_SELECTOR, 'input[type="search"]').send_keys('Hello')
    driver.switch_to.default_content()
    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'button[title="Account"]')))
    findElement(md.b.CSS_SELECTOR, 'button[title="Account"]').click()

    md.sleep(2)
    findElement(md.b.XPATH, "//*[contains(text(), 'Switch to Amadeus Essential Protection')]").click()
    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'span[title="Amadeus Essential Protection"]')))
    findElement(md.b.ID, 'currentAccountWrapper').click()
    wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'div[title="Digital for Airlines ALT"]')))
    findElement(md.b.CSS_SELECTOR, 'div[title="Digital for Airlines ALT"]').click()
    driver.fullscreen_window()

    driver.switch_to.default_content()
    for dom in dom_test:
        image_name = str(dom)
        wait.until(md.EC.presence_of_element_located((md.b.LINK_TEXT, 'Application')))
        findElement(md.b.LINK_TEXT, 'Application').click()
        wait.until(md.EC.frame_to_be_available_and_switch_to_it(0))
        wait.until(md.EC.visibility_of_element_located((md.b.CSS_SELECTOR, "input[type='search']")))
        findElement(md.b.CSS_SELECTOR, "input[type='search']").send_keys(dom)
        md.sleep(5)
        driver.save_screenshot(md.path.join('Images/', 'domain' + image_name + '.png'))
        findElement(md.b.PARTIAL_LINK_TEXT, dom).click()

        driver.switch_to.parent_frame()
        wait.until(md.EC.presence_of_element_located((md.b.PARTIAL_LINK_TEXT, 'Dashboards')))
        findElement(md.b.LINK_TEXT, 'Website Settings').click()
        md.sleep(5)
        driver.switch_to.frame(findElement(md.b.CSS_SELECTOR, 'iframe[data-testid="iframe"]'))
        driver.switch_to.frame("embedded-content")

        wait.until(md.EC.visibility_of_element_located((md.b.CSS_SELECTOR, 'select[id="dataCenterMode"]')))
        sios = 'Single Origin Server'

        init_val = md.sel(findElement(md.b.ID, 'dataCenterMode')).first_selected_option.text
        if init_val != sios:
            md.sel(findElement(md.b.ID, 'dataCenterMode')).select_by_visible_text(sios)
            # wait.until(md.EC.presence_of_element_located((md.b.CSS_SELECTOR, 'input[id="singleIpAddress"]')))
            wait.until(md.EC.presence_of_element_located((md.b.XPATH, "//*[contains(text(), ' ')]")))

            driver.save_screenshot(md.path.join('Images/', 'origin' + image_name + '.png'))

            if 'api' in dom:
                api_origin = driver.find_element(md.b.CSS_SELECTOR, 'input[id="singleIpAddress"]').get_property('value')
            else:
                web_origin = driver.find_element(md.b.CSS_SELECTOR, 'input[id="singleIpAddress"]').get_property('value')
            md.sel(findElement(md.b.ID, 'dataCenterMode')).select_by_visible_text(init_val)
        else:

            if 'api' in dom:
                api_origin = driver.find_element(md.b.CSS_SELECTOR, 'input[id="singleIpAddress"]').get_property('value')
            else:
                web_origin = driver.find_element(md.b.CSS_SELECTOR, 'input[id="singleIpAddress"]').get_property('value')
            driver.save_screenshot(md.path.join('Images/', 'origin' + image_name + '.png'))

        md.sleep(2)

        findElement(md.b.LINK_TEXT, 'WAF').click()
        wait.until(md.EC.presence_of_element_located((md.b.ID, 'ddosActivationMode')))
        ddos = driver.find_element(md.b.ID, 'ddosActivationMode').get_property('value')

        driver.switch_to.default_content()
        wait.until(md.EC.presence_of_element_located((md.b.LINK_TEXT, 'Origin and Network')))
        findElement(md.b.LINK_TEXT, 'Origin and Network').click()
        md.sleep(1)
        findElement(md.b.LINK_TEXT, 'General').click()
        wait.until(md.EC.presence_of_element_located((md.b.XPATH, "//*[contains(text(), 'impervadns.net')]")))
        if 'api' in dom:
            api_cname = findElement(md.b.XPATH, "//*[contains(text(), 'impervadns.net')]").text
        else:
            web_cname = findElement(md.b.XPATH, "//*[contains(text(), 'impervadns.net')]").text
        wait.until(md.EC.presence_of_element_located((md.b.XPATH, "//*[contains(text(), 'Domains')]")))
        content = findElement(md.b.XPATH, "//*[contains(text(), 'Domains')]")
        md.ac(driver).move_to_element(content).perform()
        driver.save_screenshot(md.path.join('Images/', 'cname' + image_name + '.png'))

        wait.until(md.EC.presence_of_element_located((md.b.PARTIAL_LINK_TEXT, 'SSL/TLS')))
        findElement(md.b.XPATH, "//*[contains(text(), 'SSL/TLS')]").click()
        md.sleep(1)
        findElement(md.b.LINK_TEXT, 'SSL Certificates').click()
        md.sleep(5)
        wait.until(md.EC.presence_of_element_located((md.b.ID, 'SslCertificatesTable')))
        findElement(md.b.XPATH, "//*[@id='certificates_table_menu']").click()
        findElement(md.b.ID, 'certificates_table_menu_view').click()
        md.sleep(5)
        driver.save_screenshot(md.path.join('Images/', 'certdata' + image_name + '_2.png'))
        cert_data_1 = findElement(md.b.XPATH, "//*[@id='cert_details_details_tab__panel']/div[1]/div[4]/span[2]").text
        cert_data_2 = findElement(md.b.XPATH, "//*[@id='cert_details_details_tab__panel']/div[1]/div[5]/span[2]").text
        cert_data_3 = findElement(md.b.XPATH, "//*[@id='cert_details_details_tab__panel']/div[1]/div[6]/span[2]").text
        cert_data = cert_data_1 + ", {}, {}".format(cert_data_2, cert_data_3)

        if 'api' in dom:
            api = [dom, api_origin, cert_data, ddos, api_cname]
            md.update_data('api', api)


        else:
            web = [dom, web_origin, cert_data, ddos, web_cname]
            md.update_data('web', web)

        md.sleep(5)
        if 'api' in dom:
            md.grabImage(dom, image_name, 'part', api_cname)
        else:
            md.grabImage(dom, image_name, 'part', web_cname)
        driver.switch_to.default_content()

    driver.delete_all_cookies()
