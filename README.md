# github-reattribute
Reattribute commit from different emails to one user/email address

If you have projects on your github that contain commits you made with another email address, this project is for you!

It allows you to standardize your work to rewrite all the old commits of your old work so that they are saved with your new email address.

Warning : Don't take credit for someone else's work. Only use this project to standardize your own commits!
Warning bis : This project is in beta, I am not responsible if data is lost during the conversion.

# How to use it
1. Clone this project
2. Give your .env file the right values
3. Execute the user recuperation script with `python3 list-all-users.py`
4. Modify the file `email.list` to match with your new email address/name
5. Once your ABSOLUTELY SURE of what you are doing, execute the script `python3 reattribute.py`
6. Wait for the script to finish...
7. Wait for the script to finish...
8. Wait for the script to finish...
9. Wait... (it can take a while)
10. Enjoy your new github, with all your commits under the same email address!