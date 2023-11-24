from backend.solution import Solution

tool = Solution()


def get_menu_list():
    return [(1, "查询任务"),
            (2, "创建任务"),
            (3, "推迟任务"),
            (4, "加快任务"),
            (5, "添加任务章节"),
            (6, "删除任务章节"),
            (7, "查看任务详情")]


def query_all_list():
    return tool.today_all_task()


def create_new_plan(plan_name, start_time, list_nums):
    if tool.add_plan(plan_name=plan_name, start_time=start_time, list_name="章", list_nums=list_nums):
        return {'msg': '创建成功!'}
    else:
        return {'msg': '创建失败!'}


def delay_plan(num, this_time, plan_name=None):
    if num == 1 and tool.delay_plan(plan_name=plan_name, now_time=this_time):
        return {'msg': '推迟成功！'}
    elif num == 2 and tool.delay_all_plan(now_time=this_time):
        return {'msg': '推迟成功！'}
    else:
        return {'msg': '推迟失败!'}


def speed_up_plan():
    return None


def add_new_chapter():
    return None


def delete_chapter():
    return None


def detail_plan():
    return None