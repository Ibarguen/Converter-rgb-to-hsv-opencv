import cv2
import tkinter
import imutils
import numpy as np
from PIL import Image
from PIL import ImageTk

global ret, frame, hmin

class Interfaz():


	def __init__(self):
		

		###-----------start interface variables
		self.root = tkinter.Tk()
		self.root.title('Color Converter')
		self.frame = tkinter.Frame(self.root, width=800, height=500)
		self.frame.pack()
		#####

		###----------- variables for show normal video
		self.show_video1 = tkinter.Frame(self.frame)
		self.show_video1.place(x=0, y=0)

		###----------- variabes for show color video
		self.show_video2 = tkinter.Frame(self.frame)
		self.show_video2.place(x=401, y=0)

		###----- start the cam
		self.cap = cv2.VideoCapture(0)


		###------ variables for label to videos
		self.lmain = tkinter.Label(self.show_video1)
		self.lmain.grid(row=0, column=0)

		self.lmain1 = tkinter.Label(self.show_video2)
		self.lmain1.grid(row=1, column=1)



		##----------variables for color range
		self.hmin = tkinter.Scale(self.frame, from_=0, to=255, length=350,	orient='horizontal', command= self.show_changes)
		self.smin = tkinter.Scale(self.frame, from_=0, to=255, 	length=350, orient='horizontal', command= self.show_changes)
		self.vmin = tkinter.Scale(self.frame, from_=0, to=255, 	length=350, orient='horizontal', command= self.show_changes)
		self.hmax = tkinter.Scale(self.frame, from_=0, to=255, 	length=350, orient='horizontal', command= self.show_changes)
		self.smax = tkinter.Scale(self.frame, from_=0, to=255, 	length=350, orient='horizontal', command= self.show_changes)
		self.vmax = tkinter.Scale(self.frame, from_=0, to=255, 	length=350, orient='horizontal', command= self.show_changes)

		self.video()
		self.video2()
	
		self.trackbar()
		self.show_changes()

		self.root.mainloop()

	def trackbar(self):
		
		hmintext =tkinter.Label(self.frame, text='hmin')
		hmintext.place(x=50, y= 310)		
		smintext =tkinter.Label(self.frame, text='smin')
		smintext.place(x=50, y= 350)
		vmintext =tkinter.Label(self.frame, text='vmin')
		vmintext.place(x=50, y= 400)


		
		hmaxtext =tkinter.Label(self.frame, text='hmax')
		hmaxtext.place(x=400, y= 310)		
		smaxtext =tkinter.Label(self.frame, text='smax')
		smaxtext.place(x=400, y= 350)		
		vmaxtext =tkinter.Label(self.frame, text='vmax')
		vmaxtext.place(x=400, y= 400)
		
	
		self.hmin.place(x=0, y=310)
		self.smin.place(x=0,y=350)
		self.vmin.place(x=0, y=400)
		self.hmax.place(x=400, y=310)
		self.smax.place(x=400, y=350)
		self.vmax.place(x=400, y=400)
		




	def video(self):
		global ret, frame 
		ret, frame = self.cap.read()		
		self.rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		




		##code to create label to normal video
		self.img = Image.fromarray(self.rgb).resize((400,300))
		imgtk = ImageTk.PhotoImage(image=self.img)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image=imgtk)
		self.lmain.after(10,self.video)
		
		
		

	def video2(self):

		global ret, frame
		kernel = np.ones((5,5), np.uint8) 	
		self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		hmin = self.hmin.get()
		smin = self.smin.get()
		vmin = self.vmin.get()

		hmax = self.hmax.get()
		smax = self.smax.get()
		vmax = self.vmax.get()
		### range the color to find
		low_color = np.array([hmin,smin,vmin],dtype=np.uint8)
		high_color = np.array([hmax,smax,vmax], dtype=np.uint8)
		
		#range
		x_1 = cv2.inRange(self.hsv,low_color, high_color)
		mascara = cv2.add(x_1, x_1)

		#filter 
		transfor = cv2.morphologyEx(mascara, cv2.MORPH_OPEN,kernel)
		moments = cv2.moments(transfor)
		
		##############
		self.img1 = Image.fromarray(transfor).resize((410,300))
		imgtk1 = ImageTk.PhotoImage(image=self.img1)
		self.lmain1.imgtk1 = imgtk1
		self.lmain1.configure(image=imgtk1)
		self.lmain1.after(10,self.video2)


	

		
		
	
	def show_changes(self, *args):
		
		hmin = self.hmin.get()
	

a = Interfaz()