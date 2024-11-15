import subprocess
import datetime
import os

def run_git_commands(repo_path):
    # Change to the specified repository directory
    os.chdir(repo_path)

    # Define the commit message with a timestamp
    commit_message = f"csv changed and {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    try:
        # Add all changes
        table_data = None
        subprocess.run(["git", "add", "."], check=True)
        print("Added changes to staging.")

        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Committed changes with message: '{commit_message}'")

        # Push to the main branch
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Pushed changes to GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your Git repository
    repository_path = r"C:\JVCODE\DjangoGithub\djangostream"  # Use raw string for Windows path
    run_git_commands(repository_path)