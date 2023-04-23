import subprocess
import sys

prefix = 'auto-gpt/'
issue_number = sys.argv[1]
branch_name = prefix + issue_number

subprocess.run(['git', 'checkout', '-b', branch_name])
