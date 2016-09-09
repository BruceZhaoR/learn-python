# py27与py35共存window解决办法

**添加环境变量就不用在强调了**

1. 将Python35文件夹下的`Python.exe` 改为`python35.exe`, 看个人喜好
2. `python35 -m pip --version`
3. `python35 -m pip install -U pip`
4. `pip -V` `pip3 -V`

看以看到已经将装包的文件夹设为 `site-packages`
