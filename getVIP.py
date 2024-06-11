"""
    This function is for extracting virtual IP assigned to web_domain.

    Libraries:
     - Subprocess --> Popen extracting virtual IP of origin CNAME.

    Parameters:
    - web_domain.

    Usage:
     getVIP(web_domain)
"""

# Libraries
import modules as md

# Extract virtual IP of CNAME origin address mapped to web domain.
def getVIP(*args):
    ip = md.Popen("dig +noall +answer {} -n 2".format(args[0]), stdout=md.PIPE, stderr=None, shell=True)
    output = ip.communicate()
    return output[0].split()[-1].decode("utf-8")

