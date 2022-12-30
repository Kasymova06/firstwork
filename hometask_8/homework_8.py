# import random
# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# def newyork (sam):
#     face = random.choice(sam)
#     with open ('la.txt', 'a+')as f:
#         f.write(f"{face}\n")
# newyork(language)

# f = open('dls.txt', 'a+')
# f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsumhas been the industrs standard dummy text ever since the 1500s, when an unknownprinter took a galley of type and scrambled it to make a type specimen book. It hassurvived not only five centuries, but also the leap into electronic typesetting, remainingessentially unchanged. It was popularized in the 1960s with the release of Letrasetsheets containing Lorem Ipsum passages, and more recently with desktop publishingoftware like Aldus PageMaker including versions of Lorem Ipsum.')
# f.close()

# with open('nyc.txt', 'a+') as z:
#     z.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsumhas been the industrs standard dummy text ever since the 1500s, when an unknownprinter took a galley of type and scrambled it to make a type specimen book. It hassurvived not only five centuries, but also the leap into electronic typesetting, remainingessentially unchanged. It was popularized in the 1960s with the release of Letrasetsheets containing Lorem Ipsum passages, and more recently with desktop publishingoftware like Aldus PageMaker including versions of Lorem Ipsum.')

with open('la.txt','r')as s, open('nyc.txt', 'r')as w, open('wikipedia.txt', 'a+') as g:
    for i in s: 
        g.write(i)
    for n in w:
        g.write(n)
