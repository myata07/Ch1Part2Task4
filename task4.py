hours = int(input("Enter your hour: "))
minutes = int(input("Enter your minutes: "))
seconds = int(input("Enter your seconds: ")) 
hours_ = int(input("Enter your hours_: ")) 
minutes_ = int(input("Enter your minutes_: ")) 
seconds_ = int(input("Enter your seconds_: "))
result = minutes * 60 + hours * 3600 + seconds

result_ = minutes_ * 60 + hours_ * 3600 + seconds_
print(result - result_)