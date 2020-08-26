# coding = utf-8
import os

curpath = os.path.dirname(os.path.realpath("__file__"))

CheckType = os.path.join(curpath, "CheckType.py")
SearchDivision = os.path.join(curpath, "SearchDivision.py")

for i in range(10):
    os.system("python %s" % CheckType)
    os.system("python %s" % SearchDivision)
