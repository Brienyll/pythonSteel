print("How many miles did you run today?")
miles = input()
kms = float(miles)*1.60934
kms = round(kms, 2)
#print("That is equal to " + str(kms) + " miles")
print(f"Your { miles }mi is equal to { kms }km")
