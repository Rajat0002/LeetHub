import subprocess

def tag_commits():
    commit_hashes = subprocess.check_output(['git', 'rev-list', '--reverse', 'HEAD']).splitlines()
    tag_counter = 1
    
    for commit_hash in commit_hashes:
        commit_hash = commit_hash.decode('utf-8')
        tag_name = 'tag_' + str(tag_counter)
        
        subprocess.run(['git', 'tag', tag_name, commit_hash])
        tag_counter += 1
        
        # Optionally, push the tags to a remote repository
        # subprocess.run(['git', 'push', 'origin', tag_name])

if __name__ == '__main__':
    tag_commits()
