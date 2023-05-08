# Github-Freshdesk-connection

Project based on the task in ```task.pdf```

## Project structure

```main.py``` - the main executable file <br>
```tests.py``` - unittests that cover most of the functionalities <br>
```requirements.txt``` - the additional needed dependencies to run the project <br>
```source/``` - folder with additional source code <br>
&emsp;&emsp;&emsp; ```arguments_parsing.py``` - checking and parsing arguments <br>
&emsp;&emsp;&emsp; ```token_configuration.py``` - extracting the 2 tokens <br>
&emsp;&emsp;&emsp; ```helper_functions.py``` - additional helping functions <br>
&emsp;&emsp;&emsp; ```database.py``` - database configuration <br>

## Prerequisites

* installed [Python](https://www.python.org/downloads/)
* installed [pip](https://pypi.org/project/pip/) (If you have Python 3.4 or later, pip is included by deafult)
* installed modules from requirements.txt (Execute ```pip install -r requirements.txt```)

## Run project

1. Make sure you have environmental variables ```GITHUB_TOKEN``` and ```FRESHDESK_TOKEN```. Make file ```source/.env``` with
   content 
```bash
GITHUB_TOKEN=<token> 
FRESHDESK_TOKEN=<token>
```
2. Execute ```python main.py <github_username> <freshdesk_domain>```
