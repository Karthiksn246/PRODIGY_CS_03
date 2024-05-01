import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on defined criteria.

    Args:
    password (str): The password to be assessed.

    Returns:
    str: Feedback on the strength of the password.
    """
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_character_criteria = bool(re.search(r'[!@#$%^&*()_+{}|:"<>?]', password))

    # Calculate overall strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_character_criteria])

    # Provide feedback based on strength score
    if strength_score == 5:
        return "Very Strong"
    elif strength_score >= 3:
        return "Strong"
    elif strength_score >= 2:
        return "Moderate"
    elif strength_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def continue_assessment():
    """
    Ask the user if they want to continue assessing passwords.

    Returns:
    bool: True if the user wants to continue, False otherwise.
    """
    response = input("Do you want to continue assessing passwords? (yes/no): ").lower()
    return response == "yes"

# Main program
while True:
    password = input("Enter a password to assess its strength: ")
    strength_feedback = assess_password_strength(password)
    print(f"Strength of the password '{password}': {strength_feedback}")

    if not continue_assessment():
        break
