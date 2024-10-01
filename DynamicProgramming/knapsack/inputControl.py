def get_positive_int(prompt):
    """Helper function to get a positive integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_continue_choice(prompt):
    """Helper function to get 'Y' or 'N' input for continuation."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Please enter 'Y' to continue or 'N' to stop.")