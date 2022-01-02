import os
import subprocess

#commit_hash=os.environ['EPA']
commit_hash='bb51c726'
GIT_GET_FILES = f'git diff-tree --no-commit-id --name-only -r {commit_hash}'

print(GIT_GET_FILES)

files_paths = subprocess.Popen(GIT_GET_FILES, shell=True, stdout=subprocess.PIPE).stdout

print(files_paths.read())
print(type(files_paths.read()))
output = files_paths.read().decode()
print(output)
print(output.split('\n'))