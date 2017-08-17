========================
Avida-ED Testing Project
========================

Introduction
------------
This project contains a test suite for the web-based version of Avida-ED_, an award-winning educational application developed at `Michigan State University`_ for undergraduate biology courses to help students learn about evolution and scientific method by allowing them to design and perform experiments to test hypotheses about evolutionary mechanisms using evolving digital organisms.

.. _Avida-ED: https://avida-ed.msu.edu/
.. _`Michigan State University`: https://msu.edu/

This project uses Selenium to run automated tests in a web browser against the Avida-ED application (running either locally or on the Internet). The test suite is being developed mainly with Chrome in mind, but tests should be runnable in Firefox at some future point.

Installation
------------
Windows:

1. Install `Python 3.6`_. During the installation process, make sure that the option to also install pip_ is checked. Alternatively, you can install pip_ separately.
2. (Optional) Install PyCharm_ or another Python IDE of your choice.
3. If you have not already done so, download/clone this repository to your computer. If you plan on running the test suite locally, you should also acquire a local version of the main `Avida-ED UI repository`_
4. Install any browsers that you plan to run the test suite with. This test suite currently supports Chrome_ and will support Firefox_ in the future.
5. If you are using Chrome, you will need to download Chromedriver_, the tool that allows Selenium to interact with Chrome. The directory where chromedriver.exe is located must also be added to your system PATH. See `this tutorial`_ on how to do this in Windows. Instructions for Firefox will be included at a later date.
6. Use pip to install the required packages listed in requirements.txt. This can be done easily by running the command ``pip install -r requirements.txt`` from the ``avida_ed_testing`` folder.  If you would like to isolate the project's requirements from those of any other Python projects (highly recommended), you can use the virtualenv_ package to create a Python virtual environment. This can also be done `through PyCharm`_.
7. If you want to run the tests locally (which is the default setting), you will need to provide the location of the Avida-ED UI repository in your first run. See below for details.

Use
----

The easiest way to run the tests is through the test suite files, located in the tests folder. The following command (simply typed into a command-line interface from the root folder of the project) will run all tests classified as 'basic':

``python tests/test_suite_basic.py``

There is also a test suite for tests that are considered 'advanced' -- however, this suite a) is currently outdated and b) does not run any tests, because there are none marked as advanced.

It is possible to run a single test file (containing one or more tests with a common purpose) using the following command:

``pytest path\to\test\testfile.py``

All of the tests are located within subdirectories of the ``tests`` folder within the ``avida_ed_testing`` folder. For example, there is a simple navigation test at ``tests\common\common_basic\navigaton\basic_nav_test.py``.

Alternatively, one can simply run ``pytest`` from the ``avida_ed_testing`` folder to run all of the tests from all of the test files. In the future, there will be test suites for running specific groupings of tests -- however, this has not been implemented yet.

There are also several command-line options that can be provided:

- --browser\: Changes the browser used to run the tests. Current options are chrome (default) and firefox (not fully supported yet).

- --local\: Sets whether the tests should be run on a local copy of Avida-ED (using a simple Python web server) or the copy hosted online by MSU. Providing "false" as the argument will run the tests on the MSU version, while any other input (or not specifying) will make the tests run locally.

- --setuipath: Used to set the path to the Avida-ED UI repository, which is used to run the tests locally. You should provide the path to the folder containing the ``av_ui`` folder.

- --setffpath: Used to set the path to the Firefox binary, which at this time is needed to run the tests via Firefox. However, this has not been thoroughly tested and Chrome is recommended to run tests at this time.

- --seturl: Used to set the URL for the online version on Avida-ED.

These options can be used when running individual tests or the test suite -- the test suite simply pipes all options given into Pytest.

.. _`Python 3.6`: https://www.python.org/downloads/
.. _pip: https://pypi.python.org/pypi/pip/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _`Avida-ED UI repository`: https://github.com/DBlackwood/av_ui
.. _Chrome: https://www.google.com/intl/en/chrome/browser/desktop/index.html
.. _Firefox: https://www.mozilla.org/en-US/firefox/new/
.. _Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
.. _`this tutorial`: https://www.java.com/en/download/help/path.xml
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _`through PyCharm`: https://www.jetbrains.com/help/pycharm/2017.1/creating-virtual-environment.html
