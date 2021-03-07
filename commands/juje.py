import requests
import json

def getpfp(subreddit):
	subreddit_url = "https://reddit.com/"+subreddit+"/about.json"
	headers = {'User-agent': 'jujebot 1.0'}
	stvar = requests.get(subreddit_url, headers=headers)
	stvar = stvar.text
	stvar = json.loads(stvar)
	stvar = stvar["data"]
	if stvar["community_icon"] != "":
		pfp_url = stvar["community_icon"]
		pfp_url = pfp_url.split("?")[0]
	elif stvar["icon_img"] != "":
		pfp_url = stvar["icon_img"]
		pfp_url = pfp_url.split("?")[0]
	else:
		pfp_url = "http://resources.moddy.juje.si/reddit.png"

	return(pfp_url)
