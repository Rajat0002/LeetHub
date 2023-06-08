# import subprocess

# tag_name = "v2.0.0"
# commit_hash = "HEAD"
# tag_message = "Initial release"


# command = f"git tag -a {tag_name} {commit_hash} -m \"{tag_message}\""
# subprocess.run(command, shell=True, check=True)

# # Push the tag to the remote repository
# push_command = f"git push origin {tag_name}"
# subprocess.run(push_command, shell=True, check=True)


import subprocess

# Get the latest tag
last_tag = subprocess.check_output(['git', 'describe', '--abbrev=0', '--tags']).strip().decode()

# Remove the leading 'v' from the tag
tag_without_v = last_tag[1:]

# Split the tag into major, minor, and patch components
major, minor, patch = tag_without_v.split(".")

# Increment the major component
new_major = int(major) + 1

# Construct the new tag with the 'v' prefix
new_tag = f"v{new_major}.0.0"

# Define the commit hash and tag message
commit_hash = "HEAD"
tag_message = "New release"

# Create the tag
command = f"git tag -a {new_tag} {commit_hash} -m \"{tag_message}\""
subprocess.run(command, shell=True, check=True)

# Push the tag to the remote repository
push_command = f"git push origin {new_tag}"
subprocess.run(push_command, shell=True, check=True)
