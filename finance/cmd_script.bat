C:\AppData\python\flask\Scripts\Activate.bat
pushd E:\Works\httprunner3\cases\src\finance
set PATH=%PATH%;E:\Works\httprunner3\framework\src
hrun3

pytest testcases --html=report/report.html --self-contained-html
report\report.html
