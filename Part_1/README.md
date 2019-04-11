# 1. Numpy and Image Basic
**在這邊會介紹Numpy的一些基本使用方式以及Image的一些基本觀念**

**這是定義List的方式**</br>
```python
this_is_list = [1,2,3,4,5] # list type
```
**這是定義Numpy array的方式**</br>
```python
this_is_arr = np.array([1,2,3,4,5]) # array type
```
**也可以透過.array()的方式將一般的List轉換成array**</br>
```python
list2arr = np.array(this_is_list) # array type
```
**之前如有需要產生連續數字的list時我們需要透過for loop的方式才能產生**</br>
```python
this_is_num_list = [x for x in range(10)] # [0,1,2,3,4,5,6,7,8,9]
```
**Numpy有提供比較簡單的方式讓我們可以快速產生numpy array**</br>
```python
this_is_num_arr = np.arange(0,10) # [0 1 2 3 4 5 6 7 8 9]
```
**也可以透過Step的方式產生我們要的array**</br>
```python
this_is_num_arr_2 = np.arange(0,10,2) # [0 2 4 6 8]
```
**快速產生0或1的 array**</br>
```python
this_is_zeros = np.zeros(5) # [0 0 0 0 0]
this_is_ones = np.ones(5) # [1 1 1 1 1]
```
**接下來是介紹一些Operations**</br>
**如果之前要將 list 裡所有的值都+1的話, 需要透過lopp的方式一個一個加起來**
**現在透過numpy array就可以直接進行加減乘除的動作**
```python
add_list = np.array(this_is_list)
add_one = add_list + 1
```
**我們可以透過row,column來抓取Numpy Matrix 底下的值**</br>
```python
mat = np.arange(0,100).reshape(10,10) # 建立出(10,10)的matrix
# mat[row,col]
```

# Image with Numpy
Numpy 可以透過 `np.asarray()` 的方式來將圖片轉換成 array type
```python 
