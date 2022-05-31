# from tkinter import*                #import
# win=Tk()                            #창 생성
# win.geometry("2000x2000")           #창 크기
# win.title("euikyun")                #창 제목
# win.option_add("*Font","맑은고딕25")#전체 폰트
# win.mainloop()                      #창실행

#import tkinter         #이렇게 하면
#tkinter.Tx()           #앞에 tkinter. 을 붙여줘야함
    
from tkinter import*  #이렇게 하면 "앞으로 tkinter 안에있는 여러 함수를 사용할 것인데, 앞으로 "
# Tk()                  #앞에 tkinter. 안붙여줘도 됨
win=Tk()                #창 생성 명령어

win.title("Hello World!")
win.option_add("*Font","맑은고딕 50")
win.geometry("500x500")   #숫자는 pixel 단위
win.configure(bg='red')
btn=Button(win, text="버튼")
btn.pack()

win.mainloop()          #창 실행
