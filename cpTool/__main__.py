import os
import sys
import subprocess as sp 


import customModules.readmeFIleGenerate as readme
import api
import git


def get_arguments():

    argument = sys.argv

    if len(argument) == 1 or len(argument) > 2:
        print("\n[-] Please use --help  for more info")
        exit()

    else:
        if argument[1] == "--cf" or argument[1] == "--codeforces":
            return "cf"
            # print("Ok cf")

        elif argument[1] == "--init":

            # print("Generating git")
            return "git"

        elif argument[1] == "-h" or argument[1] == "--help":

            print("\nusage: cp-tool [option] ..... \n")

            print("--init \t : \t to initialize git repo\n--cf \t : \t to generate solved problems from codeforces\n--help \t : \t for more info \n")
            exit()

        else:
            print("\n[-] Please use --help  for more info\n")
            exit()


def createDir():

    while (1):
        try:
            createDir()
            break

        except OSError as error:

            print(error)


def main(argument):

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

    user_info = api.getUserInfo()

    repos = api.getSubmissions()

    readme.createReadmeFile(filePath, repo_name, user_info, repos)

    os.chdir(repo_path)

    if argument == "git":
        git.initGit()

    elif argument == "cf":

        git.updateRepo()

    print("Done!")

    print("Thanks for using cp-tool")


if __name__ == "__main__":

    argument = get_arguments()
    main(argument)