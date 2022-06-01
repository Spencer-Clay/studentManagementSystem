import util.student as student
import util.processFile as processFile


class ManagementSystem(object):
    def __init__(self):
        self.filename = "student.txt"

    def displayBasicInfo(self):
        print(processFile.displayStudentInfo(self.filename))

    def manageBasicInfo_insertRecord(self, studentNum, studentName, studentSex, class1Score, class2Score, class3Score):
        return processFile.insertStudentInfo(self.filename, studentNum, studentName, studentSex, class1Score,
                                             class2Score,
                                             class3Score)

    def manageBasicInfo_delRecord(self, studentNum):
        msg = processFile.delStudentInfo(self.filename, studentNum)
        print(msg)

    def manageBasicInfo_changeRecord(self, studentNum, studentName, studentSex, class1Score, class2Score, class3Score):
        processFile.changeStudentInfo(self.filename, studentNum, studentName, studentSex, class1Score, class2Score,
                                      class3Score)

    def manageStudentInfo_calSumScore(self):
        processFile.calSumScore(self.filename)

    def manageStudentInfo_sortByScore(self):
        processFile.sortByScore(self.filename)

    def manageExamInfo_calMaxScoreOfEachClass(self):
        msg = processFile.calMaxScoreOfEachClass(self.filename)
        print(msg)

    def manageExamInfo_calMinScoreOfEachClass(self):
        msg = processFile.calMinScoreOfEachClass(self.filename)
        print(msg)

    def manageExamInfo_calAverageScoreOfEachClass(self):
        msg = processFile.calAverageScoreOfEachClass(self.filename)
        print(msg)

    def queryByStudentNum(self, studentNum):
        msg = processFile.queryByStudentNum(self.filename, studentNum)
        print(msg)

    def queryByStudentName(self, studentName):
        msg = processFile.queryByStudentName(self.filename, studentName)
        print(msg)

    def queryByRank(self, rank):
        msg = processFile.queryByRank(self.filename, rank)
        print(msg)

    def consoleUi(self):
        mainBanner = '''
********1.显示基本信息********
********2.基本信息管理********
********3.学生成绩管理********
********4.考试成绩统计********
********5.根据条件查询********
********0.退出********
请输入您的选择（0-5）：'''
        subBanner_manageBasicInfo = '''
********1.插入学生记录********
********2.删除学生记录********
********3.修改学生记录********
********0.返回上层菜单********
请输入您的选择（0-5）：'''
        subBanner_manageStudentInfo = '''
********1.计算学生总分********
********2.根据总分排名********
********0.返回上层菜单********
请输入您的选择（0-2）：'''
        subBanner_manageExamInfo = '''
********1.求课程最高分********
********2.求课程最低分********
********3.求课程平均分********
********0.返回上层菜单********
请输入您的选择（0-3）：'''
        subBanner_queryByConditions = '''
********1.按学号查询********
********2.按姓名查询********
********3.按名次查询********
********0.返回上层菜单********
请输入您的选择（0-3）：'''
        choice = 1
        while choice != "0":
            choice = input(mainBanner)
            if choice == "1":
                self.displayBasicInfo()
            elif choice == "2":
                subchoice2 = input(subBanner_manageBasicInfo)
                if subchoice2 == "1":
                    recordToInsert = input("请输入需要插入的学生信息，格式为：\"学号,姓名,性别,课程1得分,课程2得分,课程3得分\"")
                    recordToInsert = recordToInsert.split(",")
                    try:
                        status = self.manageBasicInfo_insertRecord(recordToInsert[0], recordToInsert[1],
                                                                   recordToInsert[2],
                                                                   recordToInsert[3], recordToInsert[4],
                                                                   recordToInsert[5])
                    except Exception as e:
                        status = "输入数据错误！"
                    print(status)
                elif subchoice2 == "2":
                    self.displayBasicInfo()
                    studentToDel = input("请输入要删除的学生学号：")
                    self.manageBasicInfo_delRecord(studentToDel)
                    self.displayBasicInfo()
                elif subchoice2 == "3":
                    self.displayBasicInfo()
                    studentToChange = input("请输入要修改的学生学号：")
                    recordToChange = input("请输入需要修改的学生信息，格式为：\"姓名,性别,课程1得分,课程2得分,课程3得分\"")
                    recordToChange = recordToChange.split(",")
                    try:
                        self.manageBasicInfo_changeRecord(studentToChange, recordToChange[0],
                                                          recordToChange[1],
                                                          recordToChange[2], recordToChange[3],
                                                          recordToChange[4])
                        self.displayBasicInfo()
                    except Exception:
                        print("输入错误！")
                elif subchoice2 == "0":
                    continue
            elif choice == "3":
                subchoice3 = input(subBanner_manageStudentInfo)
                if subchoice3 == "1":
                    self.manageStudentInfo_calSumScore()
                    self.displayBasicInfo()
                elif subchoice3 == "2":
                    self.manageStudentInfo_sortByScore()
                    self.displayBasicInfo()
                elif subchoice3 == "0":
                    continue
            elif choice == "4":
                subchoice4 = input(subBanner_manageExamInfo)
                if subchoice4 == "1":
                    self.manageExamInfo_calMaxScoreOfEachClass()
                elif subchoice4 == "2":
                    self.manageExamInfo_calMinScoreOfEachClass()
                elif subchoice4 == "3":
                    self.manageExamInfo_calAverageScoreOfEachClass()
                elif subchoice4 == "0":
                    continue
            elif choice == "5":
                subchoice5 = input(subBanner_queryByConditions)
                if subchoice5 == "1":
                    studentNum = input("请输入要查找的学号：")
                    self.queryByStudentNum(studentNum)
                if subchoice5 == "2":
                    studentName = input("请输入要查找的姓名：")
                    self.queryByStudentName(studentName)
                if subchoice5 == "3":
                    rank = input("请输入要查找的名次：")
                    self.queryByRank(rank)
                if subchoice5 == "0":
                    continue
            elif choice == "0":
                break


a = ManagementSystem()

a.consoleUi()
