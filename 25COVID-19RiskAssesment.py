age = input('Are you a cigarette addict older than 75 years old? (yes/no) ')
age = age.lower()  # YES or Yes or yes doesnt matter.
chronic = input('Do you have a severe chronic disease?(yes/no) ')
chronic = chronic.lower()
immune = input('Is your immune system too weak?(yes/no) ')
immune = immune.lower()
risk = bool(age=="yes" or chronic=="yes"  or immune=="yes" )

if risk:
    print('You are in risky group.')
else:
    print('You are not in risky group.')