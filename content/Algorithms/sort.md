date: 2015-11-16
author: YiHan
title: 排序算法
tags: Algorithms, sort, python

##优先队列
一句话：

##堆排序
时间复杂度： 2NlogN
一句话： 对

主要的优点在于能够同时最优使用空间，时间，最坏情况下是2NLOGN  
缺点在于不能很好利用缓冲，因为他的比较是跳跃的，而不是与周围的数据进行比较

堆这种数据结构还是主要用于优先队列中，每次只需要加载部分数据进入内存，就可以完成大数据量的处理，比如TOP10， 只需要维护一个10元素的数组，然后增量的处理数据就可以了。
