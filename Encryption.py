"""
    This function is for encrypting credentials for the sites that requires used credentials to login.

    Libraries used:
        Cryptography fernet: For encrypting and decrypting the credentials.
        sys: System libraries for executing the system level activities.
        getpass: To store user input password for connecting authorized sites.

"""

# Libraries
import modules as md

# Global var to store user password input.
pas = ""

# Instruct usage of script.
def usage():
    """Enable if decrypt block is enabled.
    print("Usage: \n  python Encryption.py --option username\noptions:\n  1.enc for encryption.\n  2.dec for decryption "
          "(encrypted password).")
    """
    print("Usage: \n  python Encryption.py --option username\noptions:\n  1.enc for encryption.")

# To encrypt used credentials.
def enc_dec():
    if len(md.argv[:]) == 3:

        # For password encryption
        print('Enter password to encrypt: ')
        globals()['pas'] = md.gp()
        if 'TRUST_STORE_KEY' in md.environ:
            key = md.getenv('TRUST_STORE_KEY')
            my_pas = bytes(pas, 'utf-8')
            ref_key = md.cpr(key)
            enc_pas = ref_key.encrypt(my_pas)

            print('\n\nPassword for login: ', str(enc_pas).split("'")[1], '\n\n')

        else:

            key = md.cpr.generate_key()
            ref_key = md.cpr(key)
            my_pas = bytes(pas, 'utf-8')
            enc_pas = ref_key.encrypt(my_pas)

            print("\n\nSet this as TRUST_STORE_KEY system variable for future use: ", str(key).split("'")[1], '\n')
            print('Password for login: ', str(enc_pas).split("'")[1], '\n\n')

    else:
        usage()


enc_dec()
