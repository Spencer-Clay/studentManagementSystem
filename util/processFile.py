"""
studentDict = {"studentNum": "",
               "studentName": "",
               "studentSex": "",
               "class1Score": "",
               "class2Score": "",
               "class3Score": "",
               }
"""


def displayStudentInfo(filename):
    with open(filename) as file_tmp:
        studentsInfo = file_tmp.read()
        file_tmp.close()
    return studentsInfo


def readStudentInfo(filename):
    students = []
    with open(filename) as file_tmp:
        studentsInfo = file_tmp.readlines()
        for eachStudent in studentsInfo:
            eachStudent = eachStudent.split(",")
            studentNum = eachStudent[0]
            studentName = eachStudent[1]
            studentSex = eachStudent[2]
            class1Score = eachStudent[3]
            class2Score = eachStudent[4]
            class3Score = eachStudent[5]
            sumScore = eachStudent[6]
            rank = eachStudent[7]
            students.append({"studentNum": str(studentNum),
                             "studentName": str(studentName),
                             "studentSex": str(studentSex),
                             "class1Score": str(class1Score),
                             "class2Score": str(class2Score),
                             "class3Score": str(class3Score),
                             "sumScore": str(sumScore),
                             "rank": str(rank),
                             })
    return students


def insertStudentInfo(filename, studentNum, studentName, studentSex, class1Score, class2Score, class3Score):
    recordToInsert = studentNum + "," + studentName + "," + studentSex + "," + class1Score + "," + class2Score + "," + class3Score + "," + str(
        float(class1Score) + float(class2Score) + float(class3Score)) + "," + "0"
    with open(filename, "a") as file_tmp:
        try:
            file_tmp.write(recordToInsert+'\n')
            file_tmp.close()
            return displayStudentInfo(filename)
        except Exception as e:
            return e


def delStudentInfo(filename, studentNum):
    records = ""
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        if str(eachStudent["studentNum"]) == str(studentNum):
            studentsInfo.remove(eachStudent)
            for i in studentsInfo:
                records += i["studentNum"] + "," + i["studentName"] + "," + i["studentSex"] + "," + i[
                    "class1Score"] + "," + i["class2Score"] + "," + i["class3Score"] + "," + i["sumScore"] + "," + i[
                               "rank"]
            with open(filename, "w") as file_tmp:
                file_tmp.write(records)
                file_tmp.close()
                return displayStudentInfo(filename)

    return "找不到该学号的学生"


def changeStudentInfo(filename, studentNum, studentName, studentSex, class1Score, class2Score, class3Score):
    records = ""
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        if str(eachStudent["studentNum"]) == str(studentNum):
            studentsInfo[studentsInfo.index(eachStudent)] = {"studentNum": str(studentNum),
                                                             "studentName": str(studentName),
                                                             "studentSex": str(studentSex),
                                                             "class1Score": str(class1Score),
                                                             "class2Score": str(class2Score),
                                                             "class3Score": str(class3Score),
                                                             "sumScore": float(class1Score) + float(
                                                                 class2Score) + float(class3Score),
                                                             "rank": "0",
                                                             }
            for i in studentsInfo:
                records += i["studentNum"] + "," + i["studentName"] + "," + i["studentSex"] + "," + i[
                    "class1Score"] + "," + i["class2Score"] + "," + i["class3Score"] + "," + str(i["sumScore"]) + "," + \
                           i["rank"].strip("\n") + "\n"
            with open(filename, "w") as file_tmp:
                file_tmp.write(records)
                file_tmp.close()
                return displayStudentInfo(filename)


