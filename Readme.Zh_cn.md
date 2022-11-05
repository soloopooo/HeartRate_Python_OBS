## Web HeartMonitor on windows.

[English](Readme.md)

感谢 [jlennox/Heartrate](https://github.com/jlennox/HeartRate).

## 运行方式

1. 克隆此仓库或直接下载 Zip。
1. 首先打开 /HRMonitor/HeartRate.exe。
2. 右键单击界面, 选择 Edit settings xml。
3. 找到 `<UDP>` 所在区域. 填入 "127.0.0.1:8909", 如下所示:
```xml
...
  <HeartRateFile />
  <UDP>127.0.0.1:8909</UDP>
</HeartRateSettingsProtocol>
```
4. 第一次配置，请运行如下命令:(推荐Powershell)
```bash
cd .\Python_Data_Monitor\
python -m venv .\3104venv\
.\3104venv\Scripts\activate
python -m pip install -r .\PyScripts\requirements.txt
```
4. 双击 start.bat 运行。
5. 浏览器打开 http://127.0.0.1:8919。

** 更推荐使用Websocket版本，而非Js轮询版本。 **

结束。

## 如何自定义可视化 html:

将你写的html文件放入 `Pyscripts/www`. 

推荐使用Websocket，ws://127.0.0.1:8919/ws/hr_json,

网页api位于 http://127.0.0.1:8919/api/hr_json.

可以在 `Pyscripts/js` 里加入你的js文件，

当服务器运行时文件将自动被挂载。

打开 http://127.0.0.1:8919/{你的html名}.html 查看效果。

## 如果我没有可使用的心率监测设备，怎么预览效果？

很简单。

只需要运行`test.bat`，不用运行`Heartrate.exe`。

它会把随机数据发送到UDP端口，然后运行`start.bat`并打开网页即可预览效果。

Gif：

![5wec2-ge0kv](https://user-images.githubusercontent.com/36123081/189464877-2ba3af54-a36d-4c26-b3f0-7f31150c8aa6.gif)

## 寻求帮助

<s>Websocket咋用啊?</s>

暂时没了...
