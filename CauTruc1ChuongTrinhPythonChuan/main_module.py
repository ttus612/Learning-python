from code_explore import emailProcess, printMeg

def main():
    emails = ['tu@gmail.com', 'nguyenvvan@gmail.com', 'liver@gmail.com']
    for email in emails:
        userName, userDomain = emailProcess(email)
        printMeg(userName, userDomain)

if __name__ == "__main__":
    main()
