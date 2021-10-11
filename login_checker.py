import string


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, sign="", username=""):
        self.username = username
        self.sign = sign

    def __str__(self):
        return 'The username contains an illegal character "{0}" at index {1}'.format(
            self.sign, self.username.find(self.sign))

class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too Long"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"

class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"



def check_input(username, password):

    UnderLine = "_"

    # Username too short
    if len(username) < 3:
        raise UsernameTooShort()

    # Username too long
    if len(username) > 16:
        raise UsernameTooLong()

    # Username doesn't contain an English letter
    if not any(char.isalpha() for char in username):
        raise UsernameContainsIllegalCharacter()

    # Username doesn't contain a number
    if not any(char.isdigit() for char in username):
        raise UsernameContainsIllegalCharacter()

    # Username doesn't contain _ sign
    if not any(char == UnderLine for char in username):
        raise UsernameContainsIllegalCharacter()

    # Username Contains illegal character except of an underline
    for char in username:
        if char in string.punctuation and char != UnderLine:
            raise UsernameContainsIllegalCharacter(char, username)

    # Password too short
    if len(password) < 8:
        raise PasswordTooShort()

    # Password too long
    if len(password) > 40:
        raise PasswordTooLong()

    # Password not include one upper case
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()

    # Password not include one lower case
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()

    # Password not include a number
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()

    # Password not include one special symbol
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

    # Valid Username & Password
    else:
        print("OK")



def main():

    while True:
        username = input("Type an username: ")
        password = input("Type a password: ")

        try:
            check_input(username, password)
            break

        except UsernameContainsIllegalCharacter as e:
            print(UsernameContainsIllegalCharacter.__str__(e))

        except UsernameTooShort as e:
            print(UsernameTooShort.__str__(e))

        except UsernameTooLong as e:
            print(UsernameTooLong.__str__(e))

        except PasswordTooShort as e:
            print(PasswordTooShort.__str__(e))

        except PasswordTooLong as e:
            print(PasswordTooLong.__str__(e))

        except PasswordMissingUppercase as e:
            print(PasswordMissingUppercase.__str__(e))

        except PasswordMissingLowercase as e:
            print(PasswordMissingLowercase.__str__(e))

        except PasswordMissingDigit as e:
            print(PasswordMissingDigit.__str__(e))

        except PasswordMissingSpecial as e:
            print(PasswordMissingSpecial.__str__(e))

        except PasswordMissingCharacter as e:
            print(PasswordMissingCharacter.__str__(e))


main()
