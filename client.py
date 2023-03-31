import socket
import math

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# Display the menu to the client
menu = {
    "pasta": 150,
    "pizza": 300,
    "sandwich": 80,
    "burger": 120,
    "salad": 70,
    "taco": 200,
    "burrito": 250,
    "brownie": 100,
    "rice bowl": 180
}
menu_display = "Menu:\n"
for item, cost in menu.items():
    menu_display += f"{item} (₹{cost})\n"
print(menu_display)

# Prompt the client to place an order
order = input("Enter your order (separate items by commas): ")

# Prompt the client for OTP
otp = input("Enter OTP: ")

# Prompt the client for their location
location = input("Enter your Address: ")

# Send the order, otp, and location to the server
client_socket.send(order.encode())
client_socket.send(otp.encode())
client_socket.send(location.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()
print(response)

# Close the connection
client_socket.close()