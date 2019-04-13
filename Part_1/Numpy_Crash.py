import numpy as np

# 這是定義List的方式
this_is_list = [1,2,3,4,5] # list type

# 這是定義Numpy array的方式 
this_is_arr = np.array([1,2,3,4,5]) # array type

# 也可以透過.array()的方式將一般的List轉換成array
list2arr = np.array(this_is_list) # array type

# 之前如有需要產生連續數字的list時我們需要透過for loop的方式才能產生
this_is_num_list = [x for x in range(10)] # [0,1,2,3,4,5,6,7,8,9]

# Numpy有提供比較簡單的方式讓我們可以快速產生numpy array
this_is_num_arr = np.arange(0,10) # [0 1 2 3 4 5 6 7 8 9]

# 也可以透過Step的方式產生我們要的array
this_is_num_arr_2 = np.arange(0,10,2) # [0 2 4 6 8]

# 快速產生0或1的 array
this_is_zeros = np.zeros(5) # [0 0 0 0 0]
this_is_ones = np.ones(5) # [1 1 1 1 1]

# Operations 

# 透過seed, 我們可以控制random產生出來的數值一直都維持是一樣的
# https://snag.gy/imUPD6.jpg
arr_add = np.array(this_is_list)
print(arr_add)
print(arr_add + 1)
np.random.seed(101)
for x in range(5):
     create_random_num = np.random.randint(0,100,10)

arr = np.random.randint(0,100,10)
# Max
arr.max()
# Min
arr.min()
# Mean
arr.mean()
# Max location
arr.argmax()
# Min location
arr.argmin()
# 透過np.reshape的功能,我們可以很方便的改變成我們想要的shape
arr.reshape(2,5)

# Indexing
mat = np.arange(0,100).reshape(10,10)
print(mat)
# 可以透過Row & Column來選擇我們要選取的區塊
# mat[row,col]

# 第一排的所有值
print(mat[:,0])
