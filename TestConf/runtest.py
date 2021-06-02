import os

import pathlib
from datetime import datetime

time = str(datetime.today().strftime('%Y-%m-%d'))

# read counter
path = pathlib.Path(__file__).parent / "counter.txt"
f = open(path, 'r+')
data = int(f.read())
# update counter
newCounter = str(data + 1)
# write new counter
f.seek(0)
f.write(newCounter)
f.truncate()
f.close()








#For running testCases
# command = "pytest --alluredir=ReportAllure/"+ time + "_" + readNewData + " --html=ReportHtml/report_"+ time + "_" + readNewData + ".html --self-contained-html" + " " + "TestCase"
command = "pytest -s  " + "TestCase"
os.system(command)