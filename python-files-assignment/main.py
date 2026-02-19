def read_numbers(file_path):
    numbers = []

    with open(file_path, "r") as file:
        for line in file:
            stripped_line = line.strip()

            # Skip blank lines
            if stripped_line == "":
                continue

            # Convert to integer (raises ValueError on bad data)
            number = int(stripped_line)
            numbers.append(number)

    return numbers


def compute_statistics(numbers):
    count = len(numbers)
    total = sum(numbers)
    average = total / count if count > 0 else 0

    return {
        "count": count,
        "sum": total,
        "average": round(average, 2),
    }


def write_log(log_path, messages):
    with open(log_path, "a") as log_file:
        for message in messages:
            log_file.write(message + "\n")
        # Add a blank separator line between runs
        log_file.write("\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"
    log_messages = []

    try:
        # --- Step 1: Read numbers ---
        numbers = read_numbers(input_file)
        log_messages.append("File opened successfully")
        log_messages.append(f"Read {len(numbers)} numbers")
        print(f"Read {len(numbers)} numbers from {input_file}")

        # --- Step 2: Compute statistics ---
        stats = compute_statistics(numbers)
        log_messages.append(f"Sum: {stats['sum']}")
        log_messages.append(f"Average: {stats['average']}")
        log_messages.append("Computation completed")
        print(f"Count  : {stats['count']}")
        print(f"Sum    : {stats['sum']}")
        print(f"Average: {stats['average']}")

        # --- Step 3: Log results ---
        log_messages.append("Processing completed")
        write_log(log_file, log_messages)
        print(f"\nResults logged to {log_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        print("Please make sure numbers.txt exists in the same directory.")

    except ValueError as error:
        print(f"Error: Invalid number format — {error}")
        print("Please make sure every line in numbers.txt is a valid integer.")


if __name__ == "__main__":
    main()
