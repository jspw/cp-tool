import subprocess as sp 

repo_url = input("Repository url : ")

init = "git init"
add_files = "git add ."
commit = "git commit -m 'auto generated by [cp-tool](https://github.com/jspw/cp-tool)'"
add_origin = "git remote add origin "+repo_url
branch = "git branch -M main"
push = "git push origin main"


def initGit () :
    sp.call(init,shell=True)
    sp.call(add_files,shell=True)
    sp.call(commit,shell=True)
    sp.call(branch,shell=True)
    sp.call(add_origin,shell=True)
    sp.call(push,shell=True)

def updateRepo():
    sp.call(add_files,shell=True)
    sp.call(commit,shell=True)
    sp.call(push,shell=True)
