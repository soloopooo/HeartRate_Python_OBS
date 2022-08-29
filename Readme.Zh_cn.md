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
4. 将 `Python_Data_Monitor\3104venv.7z` 解压到 `Python_Data_Monitor`。
4. 双击 start.bat 运行。
5. 浏览器打开 http://127.0.0.1:8919。

结束。
