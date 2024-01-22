from validator_collection import validators,errors

def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(email):
    try:
        address = validators.email(email)
        if address:
            return "Valid"
        else:
            raise errors.InvalidEmailError
    except errors.InvalidEmailError:
        return ("Invalid")

if __name__ == "__main__":
    main()
