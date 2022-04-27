file = open('Credentials.txt') #Open the txt file
content = file.readlines() #Read the content of the file

#Reads the values in each line in the Credentials.txt and assigns it to a variable
line1 = content[0]
line2 = content[1]
line3 = content[2]
line4 = content[3]
line5 = content[4]
line6 = content[5]
line7 = content[6]

start = 'Telegram bot token:'
end = 'Telegram Chat ID:'
a = line1
tokenID = (a[a.find(start)+len(start):a.rfind(end)])

start = 'Telegram Chat ID:'
end = 'Gmail password:'
b = line2
chatID = (b[b.find(start)+len(start):b.rfind(end)])

start = 'Gmail password:'
end = 'Subject for Email:'
c = line3
gmailPass = (c[c.find(start)+len(start):c.rfind(end)])

start = 'Subject for Email:'
end = 'Sender Email:'
d = line4
SubjectEmail = (d[d.find(start)+len(start):d.rfind(end)])

start = 'Sender Email:'
end = 'Receiver Email:'
e = line5
SenderEmail = (e[e.find(start)+len(start):e.rfind(end)])

start = 'Receiver Email:'
end = 'SMS Email:'
f = line6
ReceiverEmail = (f[f.find(start)+len(start):f.rfind(end)])

start = 'SMS Email:'
end = '###'
g = line7
SMSEmail = (g[g.find(start)+len(start):g.rfind(end)])

file.close()