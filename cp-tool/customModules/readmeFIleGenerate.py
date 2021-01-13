import customModules.htmlGenerator as html

def generateMarkdownFile(file,repo_name,user_info,repos):

    print("Creating markdown file .......")

    file.write("# " + repo_name + "\n\n")

    file.write("## Intro\n\n")

    file.write(">\tAutomated by [cp-tool](https://github.com/jspw/cp-tool)\n\n")

    file.write(
        "This is a repository to keep track of my problem solving practice.\nFor now, It contains all the problems I have solved at \n- **[Codeforces](https://codeforces.com/)** \n\n")

    file.write("## User Details ([" + user_info["handle"] +
               "](https://codeforces.com/profile/" + user_info["handle"] + "))\n\n")

    file.write("```.json\n")

    file.write("{\n")

    file.write('\t"handle" : "' + user_info['handle'] + '",\n')
    file.write('\t"organization" : "' + user_info['organization'] + '",\n')
    file.write('\t"rank" : "' + user_info['rank'] + '",\n')
    file.write('\t"rating" : ' + user_info['rating'] + ',\n')
    file.write('\t"contribution" : ' + user_info['contribution'] + ',\n')
    file.write('\t"maxRank" : "' + user_info['maxRank'] + '",\n')
    file.write('\t"maxRating" : ' + user_info['maxRating'] + ',\n')
    file.write('\t"joined" : "' +
               user_info['registrationTimeSeconds'] + '",\n')

    file.write("}\n")

    file.write("\n```\n")

    file.write("## Submissions \n\n")

    file.write(
        '<table align="center" border = "0px" cellpadding ="2px" cellspacing ="2px" >\n')

    file.write("<tr><th>#</th><th>Probelm</th><th>Catagory</th><th>Rating</th><th>Tags</th><th>Solution</th><th>Submission Time</th></tr>\n")

    for i in range(len(repos)):

        table_body = html.table_row_start + html.tableDataCreate(str(len(repos)-i)) + html.tableDataCreate(html.linkCreate(repos[i]["problem_link"], repos[i]["problem_name"])) + html.tableDataCreate(repos[i]["index"]) + html.tableDataCreate(repos[i]["rating"]) + html.tableDataCreate(
            repos[i]["tags"]) + html.tableDataCreate(html.linkCreate(repos[i]["solution_link"], repos[i]["programmingLanguage"])) + html.tableDataCreate(repos[i]["submission_time"]) + html.table_row_end

        file.write(table_body)

    file.write("</table>\n")


def createReadmeFile(repo_name,user_info,repos):
    file = open('SAMPLE.md', 'w')

    generateMarkdownFile(file,repo_name,user_info,repos)

    file.close()