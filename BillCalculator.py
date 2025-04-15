balance = int(input("Enter Total Amount: ₹"))
total_units = int(input("Total units consumed: "))
users = int(input("Total Number of Users: "))
total = 0
user_unit =[]

for user_id in range(1, users + 1):
    
    units = int(input(f"Units consumed by User {user_id}: "))
    user_unit.append(units)
    total +=units

if(total == total_units):
    for user_id in range(users):
        units = user_unit[user_id]
        amount = (units / total_units) * balance
        print(f"Amount to be paid by User {user_id+1} is ₹{amount:.2f}")
else:
    print("invalid data!")