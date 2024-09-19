import re
import string
import random
import math
import zxcvbn
import os
import configparser
from colorama import init, Fore, Style
init()

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the configuration values
blacklist_check = config.getboolean('password_checker', 'blacklist_check')
blacklist_file = config.get('password_checker', 'blacklist_file')
blacklist_file = os.path.join('files', blacklist_file)

# Function to check the strength score
def password_strength(password):
    """
    Evaluates the strength of a password based on the following criteria:
    1. Length: at least 12 characters
    2. Uppercase letters: at least 1
    3. Lowercase letters: at least 1
    4. Numbers: at least 1
    5. Special characters: at least 1
    Returns a score from 0 to 5, where 5 is the strongest password.
    """
    score = 0

    # Check length
    if len(password) >= 12:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check numbers
    if re.search(r"\d", password):
        score += 1

    # Check special characters
    if not password.isalnum():
        score += 1

    return score

#  Function for giving score message
def password_strength_message(score):
    """
    Returns a message based on the password strength score.
    """
    if score == 5:
        return "Strong password!"
    elif score >= 3:
        return "Medium password. Consider adding more complexity."
    else:
        return "Weak password. Please use a stronger password."

# Function to give recommendations
def password_recommendations(password, score):
    """
    Returns recommendations on how to improve the password based on the score.
    """
    recommendations = []

    if score < 5:
        if len(password) < 12:
            recommendations.append("Increase the length of your password to at least 12 characters.")
        if not re.search(r"[A-Z]", password):
            recommendations.append("Add at least one uppercase letter to your password.")
        if not re.search(r"[a-z]", password):
            recommendations.append("Add at least one lowercase letter to your password.")
        if not re.search(r"\d", password):
            recommendations.append("Add at least one number to your password.")
        if password.isalnum():
            recommendations.append("Add at least one special character to your password.")

    return recommendations

# Estimate cracking time
def password_cracking_time_estimation(password):
    """
    Estimates the time it would take for a hacker to crack the password using various password cracking techniques.
    Returns a string indicating the estimated cracking times.
    """
    # Create a zxcvbn object with the password
    result = zxcvbn.zxcvbn(password)

    # Extract the cracking time estimates
    crack_time_display = result.get("crack_times_display")
    if crack_time_display:
        cracking_times = []
        for scenario, time in crack_time_display.items():
            cracking_times.append(f"{scenario.capitalize()}: {time}")
        return "\n".join(cracking_times)
    else:
        return "Unknown"

# Checks if the password is in rockyou.txt
def password_blacklisting(password):
    """
    Checks the password against a list of known weak or compromised passwords.
    Returns a boolean indicating whether the password is blacklisted.
    """
    if blacklist_check:
        try:
            with open(blacklist_file, 'r', encoding='utf-8', errors='replace') as f:
                blacklist = [line.strip() for line in f.readlines()]
            return password in blacklist
        except FileNotFoundError:
            # Handling file not found
            return None
    else:
        print("Blacklist check is disabled.")
        return False

# Main code
def main():
    # Enter password
    while True:
        password = input("Enter a password (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console when entering a password
        # Prints
        print("\n" + "="*40)
        print(Fore.CYAN + "Password Strength Evaluation" + Style.RESET_ALL)
        print("="*40 + "\n")
        print("Password: " + password + Style.RESET_ALL)
        print()
        score = password_strength(password)
        print(Fore.GREEN + f"Password strength: {score}/5" + Style.RESET_ALL)
        print(Fore.YELLOW + password_strength_message(score) + Style.RESET_ALL)
        print()
        recommendations = password_recommendations(password, score)
        if recommendations:
            print(Fore.GREEN + "Recommendations:" + Style.RESET_ALL)
            for rec in recommendations:
                print(Fore.BLUE + f"- {rec}" + Style.RESET_ALL)
            print()
        print(Fore.GREEN + "Password Cracking Time Estimation: " + Style.RESET_ALL)
        cracking_time = password_cracking_time_estimation(password)
        print(Fore.MAGENTA + cracking_time + Style.RESET_ALL)
        print()
        if blacklist_check:
            print(Fore.GREEN + "Password Blacklisting: " + Style.RESET_ALL)
            print("Checking if password is blacklisted. This may take several seconds... " + Style.RESET_ALL)
            result = password_blacklisting(password)
            if result is None:
                print(Fore.RED + "Error: Blacklist file not found." + Style.RESET_ALL)
            elif result:
                print(Fore.RED + "WARNING: This password is blacklisted. Please choose a different password." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "Password is not blacklisted." + Style.RESET_ALL)
            print("\n" + "="*40 + "\n")
        else:
            print(Fore.GREEN + "Password Blacklisting: Disabled" + Style.RESET_ALL)
            print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
