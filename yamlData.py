import modules as md


def yamlData():

    keys = {'web': ['web_domain', 'web_origin', 'cert_data_web', 'ddos_web', 'cname_web'],
            'api': ['api_domain', 'api_origin', 'cert_data_api', 'ddos_api', 'cname_api'],
            'misc': ['tr_title', 'web_dom_pub_ip', 'virtual_ip', 'virtual_ip_0', 'splunk_url', 'xdn_0',
                     'xdn_1', 'initial_vip_check', 'api_log']}
    """
    keys = {'web': ['web_domain', 'web_origin', 'ddos_web', 'cname_web'],
            'api': ['api_domain', 'api_origin', 'ddos_api', 'cname_api'],
            'misc': ['tr_title', 'web_dom_pub_ip', 'virtual_ip', 'virtual_ip_0', 'splunk_url', 'xdn_0',
                     'xdn_1', 'initial_vip_check', 'api_log']}
    """
    return keys
