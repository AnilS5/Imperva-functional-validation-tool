"""
    For reading config file and access the key value pairs required for functional validation.
"""

# Libraries
import os

import imperva_essential
import modules as md
import imperva_new
import imperva_mss
import generateReportNew


# Function declaration for functional validation of domains.
def funcValidation():
    # Read config file.
    with open('config.yaml') as file:
        key_value = md.load(file, Loader=md.FullLoader)

    # Refresh data.yaml
    md.update_data('null_data')

    # Validate domain resolving internal VIP.
    md.grabImage(key_value['dom_test'][0], key_value['dom_test'][0].replace('.', '-') + '_0', 'part')
    if len(key_value['dom_test']) > 1:
        md.grabImage(key_value['dom_test'][1], key_value['dom_test'][1].replace('.', '-') + '_0', 'part')

    initial_ip_check = md.getVIP(key_value['dom_test'][0])
    md.virtualIP(initial_ip_check)

    # Get virtual IP for web domain.
    vip = md.getVIP(key_value['dom_test'][0])

    # Read config data.
    if key_value['fw_allwd_tr'] is not None:
        dat = md.getTaskRecordData(key_value['win_aprch_url'], key_value['func_val_tr'], key_value['fw_allwd_tr'], vip)
    else:
        dat = md.getTaskRecordData(key_value['win_aprch_url'], key_value['func_val_tr'], vip)

    # Domain accessibility checker.
    md.domainTest(key_value['web_domain'], 0)

    # Traffic flow checker.
    md.tcp_connections(key_value['rivrbed_usr'], key_value['rivrbed_url'].format(str(dat[-1]).replace('*', '')))

    # Site accessibility test and Imperva validation post host entry.
    md.hostEntry(key_value['dom_test'], key_value['web_dom_pub_ip'].split(':')[0])

    md.domainTest(key_value['web_domain'], 1)
    
    if key_value['imprv_account_type'] == 'advanced':
        imperva_new.imperva(key_value['imprv_log_usr'], key_value['imprv_url'], key_value['dom_test'])
    elif key_value['imprv_account_type'] == 'essential':
        imperva_essential.imperva(key_value['imprv_log_usr'], key_value['imprv_url'], key_value['dom_test'])
    else:
        imperva_mss.imperva(key_value['imprv_log_usr'], key_value['imprv_url'], key_value['dom_test'])
    
    # Splunk logs checker.
    md.splunk(key_value['splunk_dom'], key_value['web_domain'].split('/')[2])

    # API logs checker.
    if len(key_value['dom_test']) == 2:
       md.apiLogs(key_value['dom_test'][1])

    # Generate report.
    generateReportNew.generateReport()

    md.call_back()


# Call function.
if __name__ == '__main__':
    funcValidation()
