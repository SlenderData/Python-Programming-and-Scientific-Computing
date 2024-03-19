# 当前日期：2024-03-19
# 姓名：马云骥
# 从users模块导入Admin类，并测试其功能

from users import Admin

# 创建一个Admin实例
admin = Admin('王', '五')
# 显示管理员权限
admin.privileges.show_privileges()
