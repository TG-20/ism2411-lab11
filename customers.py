# Reflection 1:
# I would use .get() when a missing key is normal, like an optional phone
# number or email on a customer record, because the program can use a default
# and keep running. I would use bracket notation when the key must exist, like
# a customer ID, because a KeyError shows me right away that the data is bad.
# My rule of thumb is .get() for optional data and brackets for required data.
#
# Reflection 2:
# Exercise 8 reminds me of a SUMIF or a PivotTable that totals sales by region.
# The Python version is more useful for large datasets because it can handle
# more rows than Excel comfortably can. It is also repeatable, so I can run the
# same script on next month's file instead of rebuilding the summary by hand.
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


# ----- Exercise 4: Iterate -----
print("\n=== Exercise 4 ===")

for key, value in customer.items():
    print(f"{key}: {value}")

print("--- without .items() ---")
for key in customer:
    print(key)
# Without .items(), the loop only gives the KEYS (name, tier, ...),
# not the values. .items() gives both the key and the value together.

# ----- Exercise 5: Lookup table -----
print("\n=== Exercise 5 ===")

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")


# ----- Exercise 6: List of dicts -----
print("\n=== Exercise 6 ===")

customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carol", "tier": "platinum"},
    {"name": "David", "tier": "bronze"},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount = purchase * rate
    print(f"{c['name']} ({c['tier']}): ${discount:.2f} off a ${purchase} purchase")

# ----- Exercise 7: Nested catalog -----
print("\n=== Exercise 7 ===")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} — only {details['stock']} left")


# ----- Exercise 8: Sales by region -----
print("\n=== Exercise 8 ===")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    {"region": "West", "amount": 400},
    {"region": "North", "amount": 250},
]

region_totals = {}
for t in transactions:
    region = t["region"]
    region_totals[region] = region_totals.get(region, 0) + t["amount"]

for region in sorted(region_totals):
    print(f"{region}: ${region_totals[region]}")