#!/usr/bin/env python3
import os
import sys

from module import git

projectPath = sys.argv[1]
commitIdFrom = sys.argv[2]
print(projectPath)

os.chdir(projectPath)

projectName = projectPath
gitMsg = git.getCommitMsgBeforeCommit(commitIdFrom)
print(gitMsg)
