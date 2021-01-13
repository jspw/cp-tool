import os
import customModules.readmeFIleGenerate as readme
import api

# def createDir():

#     creating_directory = input("Enter dir name : ")
#     path = os.path.join(main_directory, creating_directory)
#     os.mkdir(path)


# while (1):
#     try:
#         createDir()
#         break

#     except OSError as error:

#         print(error)


main_directory = os.getcwd()

repo_name = input("Enter your repository name : ")

filePath = os.path.join(main_directory, 'test.md')

isFileExists = os.path.exists(filePath)

# if isFileExists :
#     file = open('test.md','a')
#     file.write("Hello\n")
#     file.close()
# else :
#     file = open('test.md','w')
#     file.write("Hello\n")
#     file.close()


user_info = api.getUserInfo()

repos =  api.getSubmissions()

readme.createReadmeFile(repo_name, user_info, repos)

print("Done!")

print("Thanks for using cp-tool")
