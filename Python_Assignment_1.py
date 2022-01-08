#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getLength(strTest):
    """This will return length of the string"""
    counter=0
    for i in strTest:
        counter=counter+1
    return counter
	

def printIndexForPrimitiveData(collection):
    """This will print index of all primitive data types"""
    for i in range(len(collection)):
        print(i)
		

def getAllValuesFromDict(dictSample):
    """This will return all the values from two level dictionary object"""
    list1=[]
    for i in dictSample.values():
        if type(i) == dict:
            for j in i.values(): 
                list1.append(j)
        else:
            list1.append(i)
    return list1

a=getAllValuesFromDict(dict1)



def inputFunction():
    strFunctionName=input()
    if (strFunctionName.lower())=="welcome":
        return welcome()
    
def welcome():
    return "Happy new year 2022"

b=inputFunction()
b



def concatAllValues(list1,list2,list3):
    """This will concatenate all elements from the three lists"""
    a=""
    list1.extend(list2)
    list1.extend(list3)
    for i in list1:
        a=a+str(i)
    return a

list1=[1,2,3]
list2=[3,4,5]
list3=[34,53,53]

b=concatAllValues(list1,list2,list3)

b


def returnIndexForList(list1):
    """This will return index for the list items even if the items are repeatative"""
    list2=[]
    for i in range(len(list1)):
        list2.append(i)
    return list2

list1=[234,234,"Test","ABC"]
list2=returnIndexAndValueForList(list1)
list2




import os
def getFileNames(strPath):
    """This function is used to get file names available in the provided path"""
    return os.listdir(strPath)

getFileNames("C:\\")



import platform
def getProcessorInfo():
    """This function is used to get system configuration details"""
    print(platform.machine())
    print(platform.node())
    print(platform.processor())
    print(platform.release()) 
    print(platform.uname())
	
getProcessorInfo()	
	



import datetime
def getCurrentDateTime():
    """This function is used to return current systems date time"""
    return datetime.datetime.now()

print(getCurrentDateTime())





def openImageFile(strPath,strName):
    os.startfile(strPath+strName)
    
openImageFile("C:\\Users\\Dell 1\\Documents\\fwdocuments\\"+"20160428_222019.jpg")




import vlc, time
def runVideo(strPath):
    videoPlayer=vlc.MediaPlayer(strPath)
    videoPlayer.play()
    time.sleep(20)
    videoPlayer.stop()




def moveFile(src,dest):
    """This function is used to move file from src location to dest location"""
    a=shutil.move(src,dest)
    print(a)
    return a

moveFile("C:\\Users\\abhin\\Desktop\\Dict object.docx","C:\\Users\\abhin\\Desktop\\Data Science")




import os
def shutDownSystem():
    os.system('shutdown /s')
    
shutDownSystem()





import imaplib, email
def getEmails(username,password,fromaddress):
    """This is used to print emails Subject, TO Address, From Address, Date for the emails having from address provided by the user"""
    imapobj=imaplib.IMAP4_SSL('imap.gmail.com')
    imapobj.login(username,password)
    imapobj.select("inbox")
    status, messages = imapobj.search(None,'FROM', '"{}"'.format(fromaddress))

    for num in messages[0].split():
        _, data=imapobj.fetch(num,'RFC822')
        _, bytesData=data[0]
        email_message=email.message_from_bytes(bytesData)
        print("Subject: ",email_message["subject"])
        print("To:", email_message["to"])
        print("From: ",email_message["from"])
        print("Date: ",email_message["date"])




import smtplib
def sendEmail(username,password,toAddress,emailBody):
    """This is used to send email to specified user with the message"""
    smtpobj=smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtpobj.login(username,password)
    smtpobj.sendmail(username,toAddress,emailBody)
    print("Email Sent")



    

import PyPDF2
def getPDFText(strPath):
    """This function is used to read text from pdf file"""
    pdfText=""
    pdfFileObj = open(strPath, 'rb')
    fileReader=PyPDF2.PdfFileReader(pdfFileObj)
    pageCount=int(fileReader.getNumPages())
    for i in range(0, pageCount):
        pageobj=fileReader.getPage(i)
        pdfText=pdfText+pageobj.extractText()
    return pdfText


b=getPDFText("C:\\Users\\abhin\\Desktop\\Sample.pdf")
b





import docx
def readWordFile(strPath):
    """This function is used to read word file from provided file path"""
    doc=docx.Document(strPath)
    strFileContent=""
    for paragraph in doc.paragraphs:
        strFileContent=strFileContent+paragraph.text
    return strFileContent
b=readWordFile('C:\\Users\\abhin\\Desktop\\Transmission Application.docx')
b




import os

def filterWordFilesFromDir(strDir):
    """This function is used to get word document files from provided directory"""
    os.chdir(strDir)
    os.listdir()
    list1=[]
    for i in os.listdir():
        if os.path.splitext(i)[1]==".doc" or os.path.splitext(i)[1]==".docx":
            list1.append(i)
    return list1

filterWordFilesFromDir("C:\\Users\\abhin\\Desktop")




import socket
def getIPAddress():
    """This is used to get system ip address """
    return socket.gethostbyname(socket.gethostname())

getIPAddress()






def mergePDF(pdf1,pdf2):
    """This is used to merge two pdf files"""
    pdfmerger=PdfFileMerger()
    pdfmerger.append(pdf1)
    pdfmerger.append(pdf2)
    pdfmerger.write("Test.pdf")
    pdfmerger.close()
    return pdfmerger

pdf1 = "C:\\Users\\abhin\\Desktop\\sample.pdf"
pdf2 = "C:\\Users\\abhin\\Desktop\\Smallpdf.pdf"

mergePDF(pdf1,pdf2)

