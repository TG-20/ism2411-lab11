# Reflection answers go here at the end (we'll write them last)

# ----- Exercise 1: One customer -----
print("=== Exercise 1 ===")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ----- Exercise 2: Update and add -----
print("\n=== Exercise 2 ===")

customer["phone"] = "813-555-0142"   # add a new key
print(customer)

customer["tier"] = "platinum"        # update an existing key
print(customer)

del customer["email"]                # delete a key
print(customer)

# ----- Exercise 3: Safe lookup -----
print("\n=== Exercise 3 ===")

email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    email = customer["email"]
    print("Using brackets:", email)
except KeyError:
    print("Using brackets: KeyError! 'email' is not in the dictionary")