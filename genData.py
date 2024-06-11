"""
    This function enables us to write data to data.yaml.

    Libraries:
     - yaml --> To read and write yaml data.

    Parameters:
     - WIN@proach URL (win@proach_url), web_dom_pub_ip, VIP.

    Usage:
     - genData(win@proach_url, web_dom_pub_ip, virtual_ip)
"""

# Libraries
import re

import modules as md

# To generate data and dump data to data.yaml.
def genData(*args):

    with open('data.yaml', 'r') as file:
        title = md.load(file, Loader=md.FullLoader)

    for i in args[0]:
        if i.startswith('TR'):
            tr_ref = re.findall('\d+', i)
            ref_tr = i.replace(tr_ref[0], '[{0}|https://aproach.muc.xxx.net/NotesLink/nl?RNID={0}]'.format(tr_ref[0]))
            title['tr_title'] = ref_tr
    title['web_dom_pub_ip'] = args[0][1] + ':443'
    title['virtual_ip'] = args[0][-1] + ':443'

    with open('data.yaml', 'w') as check:
        md.dump(title, check)


