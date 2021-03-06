import censys.ipv4 



c = censys.ipv4.CensysIPv4()

print("Kouneli Censys API Test UwU")
print("{you must have a censys account to use this}")

uinp = input("Please Enter IPV4: ")

for page in c.search(uinp, max_records=30):
	print(page)

	





