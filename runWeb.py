'''web端用例执行入口'''
import pytest
'''运行所有的用例'''
pytest.main(['-s','-vv','--alluredir','./report/xml'])

'''运行某一个文件的用例'''
