# coding=utf-8

from datetime import datetime


class Plan:

    def __init__(self, planName, startTime, listName, dayList, listNums):
        self.planName = planName
        self.startTime = datetime(*tuple([int(i) for i in startTime.split("-")]))
        self.listName = listName
        self.dayList = dayList
        self.listNums = listNums
        self.time = [0, 1, 5, 7, 15, 25, 32]
        self.arr = [[] for i in range(7)]
        self.get_plan()

    def get_plan(self):
        for i in range(1, self.listNums // self.dayList + 1):
            for j in range(1, 8):
                self.arr[j - 1].append(i + self.time[j - 1] - 1)

    def add_list(self, list_num):
        for i in range(self.listNums // self.dayList + 1, self.listNums // self.dayList + 1 + list_num):
            for j in range(1, 8):
                self.arr[j - 1].append(self.arr[j - 1][-1] + 1)
        self.listNums += list_num

    def delete_list(self, list_num):
        if list_num > len(self.arr[0]):
            return 0
        for i in range(7):
            for j in range(list_num):
                self.arr[i].pop()
        self.listNums = len(self.arr[0])

    def to_delay(self, nowTime=0):
        nowTime = (datetime.now() - self.startTime).days + nowTime
        m, n = len(self.arr), len(self.arr[0])
        record = []
        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == nowTime:
                    record.append([i, j])
        for i in range(m):
            for j in range(n):
                for k in range(len(record)):
                    if i >= record[k][0] and j >= record[k][1]:
                        self.arr[i][j] += 1

    def to_forward(self, nowTime=0):
        nowTime = (datetime.now() - self.startTime).days + nowTime
        m, n = len(self.arr), len(self.arr[0])
        record = []
        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == nowTime:
                    record.append([i, j])
        for i in range(m):
            for j in range(n):
                for k in range(len(record)):
                    if i >= record[k][0] and j >= record[k][1]:
                        self.arr[i][j] -= 1

    def look_data(self):
        print(self.planName)
        print(self.startTime)
        print(self.listNums)
        print(self.arr)

    def get_look(self):
        '''
        今日计划
        '''
        # 计算差额天数
        nowTime = (datetime.now() - self.startTime).days

        # 找到目标任务
        plan_arr = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if self.arr[i][j] == nowTime:
                    plan_arr.append(j + 1)

        # 输出计划
        print("{}，今日需完成目标:".format(self.planName))
        for i in range(len(plan_arr)):
            print("{} {}".format(self.listName, plan_arr[i]))

