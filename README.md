# FrontEndFramework
This is a personal project for testing a dummy web page.

# Prerequisites
1. At least Python3.6 installed.
2. Pytest should be installed. (run "pip install pytest")
3. A driver should be configurend in PATH. You can use the chromedriver from driver folder. (ex. C:\workspace\FrontEndFramework\drivers\)
4. A PYTHONPATH should be created in System Variables (for Windows)
ex.: C:\Python39\Lib;C:\Python39\DLLs;C:\Python39\Lib\lib-tk;..\;
5. Add in PATH from System Variables the PYTHONPATH that you just created. 
ex.: ;%PYTHONPATH%;

# Run
1. Run all tests by running "pytest".
2. Run a test by a specific category by running "pytest -m category".
3. Run a particular set of tests by running 'pytest -m "category1 or category2"'
4. Check all custom markers by 'pytest --markers'.