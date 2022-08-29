## Web HeartMonitor on windows.

Thanks to [jlennox/Heartrate](https://github.com/jlennox/HeartRate).

## Running

1. Open /HRMonitor/HeartRate.exe.
2. Right click, Edit settings xml.
3. Find `<UDP>` Things. Fill it with "127.0.0.1:8909", like this:
```xml
...
  <HeartRateFile />
  <UDP>127.0.0.1:8909</UDP>
</HeartRateSettingsProtocol>
```
4. Unzip `Python_Data_Monitor\3104venv.7z` to `Python_Data_Monitor`.
4. Run Start.bat.
5. Open http://127.0.0.1:8919.

All Right.
