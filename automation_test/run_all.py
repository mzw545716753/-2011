import unittest
from common import htmlTestRunner_cn

casePath = r"E:\python\automation_test\ui_case"

rule = "zw_test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

ropertpath = r"E:\python\automation_test\\ui_import\\"+"ropoert.html"

fp = open(ropertpath,"wb")

runner = htmlTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="uitest",
                                       description="自动化测试报告")
runner.run(discover)

fp.close()