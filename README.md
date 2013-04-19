GitHub2Wiki - 2013
===========

# System Requirements 
Script Updater was written in Python 2.7. Python can be downloaded online at http://python.org/download/
If running on Windows, you'll probably need to install Python. If running most linux distributions, it is most likely already installed.

# Configuration 
In the github2wiki.py file, there is a section that is a User Configuration section
Example:

wikiUser   = 'Foo'
wiki       = 'http://bar.wikia.com'
savePage   = 'Awesome Code Here'

scriptLocation = "https://raw.github.com/username/reponame/master/filename"


wikiUser is your wiki username
wiki is the wiki it will update the script on. If working on one with the api on a location other than /api.php, add the directory to the wikiname
savePage is the page where the code will be saved to.
scriptLocation is where on github the script is currently located

# Usage 
python github2wiki.py

This will run it based on the config inserted into the file.

# License 
This program is licensed under the GNU General Public License (GPL) version 3. The full text of the license can be found in the "LICENSE" file provided in the source code.

# Source Code 
The source code can be found online at https://github.com/ty-a/github2wiki

# Contributors 
* TyA <tya.wiki@gmail.com>