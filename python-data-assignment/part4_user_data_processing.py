users = [
    {
        "name": "Alice",
        "scores": [85, 90, 78, 92],
        "roles": {"admin", "editor"}
    },
    {
        "name": "Bob",
        "scores": [70, 65, 80, 75],
        "roles": {"viewer"}
    },
    {
        "name": "Charlie",
        "scores": [95, 88, 92, 97],
        "roles": {"editor", "viewer"}
    },
    {
        "name": "Diana",
        "scores": [60, 72, 68, 74],
        "roles": {"admin", "viewer"}
    }
]


def calculate_average(users):
    averages = {}
    for user in users:
        scores = user["scores"]
        average = sum(scores) / len(scores)
        averages[user["name"]] = average
    return averages


def has_admin_access(roles):
    return "admin" in roles


def main():
    print("        USER DATA PROCESSING SYSTEM")

    averages = calculate_average(users)

    for user in users:
        name = user["name"]
        avg_score = averages[name]
        admin_access = has_admin_access(user["roles"])

        print(f"\n  Name          : {name}")
        print(f"  Scores        : {user['scores']}")
        print(f"  Average Score : {avg_score:.2f}")
        print(f"  Admin Access  : {'Yes' if admin_access else 'No'}")

main()
