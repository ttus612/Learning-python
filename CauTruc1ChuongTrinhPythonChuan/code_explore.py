def emailProcess(email):
    email_username = email[0: email.index("@")]
    email_domain = email[email.index("@") + 1:]
    # print(f"Your email username is {email_username}")
    return [email_username, email_domain]

def printMeg(emailUserName, emailDomain):
    print(f"Your email username is {emailUserName}")
    print(f"Your email domain is {emailDomain}")

def main():
    email =  input("Press Enter your email address: ").strip()
    email_username, email_domain =  emailProcess(email)
    printMeg(email_username, email_domain)

if __name__ == "__main__":
    main()  