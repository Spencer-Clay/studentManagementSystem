class Student(object):
    def __init__(self, studentNum, studentName, studentSex, class1Score, class2Score, class3Score):
        self.studentNum = studentNum
        self.studentName = studentName
        self.studentSex = studentSex
        self.class1Score = class1Score
        self.class2Score = class2Score
        self.class3Score = class3Score

        self.sumScore = float(self.class1Score) + float(self.class2Score) + float(self.class3Score)
        self.rank = 0

    def updateRank(self, rank):
        self.rank = rank
