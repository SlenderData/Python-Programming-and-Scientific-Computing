# 假设有列表 list_student=[[“001”,”李元芳”，19],[“002”,”刘禅”,20],[“003”,”张三丰“，18]]，依次存放了每名学生的学号、姓名和年龄。
# 试编写程序，实现以下功能：
# (a) 在列表末尾添加学生信息：学号“004”，姓名“柯镇恶”，年龄19；学号“006”，姓名“十三郎”，年龄20。
# (b) 在列表的适当位置添加如下的学生信息：学号“005”，姓名“唐涤生”，年龄20。
# (c) 输出学号为003的学生信息。
# (d) 输出所有学生的姓名。
# (e) 输出年龄大于19的所有学生的信息。

list_student = [['001', '李元芳', 19], ['002', '刘禅', 20], ['003', '张三丰', 18]]
print("原始列表:", list_student)

# (a) 在列表末尾添加学生信息：学号“004”，姓名“柯镇恶”，年龄19；学号“006”，姓名“十三郎”，年龄20。
list_student.append(['004', '柯镇恶', 19])
list_student.append(['006', '十三郎', 20])
print("\n添加后的列表:", list_student)

# (b) 在列表的适当位置添加如下的学生信息：学号“005”，姓名“唐涤生”，年龄20。
list_student.insert(4, ['005', '唐涤生', 20])
print("\n插入后的列表:", list_student)

# (c) 输出学号为003的学生信息。
for student in list_student:
    if student[0] == '003':
        print(f"\n学号为003的学生信息：{student}")

# (d) 输出所有学生的姓名。
student_names = []
for student in list_student:
    student_names.append(student[1])
print(f"\n姓名：{student_names}")

# (e) 输出年龄大于19的所有学生的信息。
students_over_19 = []
for student in list_student:
    if student[2] > 19:
        students_over_19.append(student)
print("\n年龄大于19的学生信息:", students_over_19)