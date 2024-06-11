"""
    This method using soup API to get the title and origin IP address for the domain of airline.

    Libraries used and their functionalities:
        Beautiful Soup API: To scrap site data.
        Python regular expression (re):- To extract data required out of soup API data.

    Mandatory parameters in order to extract data:
        TR1  --> (Created for functional validation of airline).
        TR2  --> (Created for allowing FW permissions for airline url).

    Usage:
        getTaskRecordData(win@proach_url, TR1, TR2, vip)

"""
import re

import modules as md
from genData import genData

# List to store the title and IP address.
value = list()

# To extract public and virtual IPs.
def soup_data(sodata):
    for string in sodata.text.split():
        if md.findall('\d+[.]\d+[.]\d+$', string):
            if string not in value:
                return string

# Extract task records data.
def getTaskRecordData(*args):
    try:
        for i in range(len(args)):
            if i == 0:
                pass

            else:
                res = md.req(args[0] % args[i])

                soup = md.bs(res.content, features="html.parser")

                if i == 1:
                    title = str(soup.find('title'))
                    value.append(title.lstrip('<title>').rstrip('</title>'))
                    ip = soup_data(soup)
                    value.append(ip)

                elif i == 2:
                    if str(args[2]).isdigit():
                        ip = soup_data(soup)

                        if args[-1] == ip:
                            value.append(ip)
                        else:
                            value.append(args[-1])

                    else:
                        value.append(args[-1])

    # Add generated yaml data to data.yaml and return value to tcp_connections function for traffic check.
    finally:
        genData(value)
        return value