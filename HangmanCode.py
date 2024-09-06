from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import pygame

def play_sound2():
    # Replace "audio_file.mp3" with the path to your audio file
        pygame.mixer.init()
        pygame.mixer.music.load("HangMan_Audio/level.wav")
        pygame.mixer.music.play()

def seltheme():
    
    # Create a new window for selecting the theme:
    theme_window = Toplevel(root)
    theme_window.geometry("900x700")
    theme_window.minsize(900,700)
    theme_window.maxsize(900,700)
    theme_window.title("THEME")
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 16.09.20.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(theme_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    theme_window.configure(bg="plum1")
    

    def play_sound1():
    # Replace "audio_file.mp3" with the path to your audio file
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\theme.wav")
        pygame.mixer.music.play()
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    #destroying window
    def theme_destroy():
        theme_window.destroy()
    
    # Create the cities button
    cities_button = Button(theme_window, text="Cities",width=10,height=2,command=lambda: (cities_game(),theme_destroy()))
    cities_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    cities_button.place(relx=0.07, rely=0.78)
    
    # Create the actors button
    actors_button = Button(theme_window, text="Actors",width=10,height=2,command=lambda: (actors_game(),theme_destroy()))
    actors_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    actors_button.place(relx=0.22, rely=0.78)
    
    # Create the automobiles button
    Automobiles_button = Button(theme_window, text="Automobiles",width=10,height=2,command=lambda: (auto_game(),theme_destroy()))
    Automobiles_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    Automobiles_button.place(relx=0.38, rely=0.78)
    
     # Create the cartoons button
    Cartoons_button = Button(theme_window, text="Cartoons",width=10,height=2,command=lambda: (cartoon_game(),theme_destroy()))
    Cartoons_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    Cartoons_button.place(relx=0.52, rely=0.78)
    
     # Create the fruits button
    Fruits_button = Button(theme_window, text="Fruits",width=10,height=2,command=lambda: (fruit_game(),theme_destroy()))
    Fruits_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    Fruits_button.place(relx=0.68, rely=0.78)
     # Create the cricketers button
    Cricketers_button = Button(theme_window, text="Cricketers",width=10,height=2,command=lambda: (crick_game(),theme_destroy()))
    Cricketers_button.config(fg='black', bg='cornsilk2', font=('Arial', 8))
    Cricketers_button.place(relx=0.82, rely=0.78)
    play_sound1()
    theme_window.mainloop()

def won():
    won_window = Toplevel(root)
    won_window.geometry("400x400")
    won_window.minsize(400,400)
    won_window.maxsize(400,400)
    won_window.title("Won Game")
    img1 = Image.open("C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-10 at 22.50.33.jpeg")
    photo1 = ImageTk.PhotoImage(img1)
    # Create the Label widget
    label = Label(won_window, image=photo1)
    label.pack()
    def won_destroy():
        #adding sound
        pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
        pygame.mixer.music.play(loops=0)
        won_window.destroy()
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\win.wav")
    pygame.mixer.music.play()
    new_game_button = Button(won_window, text="New Game",width=10,height=2,command=won_destroy)
    new_game_button.pack(side="left",padx=150)
    won_window.mainloop()
    
def lost():
    lost_window = Toplevel(root)
    lost_window.geometry("400x400")
    lost_window.minsize(400,400)
    lost_window.maxsize(400,400)
    lost_window.title("Lost Game")
    # Load the image
    img1 = Image.open("C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-10 at 23.36.24.jpeg")
    photo1 = ImageTk.PhotoImage(img1)
    # Create the Label widget
    label = Label(lost_window, image=photo1)
    label.pack()
    def lost_destroy():
        #adding sound
        pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
        pygame.mixer.music.play(loops=0)
        lost_window.destroy()
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\lost.wav")
    pygame.mixer.music.play()
    delete_button = Button(lost_window, text="Try again",width=10,height=2,command=lost_destroy)
    delete_button.pack(side="bottom",padx=150)
    lost_window.mainloop()
def easy_game():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cities= ['MUMBAI','SURAT','PUNE','THANE','PATNA','AGRA','GOA','KOTA']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_cities)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}",font=(20))
        chances_left_label.grid(padx=100,pady=20)
    def correct_word():
        correct_label = Label(game_window, text=f"{the_word_new}")
        chances_left_label.grid(padx=100,pady=20)
        
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}",font=(20))
                if numberOfGuesses==3:
                        correct_word_label = Label(game_window, font='consolas 18 bold')
                        correct_word_label.grid(padx=100, pady=10)
                        correct_word_label.config(text=f"The correct word was: {the_word_new}")
                        correct_word()
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=100, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")
    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',':)']
   

    #Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=150,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cities=['MUMBAI','JAIPUR','RANCHI','KANPUR','NAGPUR','INDORE','BHOPAL','MEERUT','RAJKOT','RAIPUR','JHANSI']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_cities)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cities= ['BANGLORE','HYDERABAD','AHMEDABAD','CHENNAI','KOLKATA','AMRITSAR','ALLAHABAD','LUCKNOW','GHAZIABAD','FARIDABAD','VARANASI','SRINAGAR']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang4.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang5.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang7.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_cities)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window
