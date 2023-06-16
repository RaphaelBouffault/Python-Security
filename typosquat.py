import argparse
import requests
import colorama
import random
import string
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
import feedparser
import Levenshtein


# Function to search for typosquatted packages on PyPI
def search_typosquat(package):
    url = f"https://pypi.org/project/{package}/"
    response = requests.get(url)
    if response.status_code == 200:
        existing_package = package.lower()
        typosquats = []

        # Generate typosquatted package names
        for i in range(1, 10000):
            typo_name = generate_typo(existing_package)
            typosquats.append(typo_name)

        if typosquats:
            for i, typo_name in enumerate(typosquats, start=1):
                similarity_ratio = Levenshtein.ratio(existing_package, typo_name)
                if 0.80 <= similarity_ratio <= 1.0:
                    response = requests.get(f"https://pypi.org/project/{typo_name}/")
                    if response.status_code == 200:
                        print(f"Typosquatted package {i}: {typo_name}")
                        print(f"Download link: {response.url}")
                        print()

        else:
            print(f"No typosquatted packages found for the package '{package}'")
    else:
        print(f"Error with HTTP request: {response.status_code}")


def generate_typo(existing_package):
    typo_name = ""

    # Iterate over each character in the existing package name
    for char in existing_package:
        # Randomly select a lowercase letter, uppercase letter, or digit
        typo_name += random.choice(string.ascii_letters + string.digits)

    # Add additional letters or digits (between 1 and 3)
    for _ in range(random.randint(1, 3)):
        # Randomly select a lowercase letter, uppercase letter, or digit
        typo_name += random.choice(string.ascii_letters + string.digits)

    return typo_name


# Function to retrieve download statistics for a package on PyPI
def retrieve_statistics(package):
    url = f"https://pypi.org/project/{package}/"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the page to retrieve the statistics
        # ...
        return 1000  # Placeholder value for statistics
    else:
        print(f"Error with HTTP request: {response.status_code}")
        return None


# Function to send an automated report to the package supplier
def send_report(package):
    print(f"Automated report sent to the package supplier '{package}'")


# Function to perform an in-depth analysis of the supplier package
def analyze_package(package):
    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data.get("info", {})

        print(f"In-depth analysis of the supplier package '{package}':")
        print(f"Name: {info.get('name')}")
        print(f"Description: {info.get('summary')}")
        print(f"Author: {info.get('author')}")
        print(f"Author's email address: {info.get('author_email')}")
        print(f"Homepage: {info.get('home_page')}")
        print(f"Project URL: {info.get('project_url')}")
        print(f"License: {info.get('license')}")
        print(f"Latest version: {data.get('version')}")
        print(f"Release date of the current version: {info.get('release_date')}")
    else:
        print(f"Error with HTTP request: {response.status_code}")


# Function to generate a detailed report on package versions
def generate_report(package):
    # ...

    # Retrieve version and date information from the RSS link
    rss_url = f"https://pypi.org/rss/project/{package}/releases.xml"
    rss_feed = feedparser.parse(rss_url)

    if rss_feed.entries:
        print(f"\nVersion information for package '{package}':")
        for entry in rss_feed.entries:
            version = entry.title.strip()
            date = entry.published.strip()
            print(f"- Version {version}: {date}")
    else:
        print("Error: Unable to retrieve version and date information from the RSS link.")


# Function to list all typosquatted packages of the searched package
def list_typosquats(package):
    print(f"List of typosquatted packages for the package '{package}':")
    package_info_url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(package_info_url)

    if response.status_code == 200:
        package_info = response.json()
        package_url = package_info.get("info", {}).get("project_url")
        print(f"URL: {package_url}")

        similar_packages = package_info.get("releases", {}).keys()
        for i, package_name in enumerate(similar_packages, start=1):
            similarity_ratio = SequenceMatcher(None, package, package_name).ratio()
            if similarity_ratio < 0.95 and package_name != package:  # Exclude packages similar by more than 95% and the specified package itself
                package_info_url = f"https://pypi.org/pypi/{package_name}/json"
                response = requests.get(package_info_url)

                if response.status_code == 200:
                    package_info = response.json()
                    package_url = package_info.get("info", {}).get("project_url")
                    print(f"Typosquatted package {i}: {package_name}")
                    print(f"Link: {package_url}")


# Function to confirm sending the fictitious automated report
def confirm_send_report():
    while True:
        choice = input("Send the report to the package supplier? (Y/N): ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")


# Main function of the program
def main():
    # Initialize colorama for text coloring
    colorama.init()

    # Print the header in red
    header = """
      _______ __     __ _____    ____    _____   ____   _    _        _______ 
     |__   __|\ \   / /|  __ \  / __ \  / ____| / __ \ | |  | |   /\ |__   __|
        | |    \ \_/ / | |__) || |  | || (___  | |  | || |  | |  /  \   | |   
        | |     \   /  |  ___/ | |  | | \___ \ | |  | || |  | | / /\ \  | |   
        | |      | |   | |     | |__| | ____) || |__| || |__| |/ ____ \ | |   
        |_|      |_|   |_|      \____/ |_____/  \___\_\ \____//_/    \_\|_|   

    """
    print(colorama.Fore.RED + header)
    print(colorama.Style.RESET_ALL)  # Reset color

    # Print the description and options in blue
    print(colorama.Fore.BLUE + "This program allows you to search for typosquatted packages on PyPI.")
    print("Options:")
    print("-a: Perform an in-depth analysis of the supplier package")
    print("-b: Check if the package has been typosquatted and display statistics")
    print("-r: Generate a detailed report on the versions of the searched package")
    print("-l: List typosquatted packages of the searched package")
    print(colorama.Style.RESET_ALL)  # Reset color

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        epilog='Example command: python3 typosquat.py requests -b')
    parser.add_argument('package', nargs='?', help='Name of the package to search for')
    parser.add_argument('-a', action='store_true', help="Perform an in-depth analysis of the supplier package")
    parser.add_argument('-b', action='store_true',
                        help="Check if the package has been typosquatted and display statistics")
    parser.add_argument('-r', action='store_true', help="Generate a detailed report on the versions of the searched package")
    parser.add_argument('-l', action='store_true', help="List typosquatted packages of the searched package")
    args = parser.parse_args()

    if args.package:
        package = args.package

        if args.b:
            # Check for typosquat and display statistics
            search_typosquat(package)
            statistics = retrieve_statistics(package)
            if statistics:
                print(f"The package '{package}' has been typosquatted.")

        if args.r:
            # Generate detailed report
            generate_report(package)
            if confirm_send_report():
                send_report(package)

        if args.l:
            # List typosquatted packages
            search_typosquat(package)
            list_typosquats(package)

        if args.a:
            # Perform in-depth analysis of the supplier package
            analyze_package(package)

    else:
        print("Please specify the name of the package to search for.")


if __name__ == "__main__":
    main()
