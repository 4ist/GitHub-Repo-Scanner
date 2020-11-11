# GitHub Repo Scanner

This is a python application that scans a specified GitHub source repository with CLOC and (optionally) sends the CLOC scan output via email.

## Setup
The application can be executed by running `python main.py` in the root directory.
The application depends on the following software:
    - [CLOC](http://cloc.sourceforge.net/)
    - [Git](https://www.python.org/)
    - [Python](https://git-scm.com/)
    - [Perl](https://www.perl.org/)
    
## Configuration
There are several configuration options in the json files of the config directory. 
- public-config.json
    - Target repository URL
    - Declare OS-specific system commands (ex: `rmdir /s /q` or `rm -rf`)
    - Email options (leave recipient blank to skip emailing the CLOC scan result)
- private-config.json 
    - SMTP username and password
    - note that this file is ignored in .gitignore such that it can contain sensitive information that belongs outside of source control.
