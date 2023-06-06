import subprocess

tag_name = "v1.0.0"
commit_hash = "HEAD"
tag_message = "Initial release"


command = f"git tag -a {tag_name} {commit_hash} -m \"{tag_message}\""
subprocess.run(command, shell=True, check=True)

# Push the tag to the remote repository
push_command = f"git push origin {tag_name}"
subprocess.run(push_command, shell=True, check=True)
