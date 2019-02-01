from sys import argv, exit

def initialize():
    stopwords = set()
    stopwordsfile = open('stopwordsEnglish.txt', 'r')
    for line in stopwordsfile:
        stopwords.  add(line.rstrip('\n')) 
    return stopwords


def removeStopwords(inputfileName, outputfileName, stopwords):
    inputfile = open(inputfileName, 'r')
    outputfile = open(outputfileName, 'w')
    for line in inputfile:
        words = line.split()
        for word in words:
            if word.lower() not in stopwords:
                outputfile.write(word + " ")

def main():
    if len(argv) < 3:
        exit('Usage: ./removeStopwords inputfile outputfile')

    inputfileName = argv[1]
    outputfileName = argv[2]
    stopwords = initialize()
    removeStopwords(inputfileName, outputfileName, stopwords)
    print("Done!")


if __name__ == '__main__':
    main()

