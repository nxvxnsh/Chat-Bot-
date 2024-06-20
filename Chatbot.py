import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine=pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty("rate",90)
ch=1
while(ch==1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.1)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            answer = "Please repeat"
            if MyText=="Hello":
                answer = "Hey from FCA department" 
            elif MyText== "who is the class coordinator of IIMCA 7'th Sem":
                answer = "Anita Verma mam"
            elif MyText== "What are the subjects in 7'th sem":
                answer = "Cloud Computing, Data Science, File Structure, Programing in JAVA, Computer Ethics"
            elif MyText== "who is the hod of computer application":
                answer = "Prof. Geeta Santhosh"
            elif MyText== "Who teaches Cloud Computer":
                answer = "Dr. Nidhi Dahale"
            elif MyText== "Who teaches Data Science":
                answer = "Prof. Smita mam"
            elif MyText== "Who teaches File Structure":
                answer = "Prof. Versha Sehgal"
            elif MyText== "Who teaches Programing in JAVA":
                answer = "Prof Shailesh Gondal"
            elif MyText== "Who teaches Computer Ethics":
                answer = "Prof. Anita Verma"
            elif MyText== "courses available in college":
                    answer = "B Tech B Pharma"
            elif MyText== "about the scholarship":
                answer = "You can contact to the reception for more details"
            elif MyText=="team member name":
                answer = "Celina Harshit Navansh"
            engine.say(answer)
            engine.runAndWait()
            ch=int(input("Do you want to ask more questions(Yes - 1/ No - 0) : "))
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")