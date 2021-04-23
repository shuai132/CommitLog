import os
from bin.module import git

# 获取两次commit之间所有的commit信息 包含子模块(深度为1)的更新
projectPath  = "/Users/xiaoyezi/workfolder/smartpiano-apple-oversea"
commitIdTo   = "34e1c9c2424f6219f154c09bf52032f29a1e6857"
commitIdFrom = "1ac67c60bc5727c003d85d54f4916daf7c594988"

debug = False

os.chdir(projectPath)

git.stash()

git.resetHardToCommit(commitIdFrom)
git.submoduleUpdate()
statusBefore = git.getSubmoduleStatus()

git.resetHardToCommit(commitIdTo)
git.submoduleUpdate()
statusNow = git.getSubmoduleStatus()

if debug:
    print("statusNow:\n", statusNow)
    print("statusBefore:\n", statusBefore)

print("\n子模块的更新如下：")
for key in statusNow:
    commitIdNow = statusNow.get(key)
    commitIdBefore = statusBefore.get(key)
    if debug:
        print("key=%s\n"
          "before:%s\n"
          "now:   %s\n"
          % (key, commitIdBefore, commitIdNow))
    if commitIdBefore is None:
        if debug:
            print("key not found at before, ignore it!")
        break
    if commitIdNow != commitIdBefore:
        print("子模块path:%-30s 引用变更:%s --> %s" % (key, commitIdBefore, commitIdNow))
        os.chdir(key)
        gitMsg = git.getCommitMsgBeforeCommit(commitIdBefore)
        os.chdir(projectPath)
        if gitMsg != "":
            print(gitMsg)
        else:
            print("引用变更是回滚操作, 请手动查看！")
        print("")


projectName = projectPath.split("/")[-1]
print("\n主项目%s的更新如下：" % projectName)
gitMsg = git.getCommitMsgBeforeCommit(commitIdFrom)
print(gitMsg)

print("\n对子模块引用状态：")
for key in statusNow:
    commitIdNow = statusNow.get(key)
    commitIdBefore = statusBefore.get(key)
    if commitIdBefore is None:
        print("模块%s被删除" % key)
        break
    print(key)
    print("%s %s %s" % (commitIdBefore, commitIdNow == commitIdBefore and "==" or "->", commitIdNow))
