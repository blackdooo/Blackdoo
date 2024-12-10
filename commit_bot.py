import os
import random
import datetime
from subprocess import call

# Generate random number of commits per day
def make_commits():
    for _ in range(random.randint(1, 5)):  # Random number of commits
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("dummy.txt", "a") as file:
            file.write(f"Commit made at {date}\n")  # Add dummy text
        call(["git", "add", "dummy.txt"])
        call(["git", "commit", "-m", f"Random commit at {date}"])

if __name__ == "__main__":
    make_commits()