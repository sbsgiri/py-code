from subprocess import call, check_output

def callCommand(cmd):
    call(cmd,shell=True)

def saveCommandToVariable(cmd):
    return check_output(cmd,shell=True).decode('utf-8').replace('\n', '').strip()
    # run(cmdList, capture_output = True).stdout.decode().strip()

def createNewBranch(branch_name):
    callCommand(f'git checkout -b {branch_name}')

def checkCurrentbranch():
    curr_branch = saveCommandToVariable('git branch --show-current')
    return curr_branch

def renameBranchName():
    callCommand(f"git branch -m {new_branch_name}")

def checkForMainBranch():
    return saveCommandToVariable('git rev-parse --abbrev-ref origin/HEAD').replace('origin/', '')

def stagedChanges():
    callCommand("git add .")

def CommitMessage(msg):
    callCommand(f"git commit -m '{msg}'")

def changeBranchTo(branch):
    callCommand(f'git checkout {branch}')

def pushSubBranch(curr_branch):
    remote = saveCommandToVariable("git remote")
    callCommand(f'git push --set-upstream {remote} {curr_branch}')


main_branch = checkForMainBranch()

current_branch = checkCurrentbranch()
print('Main branch is -> ', main_branch)
print('your current branch -> ', current_branch)

try:
    branch_name = input('Enter branch name: ').strip()
    if branch_name:
        createNewBranch(branch_name)
    
    staged = input('Do you want to staged current changes? (y/n) ').lower()
    if staged == 'y':
        stagedChanges()
        
    msg = input("Commit message: ")
    if msg:
        CommitMessage(msg)
        
    current_branch = checkCurrentbranch()

    rename_branch = input(f'your current branch name is "{current_branch}" \nDo you want to rename branch name? (y/n) ').lower()
    
    if rename_branch == 'y':
        new_branch_name = input("Rename branch name: ")
        if new_branch_name:
            renameBranchName()
            current_branch = checkCurrentbranch()
        
    pull = input("Do you want to git pull? (y/n) ").lower()
    if pull == 'y':
        changeBranchTo(main_branch)
        callCommand('git pull')
        changeBranchTo(current_branch)
        callCommand(f'git rebase {main_branch}')

    # push your branch to remote
    push = input('Do you want to push to remote ? (y/n) ').lower()
    if push == 'y':
        pushSubBranch(current_branch)
        
except:
    pass