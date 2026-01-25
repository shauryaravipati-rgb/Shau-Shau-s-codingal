m_cause = input("Do you have a medical cause?")
attend = int(input("Enter your attendance of the student "))

if m_cause == "Y":
    print("Allowed")
else:
    if attend>=75:
        print("Allowed")
    else:
        print("Not allowed")

