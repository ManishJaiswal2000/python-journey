# Day 5: Mini-Project Day, a Bill Calculator

customer_name = input("What is your name ? ")
price = int(input("Please enter the item price : "))
quantity = int(input("Please enter the quantity number : "))

subtotal = price * quantity
gst = subtotal * 0.18

final_total = subtotal + gst

print(f"Customer : {customer_name}")
print(f"Subtotal : {subtotal}")
print(f"GST (18%) : {gst:.2f}")
print(f"Total : {final_total:.2f}")




