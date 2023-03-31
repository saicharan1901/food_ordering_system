import socket

# Menu Set
menu = {
    "pasta": 200,
    "pizza": 350,
    "sandwich": 130,
    "burger": 170,
    "salad": 120,
    "taco": 250,
    "burrito": 300,
    "brownie": 150,
    "rice bowl": 230
}

def process_order(order):
    # Code to process the order
    total_cost = 0
    order_items = order.split(",")
    for item in order_items:
        item = item.strip()
        if item in menu:
            total_cost += menu[item]

    # Add 10% discount for a bill over 600
    if total_cost > 600:
        discount_amount = total_cost * 0.1
        total_cost *= 0.9
        return total_cost, discount_amount

    return total_cost, 0

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)

print("Server started. Waiting for connections...")

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    # Receive the order from the client
    order = client_socket.recv(1024).decode()
    otp = client_socket.recv(1024).decode()
    location = client_socket.recv(1024).decode()

    print("Received order:", order)
    print("Entered OTP:", otp)
    print("Delivery Location:", location)

    # Process the order and include discount message and updated price in response
    total_cost, discount_amount = process_order(order)
    if discount_amount > 0:
        response = f"Your order costs ₹{total_cost:.2f} after a discount of ₹{discount_amount:.2f} has been applied."
    else:
        response = f"Your order costs ₹{total_cost:.2f}."
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
