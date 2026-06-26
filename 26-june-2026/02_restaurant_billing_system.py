# ----------------------------
# MSQ RESTAURANT BILLING SYSTEM
# ----------------------------

item = input("Enter Item Name      : ")
category = input("Enter Category       : ")
price = float(input("Enter Price          : "))
quantity = int(input("Enter Quantity       : "))
gst_percentage = float(input("Enter GST (%)        : "))
discount_percentage = float(input("Enter Discount (%)   : "))

subtotal = price * quantity

gst_amount = subtotal * (gst_percentage / 100)

discount_amount = subtotal * (discount_percentage / 100)

grand_total = subtotal + gst_amount - discount_amount

print("\n------------------------------------")
print("      MSQ RESTAURANT BILL")
print("------------------------------------")

print("Item             :", item)
print("Category         :", category)
print("Price            :", price)
print("Quantity         :", quantity)

print("------------------------------------")


print(f"Subtotal          : ₹{subtotal:.2f}")
print(f"GST Amount        : ₹{gst_amount:.2f}")
print(f"Discount Amount   : ₹{discount_amount:.2f}")

print("------------------------------------")

print(f"Grand Total : ₹{grand_total:.2f}")

print("------------------------------------")
print("Thank You! Visit Again")
print("------------------------------------")
