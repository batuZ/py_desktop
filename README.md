# 在xcode中写pyhton桌面程序

### 依赖
* 库管理pipenv
* UI框架PYQT5
* 打包PyInstaller

### 初始化环境 | 使用设计工具 | 导出py文件 | 打包exe

    1、```pip install pipenv``` //安装库版本管理工具
    
    2、```pipenv install``` 安装依赖

    3、 ```.\ui_designer.bat``` 打开桌面设置工具

    4、 ```.\ui_designer.bat .\UI\root.ui``` 打开设计模板root.ui

    5、```.\ui_to_py.bat .\UI\root.ui .\UI\root.py``` 把设置模板转成py

    6、 ```.\build.bat main.py``` 打包exe

### 参考资料

https://blog.csdn.net/qq_39241986/article/details/112791986

http://www.bl186.net/