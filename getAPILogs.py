import modules as md


def apiLogs(*args):
    api_domain = args[0]
    driver = md.driver_call('https://internal.loggingfacility.xxx.com/#/log-search///')
    wait = md.ww(driver, 300)
    findElement = driver.find_element

    findElement(md.b.NAME, 'paccount').send_keys('username')
    password = md.dec(md.getenv('SPLUNK_PASS'))
    findElement(md.b.NAME, 'password').send_keys(password)
    md.press('enter')
    wait.until(md.EC.presence_of_element_located((md.b.XPATH, '//*[@id="phase"]//*/span[2]')))
    findElement(md.b.XPATH, '//*[@id="phase"]//*/span[2]').click()
    md.write('PRD')
    md.press('enter')
    findElement(md.b.XPATH, '//*[@id="app"]//*/span').click()
    md.write('All')
    md.sleep(2)
    md.press('enter')
    md.sleep(2)
    findElement(md.b.ID, 'timerange').click()
    md.press('backspace')
    md.write('5')

    findElement(md.b.XPATH, '//input[@placeholder="Type a pattern ..."]').send_keys(args)
    md.press('enter')
    wait.until(md.EC.presence_of_element_located((md.b.CLASS_NAME, 'message-count')))
    md.sleep(20)
    check = findElement(md.b.CLASS_NAME, 'message-count').text
    if check != 'Msgs: 0':
        get_url = driver.current_url
        read_yaml = md.readYaml('data.yaml')
        read_yaml['api_log'] = get_url
        md.writeYaml(read_yaml)
        # print(get_url)
        # if findElement(md.b.XPATH, "//*[contains(text(), ' ')]").text:
        #     print('IP found.')
        # else:
        #     print('Not found.')
    else:
        apiLogs(api_domain)
