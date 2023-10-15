# lambda 變數1, 變數2, 變數3....:運算式

Ex1.
lambda x, y, z:x+y+z

Ex2.(變數(值))
book=lambda x, y, z:x+y+z
print(book(1,2,3))

Ex3. ((浪打函式)())
print((lambda x, y, z:x+y+z)(1,2,3))

Ex4.   串列= [1,2,4,2,5,6,7]
      定義1 =定義2(浪打函數 變數:運算式,串列)
number = [1,2,3,3,5,4,5,5]
kb=ka(lambda a:a<3, number)   #條件判斷
  print(kb)
  print(list(ka))..


# list() :清單列出
# sorted() :排序
----------------------------------------------------------------------
# Lambda函式 vs 一般函式(Function)

# Lambda函式與一般函式(Function)的差異為：
# Lambda函式不需要定義名稱，而一般函式(Function)需定義名稱
# Lambda函式只能有一行運算式，而一般函式(Function)可以有多行運算式
# Lambda在每一次運算完會自動回傳結果，而一般函式(Function)如果要回傳結果要加上 return 關鍵字
-----------------------------------------------------------------------

#三件套
# 1. map 將串列傳入進行運算 2. filter 篩選 3. reduce

# [map]
# map()內建方法會將串列(List)中的每個元素傳入Lambda函式進行特定的運算，最後回傳每個元素的運算結果

def get_name(student):
      return student["name"]
print(list(map(get_name,student)))

# 利用 lambda 匿名模式 ，可進行優化

# print(list(map(get_name,student)))
# --定義式，用lambda改寫-->
print(list(map(lambda s:s["name"], student)))
---------------------------------------------------------------------------

# [filter] 判斷式，優化
# filter()：在可疊代的物件中，依據條件運算式，選擇特定的元素，語法為：

# filter(lambda parameter: expression, iterable)

# filter()內建方法會將串列(List)中的每個元素傳入Lambda函式進行條件判斷，最後回傳符合條件的元素

# student = []
# for s in student:
#    if s["score"] >= 60:
#        student.append(s)
# print(student)
#
# 改成if else
# def check_Pass(student):
#      if s["score"] >= 60:
#            return True
#      else:
#            return Flase
# print(list(filter(check_Pass, student)))

# 優化
# 
# def check_Pass(student):
#      return True if student["score"]>=60 else False
# print(list(filter(check_Pass, student)))

# Return 優化
# print(list(filter(lambda s : True if student["score"]>=60 else False, student)))

# [reduce] 多重 lambda 簡化
# reduce()：與map()內建方法同樣在可疊代的物件中，套用特定運算式於每一個元素，但是內部的實作方式不一樣，它的實作步驟為：
# 將可疊代物件中的前兩個元素先進行Lambda運算式的運算。
# 接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算。
# 依此類推，直到可疊代物件的元素都運算完成。
# 也因為每一次的運算都是兩個元素傳入，所以語法為：
# reduce(lambda parameter1, parameter2: expression, iterable)

# 使用reduce()內建方法時，記得引用functools模組

# vals =[1,2,3,4,5]
# def reduce_func(x,y):
#      print(x,y):
#      return x+y
# print(reduce(reduce_func, vals))

# 1跟2運算完，再跟3，再跟4，再跟5   =  >  reduce 也就是累加運算 (第一個條件算完，再算第二個條件)

# 方法 (lambda 函式, 串列)
# Q:直接拿取及格學生的姓名?
list(filter(lambda s: True if s["score"]>= 60 else Flase, student))
# 及格 student 就是list串列
list(map(lambda s: s["name"], list(filter(lambda s: True if s["score"]>= 60 else Flase, student))))
#
print(list(map(lambda s: s["name"], list(filter(lambda s: True if s["score"]>= 60 else Flase, student)))))

