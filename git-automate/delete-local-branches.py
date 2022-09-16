from subprocess import call, check_output


def runCommand(cmds):
    result = check_output(cmds, shell=True).decode('utf-8')
    cleanRes = result.replace('\n', '').strip()
    return cleanRes


def exec_Command(cmd):
    # just run command no need to return or store
    call(cmd, shell=True)


def currentBranch():
    return runCommand('git branch --show-current')


try:
    hasGitRepo = runCommand('git rev-parse --is-inside-work-tree')
except:
    hasGitRepo = False

if not hasGitRepo:
    print('Sorry git repo not found :(')

else:
    try:
        if hasGitRepo == 'true':
            current_branch = currentBranch()
            print("\n..............................\n")

            # if you want to enter manually
            # main_branch = input(f"\ncurrent branch: {current_branch} \nplease specify your Main branch (dev) : ")
            # main_branch = 'dev' if main_branch == '' else main_branch

            main_branch = runCommand('git rev-parse --abbrev-ref origin/HEAD').replace('origin/', '')

            if main_branch != current_branch:
                exec_Command(f'git checkout {main_branch}')
                current_branch = currentBranch()

            branches = runCommand('git branch --list').split(' ')

            for subBranch in branches:
                branch = subBranch.strip().replace("*", '')
                if branch != main_branch and branch != '*' and branch != '':
                    exec_Command(f'git branch -D {branch}')

            print("branches deleted successfully")
            print('Here is your current branch: -> ', current_branch)

            print("..............................\n")

    except Exception as e:
        print(e)
