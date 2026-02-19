contacts = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098"
}


print("=" * 40)
print("        CONTACT BOOK")
print("=" * 40)
print(f"{'Name':<15} {'Phone Number'}")
print("-" * 40)

for name, phone in contacts.items():
    print(f"{name:<15} {phone}")

print("-" * 40)

search_name = input("\nEnter a name to search: ")


if search_name in contacts:
    print(f"\n✅ {search_name}'s Phone Number: {contacts[search_name]}")
else:
    print("\n❌ Contact not found")
