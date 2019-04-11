# 與笨蛋一起學習OPENCV
**此Git是在Udemy課程中學習到的筆記,方便自己之後可以回來進行複習或者是可以放自己亂寫的天馬行空**

## 安裝Anaconda 的虛擬環境
首先在開始進行任何一個課程先需要將Anaconda的虛擬環境安裝好
再透過下方的command來建立基本的虛擬環境, 可以透過虛擬環境來幫我們控管程式的版別
```bash
conda create --name <env_name> python=<python_version>
```
--name -> 虛擬環境的名稱</br>
python= -> 虛擬環境裡面所使用Python的版本

透過此指令, Anaconda會很貼心的幫你把其他需要一起安裝的Library一起安裝上去
在真正安裝前也會先讓我們看到說有哪些會進行安裝或更新

<img src="https://snag.gy/0HEqlz.jpg" width="600" height="500" />

安裝完畢後, 可以透過下方的指令來開啟與關閉我們的虛擬環境

開啟環境</br>
`source activate <env_name>`

關閉環境</br>
`source deactivate <env_name>`

## 安裝OpenCV
我們可以透過Anaconda的官方網站所提供的安裝方式, 輕鬆簡單地進行安裝</br>
以下可以選任何一個進行安裝</br>
`conda install -c conda-forge opencv `</br>
`conda install -c conda-forge/label/gcc7 opencv `</br>
`conda install -c conda-forge/label/broken opencv `</br>
`conda install -c conda-forge/label/cf201901 opencv `</br>
[Conda官方文件](https://anaconda.org/conda-forge/opencv)


## 確認OpenCV是否安裝成功
透過以下的方式可以讓我們檢查是否有成功將OpenCV安裝完成
![](https://snag.gy/9rzsVg.jpg)
