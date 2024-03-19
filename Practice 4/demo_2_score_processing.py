# 当前日期：2024-03-19
# 姓名：马云骥
# 处理学生的成绩数据

# 将学生学号及其总评成绩存储为对象
class StudentScore:
    def __init__(self, student_id, total_score):
        self.student_id = student_id
        self.total_score = total_score

    def __repr__(self):
        return f"StudentScore(student_id='{self.student_id}', total_score={self.total_score})"


# 将数据保存到文件中，使用utf-8编码
with open('score.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("学号,平时成绩,期末成绩\n")
    file_object.write("9999180101,77,88\n")
    file_object.write("9999180102,91,85\n")
    file_object.write("9999180103,87,96\n")
    file_object.write("9999180104,70,68\n")
    file_object.write("9999180105,86,72\n")
print()

# 读取数据并计算总评成绩，同样指定utf-8编码
students_scores = []
with open('score.txt', encoding='utf-8') as file_object:
    lines = file_object.readlines()

for line in lines[1:]:  # 跳过标题行
    student_id, regular_score, final_score = line.strip().split(',')
    total_score = round(int(regular_score) * 0.4 + int(final_score) * 0.6)
    students_scores.append(StudentScore(student_id, total_score))

# 按总评成绩降序排列
students_scores.sort(key=lambda x: x.total_score, reverse=True)

# 将排名后的成绩保存到新文件，再次使用utf-8编码
with open('sorted_scores.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("学号,总评成绩\n")
    for student_score in students_scores:
        file_object.write(f"{student_score.student_id},{student_score.total_score}\n")
