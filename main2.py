import os
from bin.module import git

# 用于对比子两个相似项目的子模块引用是否一致
projectPath1 = "/Users/xiaoyezi/workfolder/smartpiano-android-oversea"
commitId1    = "61577f949a479376f293c9ec71654c56b9d2d997"

projectPath2 = "/Users/xiaoyezi/workfolder/smartpiano-apple-oversea"
commitId2    = "34e1c9c2424f6219f154c09bf52032f29a1e6857"


def getProjectSubmoduleStatus(path, commitId):
        os.chdir(path)
        git.stash()
        git.resetHardToCommit(commitId)
        git.submoduleUpdate()
        return git.getSubmoduleStatus()

status1 = getProjectSubmoduleStatus(projectPath1, commitId1)
status2 = getProjectSubmoduleStatus(projectPath2, commitId2)

projectName1 = projectPath1.split("/")[-1]
projectName2 = projectPath2.split("/")[-1]
counter = 0
for key in status1:
    id1 = status1.get(key)
    id2 = status2.get(key)
    if id2 is None:
        break
    if id1 != id2:
        print(key)
        print("%s -> %s" % (id1, id2))
        counter += 1

if counter is 0:
    print("共有的子模块引用一致！")
