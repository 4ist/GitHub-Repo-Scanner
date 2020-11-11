import os
from configs import config

def cloneGit(repoURL):
    # Read config variables
    targetDirectory = config.public["CLOC"]["targetDirectory"]
    removeDirectoryCommand = config.public["CLOC"]["removeDirectoryCommand"]

    # Set system command variables
    cloneCommand = f'git clone {repoURL} {targetDirectory}' # assumes git is installed
    clocCommand = f'cloc {targetDirectory}' # assumes cloc and perl are installed
    removeCommand = f'{removeDirectoryCommand} {targetDirectory}' # OS specific command to remove a directory

    # Execute system commands 
    os.popen(cloneCommand).read()
    clocOutput = os.popen(clocCommand).read()
    os.system(removeCommand)

    return clocOutput