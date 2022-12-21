def main():
    print("Welcome to Asare's Email Slicer\n")
    
    email_input = input("Type in your Email:")
    
    (username, Domain) = email_input.split("@")
    (Domain, extension) = Domain.split(".")
    
    print("\naUsername:", username)
    print("Domain:",Domain)
    print("Extension:", extension)
main()    
    
    