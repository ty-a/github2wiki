##########################################################################
# Github2Wiki- Updates script on wiki based on GitHub version. 
#    Copyright (C) 2013  TyA <tya.wiki@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

import cookielib
import getpass
import json
import sys
import urllib
import urllib2

# Start User Configuration
wikiUser   = 'Kangaroopower'                        # User uploading the script
wiki       = 'http://kangaroopower.wikia.com'       # Script adds the /api.php so please don't add it here
savePage   = 'MediaWiki:Scope.js/dev.js'            # Where to save the code to

scriptLocation = "https://raw.github.com/Kangaroopower/Scope/master/Scope.js" # Location of the script
# End User Configuration

cookiejar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
opener.add_headers = [('User-Agent','Github2Wiki - Running as ' + wikiUser)]

def post(data):
	"""
	POSTs content to the wiki's API in json format

	:param data (dict): An dict of what is being posted.
	:returns: the response from the API
	"""
	
	data = urllib.urlencode(data)
	response = opener.open(wiki + '/api.php', data)
	response = response.read()
	response = json.loads(response, 'utf-8')
	return response
	
def login(username, password):
	"""
	Logins into the wiki via API

	:param username (str): The username of the user
	:param password (str): The user's password
	:returns: boolean based on success
	"""
		
	data = {
		"action":"login",
		"lgname":username,
		"lgpassword":password,
		"format":"json"
	}
	
	response = post(data)
	
	logintoken = response["login"]["token"]
	
	data = {
		"action":"login",
		"lgname":username,
		"lgpassword":password,
		"lgtoken":logintoken,
		"format":"json"
	}
	
	response = post(data)
	print response
	
	if response["login"]["result"] == "Success":
		print "Now logged in"
		return True
	else:
		print response["login"]["result"]
		sys.exit(0)
		return False
		
		
def getEditToken():
	"""
	Gets the edit token
	
	:param: none
	:returns: The edit token or False
	"""

	data = {
		"action":"query",
		"prop":"info",
		"intoken":"edit",
		"titles":"Main Page",
		"format":"json"
	}
	
	response = post(data)
	response = response["query"]["pages"].values()
	
	for token in response:
		try:
			edittoken = token["edittoken"]
		except: 
			return False
		
	return edittoken

def edit(page, content, summary='Updating script', bot=1):
	"""
	Makes the actual edit to the page
	
	:param page (str): The page to edit
	:param content (str): What to put on the page
	:param summary (str): The edit summary (Default: 'Updating script')
	:param bot (bool): Mark the edit as a bot or not (Default: 1)
	:returns: boolean based on success
	"""
	
	edittoken = getEditToken()
	if edittoken == False:
		print "Unable to aquire edit token - aborting"
		return False
	
	data = {
		"action":"edit",
		"title":page,
		"summary":summary,
		"text":content,
		"bot":bot,
		"token":edittoken,
		"format":"json"
	}
	
	response = post(data)
	
	try:
		print response["error"]["info"]
		return False
	except:
		return True
		

wikiPassword = getpass.getpass("Wiki password: ")

login(wikiUser, wikiPassword)

page = opener.open(scriptLocation)
page = page.read()

# page.replace("What to find", "What to replace it with")
page = page.replace("Edge", "Alpine")
page = page.replace("raw.github.com/Kangaroopower/Scope/master/Dialog.js", "kangaroopower.wikia.com/wiki/Mediawiki:Dialog.js?action=raw&ctype=text/javascript&maxage=0&smaxage=0")

summary = raw_input("Edit summary [Updating script]: ")
if summary == '':
	edit(savePage,page)
else:
	edit(savePage,page,summary)