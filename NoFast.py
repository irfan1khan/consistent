import tkinter
from tkinter import Entry,Label,Button
import webbrowser

# DEFINING THE WINDOW
root=tkinter.Tk()
root.title("NO FAST (*_*)")
root.config(background="steelblue")
 
# DEFINING AUTOMATE SEARCH FOR YOUTUBE
def youtube_search():
    query=entry.get()
    url=f"https://www.youtube.com/search?q={query}"
    webbrowser.open(url)

# DEFINING AUTOMATE SEARCH FOR GOOGLE
def google_search():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# DEFINING instaagram_search():
def instagram_search():
    username=entry.get().replace('@',"") 
    url=f"https://www.instagram.com/{username}"
    webbrowser.open(url)

# DEFINING AUTOMATE SEARCH FOR FACEBOOK
def facebook_search():
    username=entry.get()
    url=f"https://www.facebook.com/search?q={username}"
    webbrowser.open(url) 
    
# FOR NEW SEARCH
def undo_search():
    query=entry.get()
    entry.delete(0,len(query))
 
# CREATING INPUT ,LABEL, FIELD AND BUTTONS
Label(root,text=" WHAT YOU WANNA KNOW :").pack(pady=20)
entry=Entry(root,bg="black",width=50)
entry.pack(pady=20)


# BUTTONS
Button(root,text="SEARCH ON YOUTUBE",command=youtube_search).pack(pady=15)
Button(root,text="SEARCH ON GOOGLE",command=google_search).pack(pady=15)
Button(root,text="SEARCH ON INSTAGRAM",command=instagram_search).pack(pady=15) 
Button(root,text="SEARCH ON FACEBOOK",command=facebook_search).pack(pady=15)
Button(root,text="X",command=undo_search,fg="black").place(x=415,y=81)

#RUNNING THE GUI MAIN LOOP
root.mainloop()