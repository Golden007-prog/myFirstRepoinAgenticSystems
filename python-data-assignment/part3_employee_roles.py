employee = (101, "John Doe", "Engineering")

roles = {"admin", "editor", "viewer"}


print("      EMPLOYEE ROLE CHECKER")
print(f"  Employee ID     : {employee[0]}")
print(f"  Employee Name   : {employee[1]}")
print(f"  Department      : {employee[2]}")

print(f"  Assigned Roles  : {roles}")

has_admin = "admin" in roles

print(f"\n  Admin Access    : {'Yes' if has_admin else 'No'}")
