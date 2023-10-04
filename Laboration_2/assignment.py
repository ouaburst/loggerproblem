#!/usr/bin/env python

""" DT179G - LAB ASSIGNMENT 2
You find the description for the assignment in Moodle, where each detail regarding requirements
are stated. Below you find the inherent code, some of which fully defined. You add implementation
for those functions which are needed:

 - authenticate_user(..)
 - format_username(..)
 - decrypt_password(..)
"""

import argparse
import sys
from typing import List

__version__ = '1.2'
__desc__ = "A simple script used to authenticate spies!"


def authenticate_user(credentials: str) -> bool:
    """Procedure for validating user credentials"""
    agents = {  # Expected credentials. MAY NOT BE MODIFIED!!
        'Chevy_Chase': 'i0J0u0j0u0J0Zys0r0{',  # cipher: bAnanASplit
        'Dan_Aykroyd': 'i0N00h00~0[$',  # cipher: bEauTy
        'John_Belushi': 'J0j0S%0V0w0L0',  # cipher: CaLzOnE
    }

    ''' PSEUDO CODE
    PARSE string value of 'credentials' into its components: username and password.
    SEND username for FORMATTING by utilizing devoted function. Store return value in 'user_tmp'.
    SEND password for decryption by utilizing devoted function. Store return value in 'pass_tmp'.
    VALIDATE that both values corresponds to expected credentials existing within dictionary.
    RETURN outcome of validation as BOOLEAN VALUE.
    '''
    credential_list = credentials.split()

    user_tmp = format_username(credential_list[:-1])

    pass_tmp = decrypt_password(credential_list[-1])

    return (user_tmp, pass_tmp) in agents.items()


def format_username(username: List[str]) -> str:
    """Procedure to format user provided username"""

    ''' PSEUDO CODE
    FORMAT first letter of given name to be UPPERCASE.
    FORMAT first letter of surname to be UPPERCASE.
    REPLACE empty space between given name and surname with UNDERSCORE '_'
    RETURN formatted username as string value.
    '''

    string_name = "_".join(username)

    capitalized_name = string_name.title()

    return capitalized_name


def decrypt_password(password: str) -> str:
    """Procedure used to decrypt user provided password"""
    rot7, rot9 = 7, 9  # Rotation values. MAY NOT BE MODIFIED!!
    vowels = 'AEIOUaeiou'  # MAY NOT BE MODIFIED!!
    decrypted = str()

    ''' PSEUDO CODE
    REPEAT {
        DETERMINE if char IS VOWEL.
        DETERMINE ROTATION KEY to use.
        DETERMINE decryption value
        ADD decrypted value to decrypted string
    }
    RETURN decrypted string value
    '''

    def rotate_char(rot):
        """Nested function used to rotate characters"""
        char_value = ord(char) + rot

        decrypted_char = chr(char_value) if char_value < 127 else chr((char_value - 127) + 33)

        return decrypted_char

    for i, char in enumerate(password):
        if char in vowels:
            if i % 2 == 0:
                decrypted = decrypted + "0" + rotate_char(rot7) + "0"
            else:
                decrypted = decrypted + "0" + rotate_char(rot9) + "0"
        elif i % 2 == 0:
            decrypted = decrypted + rotate_char(rot7)
        else:
            decrypted = decrypted + rotate_char(rot9)

    return decrypted


def main():
    """The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    epilog = "DT0179G Assignment 2 v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('credentials', metavar='credentials', type=str,
                        help="Username and password as string value")

    args = parser.parse_args()

    if not authenticate_user(args.credentials):
        print("Authentication failed. Program exits...")
        sys.exit()

    print("Authentication successful. User may now access the system!")


if __name__ == "__main__":
    main()
