# List all email in a file, and associate them with a name

from utils import *

FILE = 'emails.list'

if __name__ == '__main__':


    users = list_all_users()

    # Write all users in a file
    with open(FILE, 'w') as f:
        f.write(HEADER_HELP)
        f.write("\n\n--> Delete this line before using the \"reatribute.py\" script\n\n")
        # Sort users by email
        for user in sorted(users, key=lambda user: user.email):
            f.write(str(user))
            f.write("\n\n")

