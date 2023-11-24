# coding=utf-8

import pickle
import os
from backend.plan import Plan
from datetime import datetime


class Solution:

    def __init__(self):
        self.file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def save_plan(self, plan):
        save_path = open(self.file_path + "/list/{}.pkl".format(plan.plan_name), "wb")
        str_data = pickle.dumps(plan)
        save_path.write(str_data)
        save_path.close()

    def read_plan(self, plan_name):
        with open(self.file_path + "/list/{}.pkl".format(plan_name), "rb") as file:
            return pickle.loads(file.read())

    def delete_plan(self, plan_name):
        path = self.file_path + "/list/{}.pkl".format(plan_name)
        if os.path.exists(path):
            os.remove(path)
        else:
            print("no such plan:{}".path)

    def get_all_plan(self):
        return [i[:-4] for i in os.listdir(self.file_path + "/list/") if ".pkl" in i]

    def today_all_task(self, diff=None):
        all_plan = self.get_all_plan()
        print("时间点：", datetime.now())
        for i in all_plan:
            plan = self.read_plan(i)
            if diff:
                plan.get_look(diff_day=diff)
            else:
                plan.get_look()

    def add_plan(self, plan_name='Plan', start_time=str(datetime.today()).split(" ")[0], list_name="plan", day_list=1,
                 list_nums=7):
        new_plan = Plan(plan_name, start_time, list_name, day_list, list_nums)
        self.save_plan(new_plan)

    def delay_plan(self, plan_name, now_time=0):
        plan = self.read_plan(plan_name)
        plan.to_delay(now_time)
        self.save_plan(plan)

    def delay_all_plan(self, now_time=0):
        all_plan = self.get_all_plan()
        for i in all_plan:
            plan = self.read_plan(i)
            plan.to_delay(now_time)
            self.save_plan(plan)

    def forward_plan(self, plan_name, now_time=0):
        plan = self.read_plan(plan_name)
        plan.to_forward(now_time)
        self.save_plan(plan)

    def forward_all_plan(self, now_time=0):
        all_plan = self.get_all_plan()
        for i in all_plan:
            plan = self.read_plan(i)
            plan.to_forward(now_time)
            self.save_plan(plan)

    def insert_list(self, plan_name, list_num=0):
        plan = self.read_plan(plan_name)
        plan.add_list(list_num)
        self.save_plan(plan)

    def look_plan(self, plan_name):
        plan = self.read_plan(plan_name)
        plan.look_data()

    def delete_list(self, plan_name, list_num=0):
        """
        删除指定数目的章节
        """
        plan = self.read_plan(plan_name)
        plan.delete_list(list_num)
        self.save_plan(plan)
