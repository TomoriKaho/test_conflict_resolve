"""课程资料检索助手：Git/GitHub 教学示例。"""

MATERIALS = [
    {"course": "智能化软件系统与工程", "title": "Lab1 Git合作"},
    {"course": "智能化软件系统与工程", "title": "课程讲义"},
    {"course": "程序设计基础", "title": "Python练习"},
]
# test
def search(keyword):
    return [item for item in MATERIALS if keyword.strip() in item["course"]]

if __name__ == "__main__":
    import sys
    keyword = sys.argv[1] if len(sys.argv) > 1 else "智能化"
    results = search(keyword)
    for item in results:
        print(f'{item["course"]}: {item["title"]}')
    if not results:
        print("未找到相关资料")
