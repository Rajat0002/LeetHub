# import subprocess

# tag_name = "v1.0.0"
# commit_hash = "HEAD"
# tag_message = "Initial release"


# command = f"git tag -a {tag_name} {commit_hash} -m \"{tag_message}\""
# subprocess.run(command, shell=True, check=True)

# # Push the tag to the remote repository
# push_command = f"git push origin {tag_name}"
# subprocess.run(push_command, shell=True, check=True)



import subprocess

# Get the last existing tag in the repository
last_tag = subprocess.check_output(['git', 'describe', '--abbrev=0', '--tags']).strip().decode()

# Extract the numeric portion of the last tag
last_tag_number = int(''.join(filter(str.isdigit, last_tag)))

# Increment the tag number
new_tag_number = last_tag_number + 1

# Generate the new tag name with the incremented number
tag_name = f"v{new_tag_number}.0.0"

# Set the commit hash and tag message
commit_hash = "HEAD"
tag_message = "New release"

# Create the annotated tag using the Git command
command = f"git tag -a {tag_name} {commit_hash} -m \"{tag_message}\""
subprocess.run(command, shell=True, check=True)

# Push the tag to the remote repository
push_command = f"git push origin {tag_name}"
subprocess.run(push_command, shell=True, check=True)
