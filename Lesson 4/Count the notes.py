amount = int(input("Enter the total amount: " ))

note1000 = amount // 1000
note500 = (amount % 1000) // 500

print("1000 notes are: ",note1000)
print("500 notes are: ",note500)