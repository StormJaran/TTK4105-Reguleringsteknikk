#VideoInnholdsFortegnelses LatexSkaper
#Laget av Storm Westlie til bruk som studass i TTK4105 - Reguleringsteknikk

import os

def main():
	data = readDataFromFile()
	day = data.split('Ukedag: ')[1].split('\n')[0]
	date = data.split('Dato: ')[1].split('\n')[0]
	part = data.split('Time: ')[1].split('\n')[0]
	url = data.split('Url: ')[1].split('\n')[0]
	literature = data.split('Litteratur: ')[1].split('\n')[0]
	themes = data.split('Tema: ')[1].split('\n')[0]
	keywords = data.split('Dato: ')[1].split('\n')[0]
	bpList = createBulletPointList(url,data)
	latexCode = buildLatex(day, date, url, part, literature, themes, keywords, bpList)
	copyTextToClipboard(latexCode)
	print("\n *Latex-koden er kopiert til utklippstavlen.* \n *Ha en fin dag videre!*")

def readDataFromFile():
	f = open("forelesning.txt",'r')
	dataString = ""
	for line in f:
		dataString += line
	print(dataString)
	return dataString


def createBulletPointList(url,data):
	bps = data.split('---Kulepunkter---\n')[1].split('\n---Slutt---')[0]
	bps = bps.split('\n')
	bpList = []
	for bp in bps:
		time = bp.split(' - ')[0]
		formattedTime = (int(time.split(":")[0])*60 + int(time.split(":")[1]))*1000 #Index 0 er antall minutter, index 1 er antall sekunder, "?playfrom=formattedTime"
		text = bp.split(' - ')[1].split('\n')[0]
		bpList.append("\item \href{%s?playFrom=%s}{%s -- %s}" % (url, str(formattedTime), time, text))
	return bpList

def buildLatex(day, date, url, part, literature, themes, keywords, bpList):
	sectionText = "\section*{\href{%s}{%s %s, %s time}} \n" % (url, day, date, part)
	literatureText = r"\\textbf{Litteratur:} %s \\\\ \n" % literature
	themeText = r"\\textbf{Tema:} %s \\\\ \n" % themes
	keywordsText = r"\\textbf{Nøkkelord:} %s\n" % keywords
	itemText = r"\\begin{itemize}\n\t\\setlength\\itemsep{0em}\n"
	for bp in bpList:
		itemText = itemText + "\t" + bp + "\n"
	itemText = itemText + "\end{itemize}"
	return (sectionText+literatureText+themeText+keywordsText+itemText)


def copyTextToClipboard(text):
	os.system("echo '%s' | pbcopy" % text)

if __name__ == "__main__":
	main()