import os
import customModules.readmeFIleGenerate as readme
import script

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


# repos = [
#     {
#         "problem_name": "A Bad Guy",

#         "index": "B",

#         "submission_id": "1212121212121",

#         "contest_id": "asa",

#         "problem_link": "www.facebook.com",

#         "solution_link": "www.facebook.com",

#         "rating": "1000",

#         "tags": "math,dp",

#         "programmingLanguage": "C++",

#         "submission_time": "4th feb,2021"
#     },
#     {
#         "problem_name": "A Bad Guy",

#         "index": "B",

#         "submission_id": "1212121212121",

#         "contest_id": "asa",

#         "problem_link": "www.facebook.com",

#         "solution_link": "www.facebook.com",

#         "rating": "1000",

#         "tags": "math,dp",

#         "programmingLanguage": "C++",

#         "submission_time": "4th feb,2021"
#     },
# ]


repos =  script.getSubmissions()


readme.createReadmeFile(repo_name, user_info, repos)
