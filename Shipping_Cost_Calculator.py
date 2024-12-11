#Shipping cost calculator

##input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("ENter the shipping rate per kilogram: "))


## calculate the shipping cost
shipping_cost = weight * rate

##ddisplay the result
print(f"Shiiping Cost: {shipping_cost} USD")