def cities_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    def play_sound2():
    # Replace "audio_file.mp3" with the path to your audio file
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\level.wav")
        pygame.mixer.music.play()
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    play_sound2()
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def window_destroy():
        game_window.destroy()
    
    # Create the easy button
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game(),window_destroy()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game(),window_destroy()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game(),window_destroy()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()
    
    
def easy_game1():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['NANI','RAM','NTR','ALI','ANUPAMA','JAMUNA','RANA','VANI SRI','KAJAL','MEENA','TRISHA']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\New folder\\hang6.png"),PhotoImage(file="C:\\New folder\\hang9.png"),PhotoImage(file="C:\\New folder\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}")
                if numberOfGuesses==3:
                        game_window.destroy()                
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game1():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['RAVI TEJA','SAVITRI','SAMANTHA','ANUSHKA','SATYA RAJ','ANUPAMA','SRIDEVI','VANI SRI','PRABHAS','SATYADEV']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game1():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['SAI PALLAVI','DULQUER SALMAAN','BRAMHANANDAM','ALLU ARJUN','CHIRANJEEVI','BHANU PRIYA','BALA KRISHNA','RAM CHARAN','SOUNDARYA','SHARWANAND','SIDDHARTH']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\New folder\\hang4.png"), PhotoImage(file="C:\\New folder\\hang5.png"),
    PhotoImage(file="C:\\New folder\\hang6.png"), PhotoImage(file="C:\\New folder\\hang7.png"), PhotoImage(file="C:\\New folder\\hang8.png"),
    PhotoImage(file="C:\\New folder\\hang9.png"), PhotoImage(file="C:\\New folder\\hang10.png"), PhotoImage(file="C:\\New folder\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window
def actors_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    play_sound2()
    def window_destroy1():
        game_window.destroy()
    
    # Create the easy button
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game1(),window_destroy1()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game1(),window_destroy1()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game1(),window_destroy1()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()
    


def easy_game2():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_crick= ['VIRAT','DHONI','ROHIT','MITHALI','SMRITI','BHUMRAH','SACHIN','SEHWAG','DEEPTI','RENUKA','JHULAN',
             'YASTIKA','RAHANE','CHAHAL','TANIYA','POOJA','YUVRAJ']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_crick)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}")
                if numberOfGuesses==3:
                        game_window.destroy()                
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game2():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_crick= ['AXAR PATEL','LAKSHMAN','PUNAM RAUT','SNEH RANA','KAPIL DEV']
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_crick)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game2():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_crick= ['POONAM YADAV','ARUNDATHI','SHEFALI VERMA','HARMANPREET KAUR','MEGHNA SINGH','GAUTAM GHAMBHIR','RAHUL DRAVID',]
    #hangman pictures       
    photos = [PhotoImage(file="C:\\New folder\\hang4.png"), PhotoImage(file="C:\\New folder\\hang5.png"),
    PhotoImage(file="C:\\New folder\\hang6.png"), PhotoImage(file="C:\\New folder\\hang7.png"), PhotoImage(file="C:\\New folder\\hang8.png"),
    PhotoImage(file="C:\\New folder\\hang9.png"), PhotoImage(file="C:\\New folder\\hang10.png"), PhotoImage(file="C:\\New folder\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_crick)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window


def crick_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    #start label
    start_label = Label(game_window, text='''\n\nselect the level
                                             \n1.Easy
                                             \n2.Medium
                                             \n3.Hard''',bg="DarkCyan",fg="white")
    start_label.configure(font=("Helvetica",16),justify="left")
    start_label.pack(pady=50)
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    play_sound2()
    def window_destroy2():
        game_window.destroy()
    
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game2(),window_destroy2()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game2(),window_destroy2()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game2(),window_destroy2()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()
    
    
def easy_game3():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_auto= ['VOLVO','FORD','BMW','KIA','VESPA','BENZ','AUDI','SKODA','LEXUS','KMT']
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_auto)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}")
                if numberOfGuesses==3:
                        game_window.destroy()                
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game3():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_auto= ['NISSAN','HYUNDAI','RENAULT','TRIUMPH','DUCATI','LAND ROVER','JAGUAR','TOYOTO','FERRARI','MASERATI','YAMAHA']
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_auto)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game3():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_auto= ['MARUTI SUZUKI','VOLKSWAGEN','CADILLAC','ROYAL ENFIELD','HARLEY DAVIDSON','LAND ROVER','ASTON MARTIN','TATA MOTORS','KAWASAKI','BAJAJ MOTORS']
    #hangman pictures
    photos = [PhotoImage(file="C:\\New folder\\hang4.png"), PhotoImage(file="C:\\New folder\\hang5.png"),
    PhotoImage(file="C:\\New folder\\hang6.png"), PhotoImage(file="C:\\New folder\\hang7.png"), PhotoImage(file="C:\\New folder\\hang8.png"),
    PhotoImage(file="C:\\New folder\\hang9.png"), PhotoImage(file="C:\\New folder\\hang10.png"), PhotoImage(file="C:\\New folder\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_auto)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window
def auto_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    #start label
    start_label = Label(game_window, text='''\n\nselect the level
                                             \n1.Easy
                                             \n2.Medium
                                             \n3.Hard''',bg="DarkCyan",fg="white")
    start_label.configure(font=("Helvetica",16),justify="left")
    start_label.pack(pady=50)
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    play_sound2()
    def window_destroy3():
        game_window.destroy()
    
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game3(),window_destroy3()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game3(),window_destroy3()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game3(),window_destroy3()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()
    
def easy_game6():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cartoon= ['DORA','POPEYE','TARZAN','BEN TEN','SMURFS','NODY','MR BEAN','MINIONS','POKEMON','DOREMON']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_cartoon)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}")
                if numberOfGuesses==3:
                        game_window.destroy()                
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game6():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cartoon= ['SNOW WHITE','SHINCHAN','RICHE RICH','CHOR POLICE','MINIONS','MICKEY MOUSE','CHOTA BHEEM']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_cartoon)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game6():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_cartoon= ['TOM AND JERRY','SCOOBY DOO','HANAMONATANA','POWERPUFF GIRLS','OGGY AND COCKROACHES',
              'POWER RANGERS','WINNIE THE POOH','KICK BUTTOWSKI','THE SIMPSONS','CINDERELLA']
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang4.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang5.png"),
    PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang7.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),
    PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_cartoon)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")
    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window
