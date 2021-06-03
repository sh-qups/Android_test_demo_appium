import os

import pathlib
from datetime import datetime
from delreport import deletereports

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

# For running testCases

command = "pytest -s  --alluredir=ReportAllure/" + time + "_" + newCounter + " --html=ReportHtml/report_" + time + "_" + newCounter + ".html --self-contained-html" + " TestCase"
os.system(command)


# delete htmlfiles and reportfolder except last nth number
number = 2
deletereports(number)


# For serving report

command = "allure serve " + "ReportAllure/" + time + "_" + newCounter
os.system(command)


# For single run

# python3 -m unittest TestCase.test_01_intro_to_home
# python -m pytest -s TestCase/test_01_intro_to_home.py --alluredir=ReportAllure &&  allure serve ReportAllure/



