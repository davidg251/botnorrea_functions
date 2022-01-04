import os
import subprocess
import json

commit_hash   = os.environ['GITHUB_SHA']
changed_files_command = f'git diff-tree --no-commit-id --name-only -r {commit_hash}'

def git_diff_tree():
    return subprocess.run(
        changed_files_command.split(" "),
        capture_output=True
    ).stdout.decode("utf-8")

def main():
    files_paths  = git_diff_tree().split("\n")
    files_paths.pop()
    changed_folders = set( map(lambda elem: elem.split("/")[0], files_paths) )
    changed_folders.discard('.github')
    return list(changed_folders)

print(json.dumps(main()))