import os
import pyttsx3 as ps
import webbrowser

ps.speak("hello")
print(" \t\t\t\t\tWelcome")
ps.speak("how can i help you")
while(True):
        ps.speak('please write your instruction')
        ch = input("\n please write your instruction : ")
        if ('notepad' in ch) or ('text' in ch) or ('editor' in ch):
                ps.speak('opening notepad')
                os.system("notepad")

        elif ('chrome' in ch) or ('browser' in ch) or ("internet" in ch):
                ps.speak('opening chrome')
                os.system("chrome")
                
        elif ('vlc' in ch) or ('media' in ch) or ('player' in ch):
                ps.speak('opening vlc media player')
                os.system("vlc")
                
        elif ('calc' in ch) or ('calculator' in ch) or ('math' in ch):
                ps.speak('opening calculator')
                os.system("calc")
                
        elif ('paint' in ch) or ('painting' in ch) or ('color' in ch):
                ps.speak('opening paint')
                os.system("mspaint")
                

        elif (('start' in ch) or ('song' in ch) or ('song') in ch) or ('play' in ch):
                ps.speak('enter name of the song you would you like to hear')
                name = input('enter name of the song you would you like to hear \n')
                path = name + ".mp3"
                # print(path)
                ps.speak('opening your music '+path)
                os.system(path)
               
        
        elif ('google' in ch) or ('Google' in ch):
                new = 2
                url = "http://google.com"
                webbrowser.open(url , new=new)
                ps.speak('opening  google')

        elif ('linkedln' in ch) or ('linkedin') in ch:
                new = 2
                url = "https://www.linkedin.com/feed/"
                webbrowser.open(url , new=new)
                ps.speak('opening linkedin ')

        elif ('git' in ch) or ('github') in ch:
                new = 2
                url = "https://github.com/"
                webbrowser.open(url , new=new)
                ps.speak('opening  github ')

        elif ('bootstrap' in ch) or ('css' in ch):
                new = 2
                url = "https://getbootstrap.com/docs/4.5/getting-started/introduction/"
                webbrowser.open(url , new=new)
                ps.speak('opening bootstrap ')
        elif ('insta' in ch) or ('instagram' in ch):
                new = 2
                url = "https://www.instagram.com/"
                webbrowser.open(url , new=new)
                ps.speak('opening  insta')
                
        elif ('fb' in ch) or ('facebook' in ch):
                new = 2
                url = "https://www.facebook.com/"
                webbrowser.open(url , new=new)
                ps.speak('opening  facebook')

        elif ('whatsapp' in ch) or ('whats app' in ch):
                new = 2
                url = "https://web.whatsapp.com/"
                webbrowser.open(url , new=new)
                ps.speak('opening  whatsapp')

        elif ('exit' in ch) or ('leave' in ch) or ('bye' in ch) or ('tata' in ch):
                ps.speak('Ok sir Have a nice day see you soon')
                break
        else:
                print("don't support  please try again")
                ps.speak("sorry for the inconvience   ")
                ps.speak("but i don't understand what you want")
                ps.speak("please try again")

