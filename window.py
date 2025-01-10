from tkinter import*;
from tkinter import ttk;
from tkcalendar import *;
from PIL import ImageTk,Image,ImageOps,ImageDraw,ImageFont;
from tkinter import messagebox;
from tkinter import filedialog;
import os;


window=Tk();
#this code for window 
window.geometry("800x800");
window.title("window codes");
window.configure(bg="#82e0aa");

e_name=StringVar();
e_type=StringVar();
e_quality=IntVar();
e_size=IntVar();
h_size=IntVar();
img_location=StringVar();
scalewidth=IntVar();
scalehig=IntVar();

def imagefunc():
    img_open=Image.open(img_location.get());
    newfile=e_name.get()+e_type.get();
    if(e_name.get()=="" or e_type.get()==""):
        messagebox.showwarning("showwaring",f"Enter The File Name");
    else:
        new_text=textOnImage()
        size=new_text.resize((e_size.get(),h_size.get()))
        size.save(newfile,quality=e_quality.get());
        preview(newfile)
        messagebox.showinfo("showinfo",f"image save as {newfile}");
        

def preview(temp):
    img_open=Image.open(temp);
    size=img_open.resize((e_size.get(),h_size.get()))
    imgfrmae=ImageTk.PhotoImage(size)
    image_label['image']=imgfrmae
    image_label.image=imgfrmae
    
    
def openfile():
    path=filedialog.askopenfilename(title="select a file",filetypes=(("text file","*.text"),("all files","*.*")));
    if path!="":
        img_location.set(path);
    else:
        messagebox.showwarning("showwaring","image not selected");

    img_location.set(path);
       
def scalefun():
    #print(scalewidth.get())
    e_size.set(scalewidth.get())
    
    newsize.after(1,scalefun)
     
def scheight():
    h_size.set(scalehig.get());
    newsize.after(1,scheight);
        

def textOnImage():
    img=Image.open(img_location.get());
    draw=ImageDraw.Draw(img);
    font=ImageFont.truetype("arial.ttf",size=30);
    color="red";
    thumsize=(e_size.get(),h_size.get());
    img.thumbnail(thumsize,resample=Image.BOX);
    position=(50,50);
    draw.text(position,textenter.get(),fill=color,font=font,align="right");
    return img


#here we create the part and option on the window
frame1=Frame(window,width=1200,height=200,bg="gray");
#frame1.place(x=75,y=10)
frame1.place(x=100,y=0);

#here he work in the frame
lable1=Label(frame1,text="PROJECT",font=("Aptos",40),fg="#FFC300");
#lable1.pack();
lable1.place(x=500,y=50);

#frame 2 start here
frame2=Frame(window,width=1200,height=500,bg="#884ea0");
frame2.place(x=100,y=200);


name=Label(frame2,text="Enter Name",font=("Aptos",16,"bold"),fg="gray");
name.place(x=50,y=25);

enter_name=Entry(frame2,font=("Aptos",16,"bold"),bg="white",textvariable=e_name);
enter_name.place(x=300,y=25);

format1=Label(frame2,text="Image Format",font=("Aptos",16,"bold"),fg="gray");
format1.place(x=50,y=75);

Img_quality=Label(frame2,text="Image Quality",font=("Aptos",16,"bold"),fg="gray");
Img_quality.place(x=50,y=125);

quality=Entry(frame2,font=("Aptop",16,"bold"),bg="white",textvariable=e_quality);
quality.place(x=300,y=125);

imgwidth=Label(frame2,text="Enter width",font=("Aptos",16,"bold"),fg="gray");
imgwidth.place(x=50,y=175);
newsize=Entry(frame2,font=("Aptos",16,"bold"),bg="white",textvariable=e_size);
newsize.place(x=300,y=175);

imgheight=Label(frame2,text="Enter height",font=("Aptos",16,"bold"),fg="gray");
imgheight.place(x=50,y=225);
newheight=Entry(frame2,font=("Aptos",16,"bold"),bg="white",textvariable=h_size);
newheight.place(x=300,y=225);

#enter the text
textlabel=Label(frame2,text="Text On Image",font=("Aptos",16,"bold"),fg="gray");
textlabel.place(x=50,y=275);

textenter=Entry(frame2,font=("Aptos",16,"bold"),bg="white");
textenter.place(x=300,y=275);

btn2=Button(frame2,text="Choose Image",font=("Aptos",16,"italic"),bg="white",fg="gray",command=openfile);
btn2.place(x=50,y=350);

location=Label(frame2,text="File Location",font=("Aptos",16,"bold"),fg="gray");
location.place(x=700,y=10);
pathfile=Label(frame2,font=("Aptos",10,"bold"),fg="gray",textvariable=img_location);
pathfile.place(x=850,y=10);


#drop down
box=ttk.Combobox(frame2,values=(".jpg",".png",".gif",".ico"),font=("Aptos",16,"bold"),textvariable=e_type,state="readonly");
box.current(0)
box.place(x=300,y=75);

#save button
button1=Button(frame2,text="Save Now",font=("Aptos",16,"bold","italic"),bg="white",fg="gray" ,command=imagefunc);
button1.place(x=300,y=350);

#sacel on frame 2

scale=Scale(frame2,from_=50,to=500,orient=HORIZONTAL,label="Width",variable=scalewidth);
scale.place(x=30,y=400);
#scalefun()

scaleheight=Scale(frame2,from_=50,to=500,orient=HORIZONTAL,label="Height",variable=scalehig);
scaleheight.place(x=150,y=400);
#scheight();

#
#frame 3 in the frame 2
frame3=Frame(frame2,width=400,height=400,bg="#FFBF00");
frame3.place(x=700,y=50);
image_label=Label(frame3,font=("Aptos",16,"bold"),fg="gray",bg='#FFBF00');
image_label.place(x=0,y=0);
#Alt-KeyPress-o
window.bind("<Control-o>",lambda e:openfile());
window.bind("<Control-s>",lambda e:imagefunc());
window.mainloop();
