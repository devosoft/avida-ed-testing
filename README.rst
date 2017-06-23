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
3. If you have not already done so, download this repository to your computer.
4. Install any browsers that you plan to run the test suite with. This test suite currently supports Chrome_ and will support Firefox_ in the future.
5. If you are using Chrome, you will need to download Chromedriver_, the tool that allows Selenium to interact with Chrome. The directory where chromedriver.exe is located must also be added to your system PATH. See `this tutorial`_ on how to do this in Windows. Instructions for Firefox will be included at a later date.

There will be more steps later once this README is complete.

.. _`Python 3.6`: https://www.python.org/downloads/
.. _pip: https://pypi.python.org/pypi/pip/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _Chrome: https://www.google.com/intl/en/chrome/browser/desktop/index.html
.. _Firefox: https://www.mozilla.org/en-US/firefox/new/
.. _Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
.. _`this tutorial`: https://www.java.com/en/download/help/path.xml