def addText(text, fileName):
    with open(fileName, 'w') as file:
        file.write(text)
        print('This is the text you added:', text)

def showTotal(createfile):
    dic = {}
    with open(createfile, "r") as readFile:
        splitedFile = readFile.read().lower().split(" ")
        maxwords=0
        for i in splitedFile:
                maxwords +=1
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
                mostUsedWord= max(dic) #the most frequent word in input txt
                frequenceOfword = dic[mostUsedWord] #how many time did the frequent word written 
    print('the most frequent word : '  , mostUsedWord, "\t the word reapeted :", frequenceOfword ) 

print('1. Create a file')
while True:
    option = input('Choose the mode: ')
    if option == '1':
        print('Create a "pdf" or "txt" file; otherwise, it will be invalid.')
        createfile = input('Create a file name: ')
        if createfile.lower().endswith((".pdf", ".txt")):
            print('The file is created as:', createfile)
            text = input('Type the text to input to the file: ')
            addText(text, createfile)  
            showTotal(createfile)       
            break   
        else:
            print('Invalid file type.')  
    else:
        print('Invalid choice, try again.')

 
        