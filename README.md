# booking
test repository for booking

## System Test Guidelines
Guidelines for how to install robot framework, create libraries, keywords and how to run tests.

### Robot Framework Installation 
1.	Install Python v3 https://www.python.org/downloads/ 
2.	Update pip in a terminal
      * python -m pip install --upgrade pip
3.	Use pip to install robot framework and required python libraries:
      *	pip install robotframework
      *	pip install robotframework-seleniumlibrary
4. Download chromedriver and put it in the PATH

### Naming Convention
Naming convention is mainly based on [PEP8](https://www.python.org/dev/peps/pep-0008/) 
*	class names: CapWords convention – **SeleniumExtensions()**
*	robot and py-files: small letters with underscore as separator – **selenium_extensions.py**
*	add _navigation to navigation files for page object - ***_navigation.py** 
*	folders: small letters and separate with underscore: **../html_components**
*	functions: lowercase, separated by underscores: **login_to_booking()**
*	variables: lowercase, separated by underscores: **first_name**
*	constants: defined in class level, uppercase, separated by underscores: **ROBOT_LIBRARY_SCOPE**
*   robot keywords and test cases: uppercase, separated by space: **Login**
 
### Code Layout 
https://www.python.org/dev/peps/pep-0008/#code-lay-out 
*	use 4 spaces per indentation level. 
*	use spaces instead of tabs. Python 3 does not allow mixing the use of tabs and spaces for indentation. 
*	maximum line length is 100 characters.
*	add a blank line at the end of python files but for robot files it’s not needed.
*	imports are on separate lines, however if imports are from one module they should be on one line: **from subprocess import Popen, PIPE** 
*	use single quote characters for strings, and use double quote character inside sting if needed: **xpath = ‘//button[text()=”next”]’**
*   robot framework allows keywords arguments to be separated by two spaces but to make it more readable and consistent with python indentation, use 4 spaces.

### Comments
*	remember to update comments when the code changes.
*	comments should be in English language only.
*	use inline comments sparingly.

### Documentation Strings
https://www.python.org/dev/peps/pep-0257/ 
*	reStructuredText is used as the docstring format.
*	Python functions which are used as robot framework keywords(decorated with @keyword) must have documentation which includes examples:

```python    
    @keyword
    @save_driver
    @run_on_failure
    def login(self, username, password):
        """login to booking
         
        This keyword logs into the booking
        with the input parameters. 
         
        :param username: username
        :param password: password

        Example:
        | Login | user@abc.com | pass123 |
        """ 
```      
*    Document has a one line description of the keyword which it starts right after the starting three double quotes.
*    Three double quotes in the end of the documentation should be on a separate line.
*    Robot keyword example should be as written here, keyword words starting with uppercase and space as separator: **| Login To Management | user@abc.com | pass123 | clinic A |**

### Page Object
Page objects are libraries written specifically for booking app. The aim is to provide a keyword per each functionality of each page. So when that keyword is called in a test, it does all the navigation to desired page and the functionality as well.
**page_objects** folder includes **booking**, **html_components**, **smoke_tests** folders and **base.py** class which is the parent class for all the page object classes.
*    Each page object class must inherit **Base** class directly or indirectly.
*    All python folders, recursively, must have \_\_init__.py file to make it as python module. The common_library_imports.robot file can access python modules as libraries since the python path is set in the run.py file with pythonpathsetter.
*    **html_components** includes keywords for custom UI html components
*    **smoke_tests** includes smoke tests for keywords
### Creating  Robot Keywords in Python
*    add **@keyword** decorator to the python function you wish to use as a robot framework keyword.
*    add **@save_driver** decorator when keyword would be use web browsers
*    add **@run_on_failure** decorator when SeleniumLibrary run_on_failure is needed.
*    any class that implements keywords must have the class variable **ROBOT_LIBRARY_SCOPE = 'GLOBAL'**
*    when using multiple decorators, **@keyword** must be on top of all others.
*    add a new smoke test in **smoke_test.robot** file for each keyword created when possible. The aim is to check that the new keyword does the desired functionality and it does'nt break other keywords from working. In order to run smoke tests, change the run.py file to point to smoke_tests folder. (by default it is pointing to test-specification folder) However don't commit the changes to the run.py, this is just intended for your testing.

```python    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    @keyword 
    @save_driver
    @run_on_failure
    def log_out(self):
```
### Logging
For logging use robot [logger API](https://robot-framework.readthedocs.io/en/latest/autodoc/robot.api.html#module-robot.api.logger). In case there's a need to format text of the log, use Python [Format String Syntax](https://docs.python.org/2/library/string.html#format-string-syntax). The Python format does the type conversion automatically.
### Class init functions, super() and arguments
In existing Python code you can see classes which have \_\_init__ methods calling their superclass's \_\_init__ method in order to inherit the information and functionality the superclass has implemented. However, in Python the super() function does not always call the superclass of a class. In fact, it calls the next class in the MRO (Method Resolution Order) which may create the illusion of calling the superclass. In cases of multiple inheritance there is bound to be a step where a call to super(myClass, self).\_\_init__() will actually call a class sibling's or even sibling offspring's class \_\_init__. This will create problems at least if you are passing arguments to the \_\_init__ method: there will be a mismatch between the number of arguments passed and expected. To avoid these problems:
*    do **NOT** inherit your class from more than one superclass
*    do **NOT** require arguments to be passed to __init__ methods
### Exceptions
Raise Python [Built-in Exceptions](https://docs.python.org/2/library/exceptions.html).
When there's no appropriate exception use **ValueError**.
### Common
Common directory contains **common_library_imports.robot** and **common_variables.py**
#### common_library_imports.robot
common_library_imports.robot contains references to all the libraries, page objects and common variable file. Robot tests resources need to use common_library_imports.robot as their Resource in the settings in order to be able to find the keywords.
#### common_variables.py
Global robot variables and testing environments(which would be used in run.py for running tests) are defined in the common_variables.py.
### How to run tests
*    add **Tags** to robot test suites. They can be added as **[Tags]** to the test case or specified in **Force Tags** in the **Settings** of the test suite. **run.py** finds these tags and run tests based on the given tags.
*    specify which environment you want to run the test against by setting **variablefile** in the **run.py**. eg: variablefile='resources/common/variable_file/common_variables.py:**dev**'
*    open a terminal in the system-test root directory and run **python3 run.py tag_of_the_test_to_run** eg: python3 run.py login
*    results of the test are stored in the **output** directory. Each time a new test is run the **output** directory is deleted and recreated. So in case you need to keep the evidence of a test result, remember to copy the output folder to another destination before running a new test.
### Useful links
*    [Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
*    [Robot Framework Quick Start Guide](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst)
*    [Robot Framework Installation Instructions](https://github.com/robotframework/robotframework/blob/master/INSTALL.rst)
*    [SeleniumLibrary Keywords](http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
*    [SeleniumLibrary Github](https://github.com/robotframework/SeleniumLibrary)
