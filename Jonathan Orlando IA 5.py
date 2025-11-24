# Individual Assignment 5 - Test Score Average Calculator

def get_average():
    """Gets three test scores from user and returns the calculated average."""
    # Get three test scores and convert to numbers
    score1 = float(input("Enter score for test 1: "))
    score2 = float(input("Enter score for test 2: "))
    score3 = float(input("Enter score for test 3: "))

    # Calculate average using standard formula
    average = (score1 + score2 + score3) / 3

    # Return the calculated average to main function
    return average


def check_average(average_score):
    # Determine feedback based on score ranges
    # Check if average is greater than 95
    if average_score > 95:
        print(f"Congratulations! You did great!")
    # Check if average is between 85 and 95 (inclusive)
    elif average_score >= 85:
        print(f"You did great, but did not reach the Top High.")
        # Check if average is between 70 and 84
    elif average_score >= 70:
        print(f"Good effort, but you could do better.")
    # If average is below 70
    else:
        print(f"You need to study harder next time.")


def main():
    # Calculate average by calling get_average function
    average = get_average()

    # Display the calculated average with formatting
    print(f"Your test average is: {average:.2f}")

    # Provide feedback based on the average score
    check_average(average)


# Start program execution
if __name__ == "__main__":
    main()