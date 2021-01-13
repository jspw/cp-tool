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

repo_name = "My Cp Track"

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


user_info = {
    "handle": "Shifat",
    "rating": "1030",
    "maxRating": "1366",
    "contribution": "16",
    "rank": "newbie",
    "maxRank": "pupil",
    "registrationTimeSeconds": "2012",
    "organization": "Software Engineering , SUST",
    "avatar": "https://codeforces.com//userpic.codeforces.com/713637/avatar/c741af7877c783b4.jpg"

}

repos =  api.getSubmissions()


readme.createReadmeFile(repo_name, user_info, repos)
