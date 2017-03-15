#VideoInnholdsFortegnelses LatexSkaper
#Laget av Storm Westlie til bruk som studass i TTK4105 - Reguleringsteknikk

import os

def main():
	day = input("Ukedag: ")
	date = input("Dato: ")
	part = input("Time: ")
	url = input("Url: ")
	literature = input("Litteratur: ")
	themes = input("Tema: ")
	keywords = input("Nøkkelord: ")
	bpList = createBulletPointList(url)
	latexCode = buildLatex(day, date, url, part, literature, themes, keywords, bpList)
	copyTextToClipboard(latexCode)
	print("\n *Latex-koden er kopiert til utklippstavlen.* \n *Ha en fin dag videre!*")

def createBulletPointList(url):
	print("\n *Kulepunktsliste* \n")

	bpList = []
	while(True):
		time = input("Tidspunkt: ")
		if(time == ""): break
		formattedTime = (int(time.split(":")[0])*60 + int(time.split(":")[1]))*1000 #Index 0 er antall minutter, index 1 er antall sekunder, "?playfrom=formattedTime"
		text = input("Kulepunkt: ")
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