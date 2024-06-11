import modules as md

def splunk(domain, web_domain):

    driver = md.driver_call(domain)
    wait = md.ww(driver, 300)
    findElement = driver.find_element
    findElement(md.b.ID, 'username').send_keys('username')
    password = md.dec(md.getenv('SPLUNK_PASS'))
    findElement(md.b.ID, 'password').send_keys(password)
    del password
    findElement(md.b.CSS_SELECTOR, 'input[type="submit"]').click()
    wait.until(md.EC.presence_of_element_located((md.b.CLASS_NAME, "ace_text-input")))
    md.sleep(5)
    findElement(md.b.CLASS_NAME, "ace_text-input").send_keys('index="*-aere-*" source="*" PodName=* Access_Host=%s' % web_domain)
    md.press('Enter')
    md.sleep(20)
    get_url = driver.current_url
    with open('data.yaml', 'r') as file:
        data = md.load(file, Loader=md.FullLoader)
        data['splunk_url'] = get_url

    with open('data.yaml', 'w') as check:
        md.dump(data, check)

