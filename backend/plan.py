# coding=utf-8

from datetime import datetime


class Plan:

    def __init__(self, plan_name, start_time, list_name, day_list, list_nums):
        self.plan_name = plan_name
        self.start_time = datetime(
            *tuple([int(i) for i in start_time.split("-")]))
        self.list_name = list_name
        self.day_list = day_list
        self.list_nums = list_nums
        self.time = [0, 1, 5, 7, 15, 25, 32]
        self.arr = [[] for _ in range(7)]
        self.get_plan()

    def get_plan(self):
        for i in range(1, self.list_nums // self.day_list + 1):  # list个数
            for j in range(1, 8):  # 复习周期
                self.arr[j - 1].append(i + self.time[j - 1] - 1)

    def add_list(self, list_num):
        # 判断今天与计划创建日期的差数
        diff_days = (datetime.now() - self.start_time).days
        if diff_days <= self.arr[0][-1]:
            for _ in range(list_num):
                for j in range(1, 8):
                    self.arr[j - 1].append(self.arr[j - 1][-1] + 1)
        else:
            for i in range(list_num):
                for j in range(1, 8):
                    self.arr[j - 1].append(diff_days + i + self.time[j - 1])
        self.list_nums += list_num

    def delete_list(self, list_num):
        if list_num > len(self.arr[0]):
            return 0
        for i in range(7):
            for j in range(list_num):
                self.arr[i].pop()
        self.list_nums = len(self.arr[0])

    def to_delay(self, now_time=0):
        now_time = (datetime.now() - self.start_time).days + now_time
        m, n = len(self.arr), len(self.arr[0])
        record = []
        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == now_time:
                    record.append([i, j])
        for i in range(m):
            for j in range(n):
                for k in range(len(record)):
                    if i >= record[k][0] and j >= record[k][1]:
                        self.arr[i][j] += 1

    def to_forward(self, now_time=0):
        now_time = (datetime.now() - self.start_time).days + now_time
        m, n = len(self.arr), len(self.arr[0])
        record = []
        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == now_time:
                    record.append([i, j])
        for i in range(m):
            for j in range(n):
                for k in range(len(record)):
                    if i >= record[k][0] and j >= record[k][1]:
                        self.arr[i][j] -= 1

    def look_data(self):
        print(self.plan_name)
        print(self.start_time)
        print(self.list_nums)
        print(self.arr)

    def get_look(self, diff_day=0):
        '''
        今日计划
        '''
        # 计算差额天数
        now_time = (datetime.now() - self.start_time).days + diff_day

        # 找到目标任务
        plan_arr = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if self.arr[i][j] == now_time:
                    plan_arr.append(j + 1)

        # 输出计划
        print("{}，今日需完成目标:".format(self.plan_name))
        for i in range(len(plan_arr)):
            print("{} {}".format(self.list_name, plan_arr[i]))
