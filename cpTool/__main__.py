import os
import sys
import subprocess as sp
import optparse as op

import cpTool.customModules.readmeFIleGenerator as readme
import cpTool.git as git
import cpTool.api as api


def get_arguments():


    parser = op.OptionParser();
    parser.add_option("-c","--config",dest="configure",help="confiure local space for git")
    parser.add_option("-j","--judge",dest="judge",help="online judge")

    (options,arguments) = parser.parse_args()


    if options.judge == "codeforces" and options.configure == "init" :
        return "git"

    elif options.judge == "codeforces" and options.configure == "update":
        return "update"

    else :
        parser.error("\n-c \t : \t use '-c update' to update repo or '-c init to initialize repo\n-j \t : \t use '-j codeforces'\n--help \t : \t for more info contact 'mhshifat757@gmail.com' \n")


def createDir():
    while (1):
        try:
            createDir()
            break

        except OSError as error:

            print(error)


def main(argument):
    username = input("Enter codeforces handle : ")

    if argument == "git":

        repo_name = input("Enter your repository name : ")
        current_path = os.getcwd()
        repo_path_name = repo_name
        path = os.path.join(current_path, repo_path_name)

        try:
            os.mkdir(path)
        except Exception as err:
            print(err)
            print("Please try again!")
            exit()

        repo_path = os.path.join(current_path, repo_path_name)

        filePath = os.path.join(repo_path, 'README.md')

        user_info = api.getUserInfo(username)

        repos = api.getSubmissions(username)

        readme.createReadmeFile(filePath, repo_name, user_info, repos)

        os.chdir(repo_path)

        git.initGit()

    elif argument == "update":

        repo_path = current_path = os.getcwd()

        repo_name = os.path.basename(repo_path)

        filePath = os.path.join(repo_path, 'README.md')

        user_info = api.getUserInfo(username)

        repos = api.getSubmissions(username)

        readme.createReadmeFile(filePath, repo_name, user_info, repos)

        git.updateRepo()

    print("Done!")

    print("Thanks for using cp-tool")


if __name__ == "__main__":

    print('''
                         ____ ____     _____           _ 
                        / ___|  _ \   |_   _|__   ___ | |
                       | |   | |_) |____| |/ _ \ / _ \| |
                       | |___|  __/_____| | (_) | (_) | |
                        \____|_|        |_|\___/ \___/|_|
                                                         
    ''')

    argument = get_arguments()

    main(argument)