def cartoon_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    #start label
    start_label = Label(game_window, text='''\n\nselect the level
                                             \n1.Easy
                                             \n2.Medium
                                             \n3.Hard''',bg="DarkCyan",fg="white")
    start_label.configure(font=("Helvetica",16),justify="left")
    start_label.pack(pady=50)
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    play_sound2()
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    def window_destroy6():
        game_window.destroy()
    
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game6(),window_destroy6()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game6(),window_destroy6()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game6(),window_destroy6()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()
    
def easy_game5():
    
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("easy Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)

    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['APPLE','QUINCE','GUAVA''MANGO','PEACH','PEAR','DATES','PLUM','KIWI','LYCHEE','CHERRY','SATSUMA','GRAPES','ORANGE']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]
        
    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {3}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<3:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
    
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {3 - numberOfGuesses}")
                if numberOfGuesses==3:
                        game_window.destroy()                
                        lost()
                    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    
    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)
    
    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
    

def medium_game5():
    #creating window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("medium Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['PINEAPPLE','CANTALOUPE','HONEYDEW','JACKFRUIT','APRICOT']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global chances_left_label
        global the_word_new
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {5}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<5:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()                    
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
            else:
                
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {5 - numberOfGuesses}")
                if numberOfGuesses==5:
                    game_window.destroy()
                    lost()
                    
                        
                        
    
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=20)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()

