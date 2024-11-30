def tip_calculator():
    total_bill=float(input("Enter total bill:"))
    tip_percentage=float(input("Enter tip percentage:"))
    num_person=int(input("How many people are splitting the bill?"))

    tip=total_bill*(tip_percentage/100)
    total=tip+total_bill
    per_person=total/num_person

    print(f"\nTip Amount: ${tip:.2f}")
    print(f"Total Amount (with tip): ${total:.2f}")
    print(f"Amount Per Person: ${per_person:.2f}")

tip_calculator()
