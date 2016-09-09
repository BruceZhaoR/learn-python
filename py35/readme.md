## py27与py35共存window解决办法

**添加环境变量就不用在强调了**

1. 将Python35文件夹下的`Python.exe` 改为`python35.exe`, 看个人喜好
2. `python35 -m pip --version`
3. `python35 -m pip install -U pip`
4.  `pip3 -V`
5.  `pip3 install numpy`

看以看到已经将装包的文件夹设为 `site-packages`

## IDLE 清屏

打开`Python35-> Lib ->idlelib -> config-extensions.def`
末尾加上：

```def
[ClearWindow]
enable=1
enable_editor=0
enable_shell=1
[ClearWindow_cfgBindings]
clear-window=<Control-Key-l>
```
保存

然后再把此文件夹下的 `ClearWindow.py` 放在`idlelib`文件夹里面就ok了~~

打开python的idle，看看options是不是多了一个选项`clear shell window ctrl+L`

## 安装 scipy scikit-learn

首先安装这个 numpy + mkl :  http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

其次安装  http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy

最后安装  http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-learn

## 爬虫框架 pyspider

scrapy python3.3 以上 windows 安装不了。主要原因是 Twiste

pyspider http://docs.pyspider.org/en/latest/Quickstart/
https://github.com/binux/pyspider

爬虫工具介绍： http://www.wtoutiao.com/p/17508iO.html