def hard_game5():
    #creating main window
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("hard Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    #list of words
    list_actors= ['WATERMELON','GOOSEBERRY','NECTARINE','MUSKMELON','DRAGON FRUIT','POMEGRANATE','STAR FRUIT','RASPBERRY']
    
    #hangman pictures       
    photos = [PhotoImage(file="C:\\all_files\\Hangman\\hang4.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang5.png"),
    PhotoImage(file="C:\\all_files\\Hangman\\hang6.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang7.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang8.png"),
    PhotoImage(file="C:\\all_files\\Hangman\\hang9.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang10.png"), PhotoImage(file="C:\\all_files\\Hangman\\hang11.png")]

    #game loop
    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        global the_word_new
        global chances_left_label
        numberOfGuesses = 0
        the_word = random.choice(list_actors)
        the_word_new = ""
        for char in the_word:
            if char.isalpha():
                the_word_new=the_word_new+char    
        the_word_withSpaces = " ".join(the_word_new)
        lblWord.set(' '.join("_"*len(the_word_new)))
        chances_left_label = Label(game_window, text=f"Chances left: {8}")
        chances_left_label.grid(padx=5,pady=20)
            
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<8:	
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        play_sound()
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        game_window.destroy()
                        won()
                        
                        
                        
            else:
                imgLabel.config(image=photos[numberOfGuesses],bg="white")
                numberOfGuesses += 1
                play_sound_1()
                chances_left_label.config(text=f"Chances left: {8 - numberOfGuesses}")
                if numberOfGuesses==8:
                        game_window.destroy()
                        lost()
                        
                        
                        
                        
    #hangman images on the main screen
    imgLabel=Label(game_window,bg="DarkCyan")
    imgLabel.grid( padx=5, pady=40)
    

    #displaying word on the screen
    lblWord = StringVar()
    Label(game_window, textvariable=lblWord, font='consolas 24 bold').grid(padx=10,pady=10)

    #adding sound to buttons
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    sound = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.30.48-_1_.wav")
    sound1 = pygame.mixer.Sound("C:\\Users\\tatan\\Downloads\\WhatsApp-Audio-2023-03-10-at-21.31.39-_1_.wav")

    # Create a list of alphabets
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


    # Create a frame for the buttons
    frame = Frame(game_window,bd=10, relief="groove")
    frame.grid(padx=30,pady=70)

    # Create a function to play the sound
    def play_sound():
        sound.play()
    def play_sound_1():
        sound1.play()

    # Create a grid of 3 rows and 9 columns inside the frame
    for i in range(3):
        for j in range(9):
           # Calculate the index of the alphabet in the list
           index = i * 9 + j
           # Check if the index is within the bounds of the list
           if index < len(alphabets):
               # Create a button for the alphabet
               button=Button(frame, text=alphabets[index], width=6, height=3, font=(8), command=lambda letter=alphabets[index]: guess(letter))

               # Place the button in the grid
               button.grid(row=i, column=j)
    newGame()
#creating start game window
def fruit_game():
    game_window = Toplevel(root)
    game_window.geometry("900x700")
    game_window.minsize(900,700)
    game_window.maxsize(900,700)
    game_window.title("Game")
    
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    #start label
    start_label = Label(game_window, text='''\n\nselect the level
                                             \n1.Easy
                                             \n2.Medium
                                             \n3.Hard''',bg="DarkCyan",fg="white")
    start_label.configure(font=("Helvetica",16),justify="left")
    start_label.pack(pady=50)
    # Set the background color of the main window
    game_window.configure(bg="DarkCyan")
    
    bg_image = Image.open(r"C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-12 at 15.31.49.jpeg")
    # Resize the image to fit the window size
    bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
    # Create a PhotoImage object from the resized image
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Create a label to hold the background image
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    play_sound2()
    def window_destroy5():
        game_window.destroy()
    
    easy_button = Button(game_window, text="Easy",font=(10),width=10,height=2,command=lambda: (easy_game5(),window_destroy5()))
    easy_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    easy_button.place(relx=0.1, rely=0.6)
    

    # Create the medium button
    medium_button = Button(game_window, text="Medium",font=(10),width=10,height=2,command=lambda: (medium_game5(),window_destroy5()))
    medium_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    medium_button.place(relx=0.45, rely=0.6)


    #create the hard button
    hard_button = Button(game_window, text="Hard",font=(10),width=10,height=2,command=lambda: (hard_game5(),window_destroy5()))
    hard_button.config(fg='black', bg='RosyBrown1', font=('Arial', 8))
    hard_button.place(relx=0.8, rely=0.6)
    game_window.mainloop()


    

#creating instructions window
def show_instructions():
    
    # Create a new window for instructions
    instr_window = Toplevel(root)
    instr_window.geometry("900x700")
    instr_window.minsize(900,700)
    instr_window.maxsize(900,700)
    instr_window.title("Instructions")
    #root.destroy()
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    # Add some sample instructions
    instr_heading = Label(instr_window,bg="plum1",fg="black",text="INSTRUCTIONS")
    instr_heading.configure(font=("Helvetica",20),justify="left")
    instr_heading.pack(pady=50)
    instr_label = Label(instr_window,bg="plum1",fg="black",text='''1. Choose a comfortable level
                                                               \n2. Choose your favourite theme.
                                                               \n3. Displaying the word to you "_ _ _ _ _ _ "
                                                               \n4. Guess any letter
                                                               \n5. If the letter  is in the choosen word then letter  is shown in right position 
                                                               \n6. If not ,your chances are decremented by 1
                                                               \n7. Repeat above steps until player guess  the word or run out of guesses 
                                                               \n8. If the player has guessed the "you 🏆 won  the game"
                                                               \n9. If player runs out of guesses and guesses  wrongly, " you lost the game " 
                                                               \n10. Hangman  structure is revealed''')
    instr_label.configure(font=("Helvetica",16),justify="left")
    instr_label.pack()
    def instr_destroy():
        #adding sound
        pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
        pygame.mixer.music.play(loops=0)
        instr_window.destroy()
    
    
    back_button = Button(instr_window, text="Back",width=10,height=2,command=instr_destroy)
    back_button.pack(side="left" ,padx =400)
    
    
    # Set the background color of the main window
    instr_window.configure(bg="plum1")
    
#creating exit window
def exit_game():
    #adding sound
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\mixkit-positive-interface-click-1112.wav")
    pygame.mixer.music.play(loops=0)
    root.destroy()

pygame.mixer.init()# initialise the pygame

def play_sound():
    # Replace "audio_file.mp3" with the path to your audio file
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\tatan\\Downloads\\welcome.wav")
    pygame.mixer.music.play()

# Set up the main window
root = Tk()
root.geometry("900x700")
root.minsize(900,700)
root.maxsize(900,700)
root.title("Hangman Game")
play_sound()

bg_image = Image.open("C:\\Users\\tatan\\Downloads\\WhatsApp Image 2023-03-11 at 22.59.16.jpeg")
# Resize the image to fit the window size
bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
# Create a PhotoImage object from the resized image
bg_photo = ImageTk.PhotoImage(bg_image)
# Create a label to hold the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Set the background color of the main window
root.configure(bg="sky blue")

frame = Frame(root)
frame.pack(side="bottom", padx=20, pady=20)


# Create the start button
start_button = Button(root, text="Start Game",width=10,height=2,command=seltheme)
start_button.config(fg='black', bg='sky blue', font=('Arial', 12))
start_button.place(relx=0.1, rely=0.8)

# Create the instructions button
instruction_button = Button(root, text="Instructions",width=10,height=2,command=show_instructions)
instruction_button.config(fg='black', bg='sky blue', font=('Arial', 12))
instruction_button.place(relx=0.45, rely=0.8)


#create the exit button
exit_button = Button(root, text="Exit",width=10,height=2,command=exit_game)
exit_button.config(fg='black', bg='sky blue', font=('Arial', 12))
exit_button.place(relx=0.8, rely=0.8)

root.mainloop()
