import os.path

import pytest_html
from icecream import ic
import toml


def pytest_html_report_title(report):
    report.title = "HttpRunner3 接口自动化测试演示!"
    config_file_path = "{}{}{}".format(os.path.curdir, os.path.sep, "httprunner3.toml")
    if os.path.exists(config_file_path):
        config_dict = toml.load(config_file_path)
        if config_dict.get("Report", None):
            if config_dict["Report"].get("Title", None):
                report.title = config_dict["Report"]["Title"]


def pytest_generate_tests(metafunc):
    print("metafunc", metafunc)
    print("metafunc.fixturenames", metafunc.fixturenames)
    if "one_ele" in metafunc.fixturenames:
        # metafunc.parametrize("from_ls", metafunc.config.getoption("stringinput"))
        metafunc.parametrize("one_ele", ["a", "b"])


if __name__ == "__main__":
    class MockReport:
        title = None

    _report = MockReport()
    pytest_html_report_title(_report)
    ic(_report.title)
