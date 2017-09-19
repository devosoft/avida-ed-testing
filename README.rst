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

IMPORTANT:

One of the most important things to be conscious of during the installation process is that you are always using the correct Python interpreter. Almost all Mac users and many Windows users will already have a Python 2.7 installation on their computer, which will NOT be able to run this testing project. If Python 2.7 is already installed on your computer, Python-related commands will be run using 2.7 by default.

You can determine which is the default interpreter by running the command ``which python`` (for Mac) or ``where python`` (for Windows) from a command prompt window. If the path that these commands output contains ``python36``, you should be fine -- if it contains ``python27`` instead, you will need to be careful.

If you are on a Mac, you should just be able to affix a '3' to any Python-related command on the command line; for example, ``python3`` instead of ``python`` or ``pip3`` instead of ``pip``.

If you are on Windows, this is more complicated. Assuming that you already have Python 3.6 installed, the best way to launch Python is using the Python Launcher for Windows. To do this, instead of using ``python`` on the command line, use ``py -3`` for Python 3.6 or ``py -2`` for Python 2.7. Note that this ONLY works if you have at least one version of Python >= 3.3 installed on your computer. To use pip, you will either need to create a virtual environment (described below) or add C:\Path\to\Python36\Scripts to your PATH environment variable (see `this tutorial`_), which will allow you to use ``pip3.6`` instead of ``pip`` to ensure that you are always using the Python 3.6 version of pip.
Windows:

1. Install `Python 3.6`_. During the installation process, make sure that the option to also install pip_ is checked. Alternatively, you can install pip_ separately.
2. (Optional) Install PyCharm_ or another Python IDE of your choice.
3. If you have not already done so, download/clone this repository to your computer. If you plan on running the test suite locally (which is the default setting), you should also acquire a local version of the main `Avida-ED UI repository`_
4. Install any browsers that you plan to run the test suite with. This test suite currently supports Chrome_ and may support Firefox_ in the future.
5. If you are using Chrome, you will need to download Chromedriver_, the tool that allows Selenium to interact with Chrome. The directory where chromedriver.exe is located must also be added to your system path. See `this tutorial`_ on how to do this in Windows. If you are using Firefox, you will need to download Geckodriver_ and add its location to the system path -- however, you should be aware that not all tests run properly in Firefox at this time.
6. (Recommended) This project requires several specific Python packages to run properly. If you use or plan to use the Python 3 installation on your computer to do anything outside the scope of this project, it is helpful to isolate the package requirements for this project to prevent clashing of dependencies with other Python projects. This can be done with a virtual environment. It is possible to set up a project-specific virtual environment `through PyCharm`_, or you can create one manually (the virtualenv_ Python package would be useful for this -- install it via the command ``pip3 install virtualenv``).
7. Use pip to install the required packages listed in requirements.txt. This can be done easily by running the command ``pip install -r requirements.txt`` from the ``avida_ed_testing`` folder.
8. If you want to run the tests locally (which is the default setting), you will need to provide the location of the Avida-ED UI repository using the --setuipath option. More information about this option is given below. NOTE: You only need to use --setuipath the first time you run the experiment -- the location you give will be saved by the test suite.

Mac:

The installation process is essentially the same as for Windows. However, the process of adding something to the system path will be different -- this guide_ explains how you can do this. Also, it is important to make sure you are using the correct Python interpreter to run the test suite, since Macs tend to come with Python 2.7 installed. Please see the section marked IMPORTANT above for more information.

Use
----

The easiest way to run the tests is through the test suite files, located in the tests folder. The following command (simply typed into a command-line interface from the root folder of the project) will run all tests classified as 'basic':

``python tests/test_suite_basic.py``

There is also a test suite for tests that are considered 'advanced' -- however, this suite does not run any tests, because there are none marked as advanced. If you would like to inspect this file, it is located at ``tests\test_suite_advanced.py``.

It is possible to run a single test file (containing one or more test cases with a common purpose) using the following command:

``pytest path\to\test\testfile.py``

All of the tests are located within subdirectories of the ``tests`` folder within the ``avida_ed_testing`` folder. For example, there is a simple navigation test at ``tests\common\common_basic\navigaton\basic_nav_test.py``.

Alternatively, one can simply run ``pytest`` from the ``avida_ed_testing`` folder to run all of the tests from all of the test files.

There are also several command-line options that can be provided:

- --browser [BROWSER]\: Changes the browser used to run the tests. Current options are chrome (default) and firefox (not fully supported yet).

- --local [true/false]\: Sets whether the tests should be run on a local copy of Avida-ED (using a simple Python web server) or the copy hosted online by MSU. Providing "false" as the argument will run the tests on the MSU version, while any other input (or not specifying) will make the tests run locally.

- --setuipath [PATH]: Used to set the path to the Avida-ED UI repository, which is used to run the tests locally. You should provide the path to the folder containing the ``av_ui`` folder.

- --setffpath [PATH]: Used to set the path to the Firefox binary, which at this time is needed to run the tests via Firefox. However, this has not been thoroughly tested and Chrome is recommended to run tests at this time.

- --seturl [URL]: Used to set the URL for the online version on Avida-ED.

These options can be used when running individual tests or the test suite -- the test suite simply pipes all options given into Pytest.

.. _`Python 3.6`: https://www.python.org/downloads/
.. _pip: https://pypi.python.org/pypi/pip/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _`Avida-ED UI repository`: https://github.com/DBlackwood/av_ui
.. _Chrome: https://www.google.com/intl/en/chrome/browser/desktop/index.html
.. _Firefox: https://www.mozilla.org/en-US/firefox/new/
.. _Geckodriver: https://github.com/mozilla/geckodriver/releases
.. _Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
.. _`this tutorial`: https://www.java.com/en/download/help/path.xml
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _`through PyCharm`: https://www.jetbrains.com/help/pycharm/2017.1/creating-virtual-environment.html
.. _guide: https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/#.Waog9umQxPY
