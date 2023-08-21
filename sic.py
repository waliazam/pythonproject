p_amount = int(input("Enter Principal  Amount: "))

roi = int(input("Enter rate of interest : "))

time_p = int(input("Enter time period: "))

si = (p_amount * roi * time_p) / 100

print("Simple Interest is : " + str(si))