"""
    This function helps to decrypt encrypted credentials

    Libraries used:
        Fernet --> To encrypt and decrypt credentials.

    Usage:
        decrypt(pas)
"""

# Libraries
import modules as md


# Decrypt credentials.
def decrypt(pas):
    enc_pas = bytes(pas, 'utf-8')
    ref_key = bytes(md.getenv('TRUST_STORE_KEY'), 'utf-8')
    dec_pas = md.cpr(ref_key)
    password = str(dec_pas.decrypt(enc_pas)).split("'")[1]
    return password

