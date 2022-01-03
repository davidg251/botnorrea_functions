import os
import subprocess

commit_hash   = os.environ['GITHUB_SHA']
changed_files_command = f'git diff-tree --no-commit-id --name-only -r {commit_hash}'
changed_files_output = subprocess.run(changed_files_command.split(" "), capture_output=True).stdout
files_paths  = changed_files_output.decode("utf-8").split("\n")
files_paths.pop()
changed_folders = set(map(lambda elem: elem.split("/")[0], files_paths))
print(changed_folders)
