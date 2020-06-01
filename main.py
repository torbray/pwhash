import hashlib as hl
import os


def encrypt(pwd, salted):
    if salted is None:
        salted = os.urandom(16)
    hashed = hl.pbkdf2_hmac('sha256', pwd.encode(), salted, 100000)
    return hashed, salted


class UserLogin:

    def __init__(self, username, pwd):
        self.username = username
        self.hash, self.salt = encrypt(pwd, None)


def main():
    list_of_users = [UserLogin('torbray', 'password'),
                     UserLogin('JohnDoe', 'password'),
                     UserLogin('JaneDoe', 'hunter2'),
                     UserLogin('JohnCena', '#password')]

    # Username validation
    while True:
        test_user = input('Enter a username >> ')
        if test_user.lower() == 'exit':
            return False
        elif len(test_user) < 4 or len(test_user) > 16:
            print('Invalid length! A username must be between 4 and 16 characters.\n')
            continue
        break

    # Password validation
    while True:
        test_pwd = input('Enter a password >> ')
        if test_pwd.lower() == 'exit':
            return False
        elif len(test_pwd) < 8 or len(test_pwd) > 16:
            print('Invalid length! A password must be between 8 and 16 characters.\n')
            continue
        break

    # Check username against existing database
    valid, session = False, None
    for user in list_of_users:
        if user.username == test_user:

            # Checks password hash against inputted hash
            if user.hash == encrypt(test_pwd, user.salt)[0]:
                valid = True
                session = user
                break

    # Creates "session"
    if valid:
        print(f'Successful login\nWelcome {session.username}\n')
    else:
        print('Invalid username or password\n')
    return True


if __name__ == '__main__':
    running = True
    while running:
        running = main()
