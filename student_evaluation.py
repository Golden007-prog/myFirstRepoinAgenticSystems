def greet_student(name):
    """Takes a student name and returns a greeting string."""
    return f"Hello, {name}"


def calculate_scores(scores_list):
    """Takes a list of scores and returns number of subjects and average score."""
    num_subjects = len(scores_list)
    average = sum(scores_list) / num_subjects
    return num_subjects, average


def get_result(average):
    """Returns 'Pass' if average >= 50, otherwise 'Fail'."""
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    # Ask for student name
    name = input("Enter student name: ")

    # Ask for scores (space-separated)
    scores_input = input("Enter scores (space-separated): ")
    scores_list = [float(score) for score in scores_input.split()]

    # Call all functions
    greeting = greet_student(name)
    num_subjects, average = calculate_scores(scores_list)
    result = get_result(average)

    # Print formatted output
    print(greeting)
    print(f"Subjects: {num_subjects}")
    print(f"Average Score: {average}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
