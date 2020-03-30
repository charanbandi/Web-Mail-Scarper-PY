import urllib,re

sites = ["site1","site2"]

for site in sites:
	f = urllib.urlopen(site)
	s = f.read()
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
	newemails = list(set(emails))
	print newemails