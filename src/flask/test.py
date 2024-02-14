import subprocess

out = subprocess.run("node --version", capture_output=True)

print(out.stdout)