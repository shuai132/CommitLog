# coding:utf-8

import commands

cmd = commands.getoutput

# 基本操作
def stash():
    cmd("git stash")

def resetHardToCommit(commitId):
    cmd("git reset --hard " + commitId)

def submoduleUpdate():
    cmd("git submodule update --init --recursive")


# 拓展操作
def getCommitInfoWithId(commitId):
    prefix = "git log --format='%H|%ct|%an|%s' -1 "
    info = cmd(prefix + commitId)
    return info

def getCommitTimeWithId(commitId):
    info = getCommitInfoWithId(commitId)
    time = info.split("|")[1]
    return time

def getCommitMsgBeforeCommit(commitId):
    prefix = "git log --format='%s' --since="
    time = getCommitTimeWithId(commitId)
    return cmd(prefix + time)

# 获取子模块状态表 path作为key commitId作为value
def getSubmoduleStatus():
    smStatus = cmd("git submodule status").split("\n")
    statusTable = {}
    for status in smStatus:
        infos = status[1:].split(" ")

        HEAD = infos[0]
        path = infos[1]

        statusTable[path] = HEAD
    return statusTable
