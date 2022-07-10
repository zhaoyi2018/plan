# coding=utf-8

import pickle
import os
from plan import Plan
from datetime import datetime


class Solution:

    def save_plan(self, plan):
        save_path = open("list/{}.pkl".format(plan.planName), "wb")
        strData = pickle.dumps(plan)
        save_path.write(strData)
        save_path.close()

    def read_plan(self, planName):
        with open("list/{}.pkl".format(planName), "rb") as file:
            return pickle.loads(file.read())

    def delete_plan(self, planName):
        path = "list/{}.pkl".format(planName)
        if os.path.exists(path):
            os.remove(path)
        else:
            print("no such plan:{}".path)

    def get_all_plan(self):
        return [i[:-4] for i in os.listdir("list/") if ".pkl" in i]

    def today_all_task(self, diff=None):
        all_plan = self.get_all_plan()
        for i in all_plan:
            plan = self.read_plan(i)
            if diff:
                plan.get_look(diff_day=diff)
            else:
                plan.get_look()

    def add_plan(self, planName='Plan', startTime=str(datetime.today()).split(" ")[0], listName="plan", dayList=1,
                 listNums=7):
        newPlan = Plan(planName, startTime, listName, dayList, listNums)
        self.save_plan(newPlan)

    def delay_plan(self, planName, nowTime=0):
        plan = self.read_plan(planName)
        plan.to_delay(nowTime)
        self.save_plan(plan)

    def delay_all_plan(self, nowTime=0):
        all_plan = self.get_all_plan()
        for i in all_plan:
            plan = self.read_plan(i)
            plan.to_delay(nowTime)
            self.save_plan(plan)

    def forward_plan(self, planName, nowTime=0):
        plan = self.read_plan(planName)
        plan.to_forward(nowTime)
        self.save_plan(plan)

    def forward_all_plan(self, nowTime=0):
        all_plan = self.get_all_plan()
        for i in all_plan:
            plan = self.read_plan(i)
            plan.to_forward(nowTime)
            self.save_plan(plan)

    def insert_list(self, planName, listNum=0):
        plan = self.read_plan(planName)
        plan.add_list(listNum)
        self.save_plan(plan)

    def look_plan(self, planName):
        plan = self.read_plan(planName)
        plan.look_data()

    def delete_list(self, planName, listNum=0):
        '''
        删除指定数目的章节
        '''
        plan = self.read_plan(planName)
        plan.delete_list(listNum)
        self.save_plan(plan)
