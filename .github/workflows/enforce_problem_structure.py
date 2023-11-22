import os
import sys
from github import Github

# get inputs from workflow
(token, repo_name, identifier, event_type) = sys.argv[1:5]

g = Github(token)
repo = g.get_repo(repo_name)

if event_type == 'pull_request':
    pr = repo.get_pull(int(identifier))
    files = pr.get_files()
else:
    commit = repo.get_commit(identifier)
    files = commit.files

# get the files changed
files = pr.get_files()

for file in files:
    if file.filename.startswith('problems/'):
        # extract the problem name from the file path
        problem_name = os.path.basename(file.filename).split('.')[0]

        # check if the problem is in the correct folder
        correct_dir = f'problems/{problem_name}/'
        if not file.filename.startswith(correct_dir):
            print(f'::error file={file.filename}, Problem {problem_name} is not in the correct folder. It should be in {correct_dir}.')
            sys.exit(1)

        # check if necessary files are present
        necessary_files = [f'{correct_dir}Readme.md']
        for necessary_file in necessary_files:
            if not any(f.filename == necessary_file for f in files):
                message = f'::missing necessary file={necessary_file}'
                message += '\n'
                message += 'Here is a README template for you to use:\n\n'
                message += '```md\n'
                message += '# Problem Link:\n\n'
                message += '[Comment]: <> (Add problem link here)\n\n'
                message += '# Intuition:\n\n'
                message += '[Comment]: <> (Add intuition here)\n\n'
                message += '# Notes:\n\n'
                message += '[Comment]: <> (Add your approach here. You can also add some points to remember)\n\n'
                message += '```'
                pr.create_issue_comment(message)
                print(message)
                sys.exit(1)