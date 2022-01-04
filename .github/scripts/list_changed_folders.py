import os
import subprocess

commit_hash   = os.environ['GITHUB_SHA']
changed_files_command = f'git diff-tree --no-commit-id --name-only -r {commit_hash}'

def git_diff_tree():
    return subprocess.run(
        changed_files_command.split(" "),
        capture_output=True
    ).stdout.decode("utf-8")

def main():
    files_paths  = git_diff_tree().split("\n")
    print(files_paths)
    files_paths.pop()
    changed_folders = set( map(lambda elem: elem.split("/")[0], files_paths) )
    changed_folders.discard('.github')
    return changed_folders

print(main())