def calSumScore(filename):
    records = ''
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        eachStudent["sumScore"] = float(eachStudent["class1Score"]) + float(eachStudent["class2Score"]) + float(
            eachStudent["class3Score"])
    for i in studentsInfo:
        records += i["studentNum"] + "," + i["studentName"] + "," + i["studentSex"] + "," + i[
            "class1Score"] + "," + i["class2Score"] + "," + i["class3Score"] + "," + str(i["sumScore"]) + "," + str(
            studentsInfo.index(i) + 1).strip(
            "\n") + "\n"
    with open(filename, "w") as file_tmp:
        file_tmp.write(records)
        file_tmp.close()
        return displayStudentInfo(filename)


def sortByScore(filename):
    records = ''
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        eachStudent["sumScore"] = float(eachStudent["class1Score"]) + float(eachStudent["class2Score"]) + float(
            eachStudent["class3Score"])
    studentsInfo.sort(key=lambda student: student["sumScore"])
    studentsInfo = studentsInfo[::-1]
    for i in studentsInfo:
        records += i["studentNum"] + "," + i["studentName"] + "," + i["studentSex"] + "," + i[
            "class1Score"] + "," + i["class2Score"] + "," + i["class3Score"] + "," + str(i["sumScore"]) + "," + str(
            studentsInfo.index(i) + 1).strip(
            "\n") + "\n"
    with open(filename, "w") as file_tmp:
        file_tmp.write(records)
        file_tmp.close()
        return displayStudentInfo(filename)


def calMaxScoreOfEachClass(filename):
    studentsInfo = readStudentInfo(filename)
    scoreOfClass1 = []
    scoreOfClass2 = []
    scoreOfClass3 = []
    for i in studentsInfo:
        scoreOfClass1.append(i["class1Score"])
        scoreOfClass2.append(i["class2Score"])
        scoreOfClass3.append(i["class3Score"])
    return "课程1最高分是%s,\n课程2最高分是%s,\n课程3最高分是%s" % (
        str(max(scoreOfClass1)), str(max(scoreOfClass2)), str(max(scoreOfClass3)))


def calMinScoreOfEachClass(filename):
    studentsInfo = readStudentInfo(filename)
    scoreOfClass1 = []
    scoreOfClass2 = []
    scoreOfClass3 = []
    for i in studentsInfo:
        scoreOfClass1.append(i["class1Score"])
        scoreOfClass2.append(i["class2Score"])
        scoreOfClass3.append(i["class3Score"])
    return "课程1最高分是%s,\n课程2最高分是%s,\n课程3最高分是%s" % (
        str(min(scoreOfClass1)), str(min(scoreOfClass2)), str(min(scoreOfClass3)))


def calAverageScoreOfEachClass(filename):
    studentsInfo = readStudentInfo(filename)
    scoreOfClass1 = []
    scoreOfClass2 = []
    scoreOfClass3 = []
    for i in studentsInfo:
        scoreOfClass1.append(i["class1Score"])
        scoreOfClass2.append(i["class2Score"])
        scoreOfClass3.append(i["class3Score"])
    scoreOfClass1 = [float(i) for i in scoreOfClass1]
    scoreOfClass2 = [float(i) for i in scoreOfClass2]
    scoreOfClass3 = [float(i) for i in scoreOfClass3]
    return "课程1平均分是%s,\n课程2平均分是%s,\n课程3平均分是%s" % (
        str(sum(scoreOfClass1) / len(scoreOfClass1)), str(sum(scoreOfClass2) / len(scoreOfClass2)),
        str(sum(scoreOfClass3) / len(scoreOfClass3)))


def queryByStudentNum(filename, studentNum):
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        if eachStudent["studentNum"] == studentNum:
            return ','.join(eachStudent.values())
    return "不存在该学号！"


def queryByStudentName(filename, name):
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        if eachStudent["studentName"] == name:
            return ','.join(eachStudent.values())
    return "不存在该姓名！"


def queryByRank(filename, rank):
    studentsInfo = readStudentInfo(filename)
    for eachStudent in studentsInfo:
        if eachStudent["rank"].strip("\n") == rank:
            return ','.join(eachStudent.values())
    return "不存在该名次！"
