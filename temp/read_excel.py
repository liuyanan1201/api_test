#1/导入 xlrd
import xlrd

#2/打开excel（work_book)
excel=xlrd.open_workbook("../data/data.xls")

#指定工作表
sheet=excel.sheet_by_name("登陆")#通过名字
sheet=excel.sheet_by_index(0)#第二种方法  第0个工作表

#读取信息
print(sheet.nrows)#有效数据行数
print(sheet.ncols)#有效数据列数


print(sheet.row_values(0)) #打印标题行
print(sheet.row_values(1))#打印第一行



#打印执行单元格数据
print(sheet.cell(0,0).value) #第一行第一列单元格的值
print(sheet.cell(1,0).value) #第二行第一列单元格的值

#练习1、打印所有注册模块的用例不要标题行

sheet1=excel.sheet_by_name("注册")#通过名字
for n in range(1,sheet1.nrows):
    print(sheet1.row_values(n))


