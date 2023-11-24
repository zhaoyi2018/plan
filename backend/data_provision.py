from datetime import datetime
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


def create_new_plan():
    return None


def delay_plan():
    return None


def speed_up_plan():
    return None


def add_new_chapter():
    return None


def delete_chapter():
    return None


def detail_plan():
    return None