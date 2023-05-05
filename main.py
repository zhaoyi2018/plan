# coding=utf-8

from solution import Solution


def create_plan_2(tool):
    print("请按要求，依次输入：")
    planName = input("任务名：")
    startTime = input("开始时间（2020-01-02）:")
    listNums = int(input("章节数目："))
    tool.add_plan(planName=planName, startTime=startTime, listName="章", listNums=listNums)
    print("添加成功！")


def delay_plan_3(tool):
    print('''请选择：\n
    1. 指定任务推迟\n
    2. 全部任务推迟\n
    3. 退出
    ''')
    num = int(input("输入号码："))
    if num == 3:
        return
    elif num == 1:
        plan_name = input("任务名：")
        this_time = int(input("推迟时间指定(若为当天设为0，昨天为-1，明天为1):"))
        tool.delay_plan(planName=plan_name, nowTime=this_time)
    elif num == 2:
        this_time = int(input("推迟时间指定(若为当天设为0，昨天为-1，明天为1):"))
        tool.delay_all_plan(nowTime=this_time)
    print("推迟成功！")


def forward_plan_4(tool):
    print('''请选择：\n
        1. 指定任务提前\n
        2. 全部任务提前\n
        3. 退出
        ''')
    num = int(input("输入号码："))
    if num == 3:
        return
    elif num == 1:
        plan_name = input("任务名：")
        this_time = int(input("提前时间指定(若为当天设为0，昨天为-1，明天为1):"))
        tool.forward_plan(planName=plan_name, nowTime=this_time)
    elif num == 2:
        this_time = int(input("提前时间指定(若为当天设为0，昨天为-1，明天为1):"))
        tool.forward_all_plan(nowTime=this_time)


def insert_list_5(tool):
    plan_name = input("任务名称:")
    tool.look_plan(plan_name)
    list_num = int(input("添加章节数:"))
    tool.insert_list(planName=plan_name, listNum=list_num)
    print("添加成功！")


def delete_list_6(tool):
    plan_name = input("任务名称:")
    tool.look_plan(plan_name)
    list_num = int(input("删除章节数:"))
    tool.delete_list(planName=plan_name, listNum=list_num)
    print("删除成功！")


def look_plan_7(tool):
    plan_name = input("任务名称:")
    tool.look_plan(planName=plan_name)


def print_menu():
    # 主菜单栏
    print("*" * 20)
    print("--- 心灵再慢一点，动手再做一点！ ----")
    print("1. 查询任务")
    print("2. 创建任务")
    print("3. 推迟任务")
    print("4. 加快任务")
    print("5. 添加任务章节")
    print("6. 删除任务章节")
    print("7. 查看任务详情")
    print("8. 退出系统")
    print("*" * 20)
    return int(input("请输入序号:"))


if __name__ == "__main__":
    tool = Solution()
    while True:
        num = print_menu()
        if num == 8:
            print("退出成功！")
            break
        elif num == 1:
            diff = int(input("是否需要偏移（天）："))
            tool.today_all_task(diff)
        elif num == 2:
            create_plan_2(tool)
        elif num == 3:
            delay_plan_3(tool)
        elif num == 4:
            forward_plan_4(tool)
        elif num == 5:
            insert_list_5(tool)
        elif num == 6:
            delete_list_6(tool)
        elif num == 7:
            look_plan_7(tool)


