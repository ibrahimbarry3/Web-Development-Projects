#Author Ricky Birnbaum & Ibrahim
#Web Tech
#February 6, 2016
#Ibrahim 50% of work & Ricky 50% of work

import random, string, time

def wrap(HTMLtype, ABCDE):
    
    #Step 1 print Front tag
    frontTag=HTMLtype
    #step 2 print the Text
    text=ABCDE
    
    #step 3 print end tag
    endTag=HTMLtype.split()
    endTag=endTag[0]
    if (endTag[-1] != '>'):
        endTag=endTag+'>'
    endTag=endTag.replace('<', '</')
    return(frontTag+'\n'+text+'\n'+endTag)


def generateHTML():

    
    #input file from user
    configFile = open("config.txt", 'r')
    #configFile = open("config2.txt", 'r')


    
    #output html file
    htmlFile = open("HW1.html", 'w')
    #stores information from configFile
    dictionary = {} 

    #read through file upto line 7
    for line in range(5):
        text = configFile.readline().split()
        dictionary[text[0]] = text[1]
    #TITLE and AUTHOR
    for line in range(2):
        text = configFile.readline().split()
        description = text[1]
        #if split causes more than 2 strings
        if (len(text)>2):
            for i in range(2, len(text)):
                description = description + " " + text[i]
        dictionary[text[0]] = description
    #IMAGES or LETTER
    text = configFile.readline()
    dictionary[text] = ""
    #to check for alternating cell
    alternate = 0
    #string builder for all <tr> row tags
    allrows = "" 
    if (text=="IMAGES\n"):
        for line in configFile.readlines():
            #a row of images
            listImagesRow = line.split()
            #string builder for all <td> cell tags
            alltabledata = "" 
            #for each image in the row
            for image in listImagesRow:
                image = '<img src="images/'+image+'"/>'
                td = wrap('<td class="cell'+str(alternate)+'">', image)
                if (alternate == 0): #even cell
                    alternate+=1
                else: #odd cell
                    alternate-=1
                alltabledata = alltabledata + td + "\n"
            tr = wrap('<tr>', alltabledata)
            allrows = allrows + tr + "\n"
            if ((len(listImagesRow))%2 == 0 and alternate ==0):
                alternate+=1
            elif ((len(listImagesRow))%2 == 0 and alternate ==1):
                alternate-=1
##----------------------------------------------
     #This section handles the Random letters                       
    else:
        dim = configFile.readline().split('x') #dimensions
        letters = string.ascii_letters #all alphabets
        letterList = list(letters) #a list of each letter
        for m in range(int(dim[0])):
            alltabledata = "" #string builder for all <td> cell tags
            for n in range(int(dim[1])):
                #randomize letter selection
                randLetter = letterList[random.randrange(len(letterList))]
                td = wrap('<td class="cell'+str(alternate)+'">', randLetter)
                if (alternate == 0): #even cell
                    alternate+=1
                else: #odd cell
                    alternate-=1
                alltabledata = alltabledata + td + "\n"
            tr = wrap('<tr>', alltabledata)
            allrows = allrows + tr + "\n"
            #if columns are even
            if (int(dim[1])%2 == 0 and alternate ==0):
                alternate+=1
            elif (int(dim[1])%2 == 0 and alternate ==1):
                alternate-=1
                
##----------------------------------------------
    table = wrap('<table>', allrows)
    configFile.close()
    
    h1 = wrap('<h1>', dictionary["TITLE"])
    pString = 'Created automatically on: ' \
             +time.asctime( time.localtime(time.time()))+'\n' \
             +'</br>\n</br>\nAuthors: '+dictionary['AUTHORS']
    p = wrap('<p>', pString)
    allCenter = h1 + table + p
    #center everything and put on the body
    center = wrap('<center>', allCenter)
    body = wrap('<body>', center)

    #styling details under <head> section
    details = "body {background-color: "+dictionary["BODY_BACKGROUND"]+";}\n" \
            ".cell0 {background-color: "+dictionary["CELL_BACKGROUND1"]+";}\n" \
            ".cell1 {background-color: "+dictionary["CELL_BACKGROUND2"]+";}\n" \
            "td {border: "+dictionary["TABLE_BORDER_PX"]+" solid " \
            +dictionary["TABLE_BORDER_COLOR"]+"; text-align: center;}" \
            "table {width: 60%; border-collapse: collapse;}\n" \
            "img {width: 100; height: 80;}"
    
    style = wrap('<style type="text/css">', details)
    head = wrap('<head>', style)

    allHTML = head + body
    html = wrap('<html>', allHTML)
    htmlFile.write(html)
    
    htmlFile.close()
    
generateHTML()
