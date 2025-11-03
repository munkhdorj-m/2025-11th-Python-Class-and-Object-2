# Python Class and Objects 2

Python Class and Objects PDF:

https://drive.google.com/file/d/1GHMSwiOsYEQY1oRaJ548FfOX41OujLdd/view?usp=sharing


---

## Exercise 1

**Problem:**

Create a class Library that:  
    -Has a list of available books  
Methods:  
    -add_book(title)  
    -borrow_book(title) – removes from list if available  
    -return_book(title) – adds back  
    -show_books() – displays all books  

Example:

    Input:
      lib = Library()
      lib.add_book("1984")
      lib.add_book("The Hobbit")
      lib.borrow_book("1984")
      lib.show_books()
    
    Output:
      Available books:
      The Hobbit
---

## Exercise 2

**Problem:**

Create a class Player with:  
    -Attributes: name, health = 100, score = 0  
Methods:  
    -take_damage(amount) – reduce health but not below 0   
    -add_score(points)  
    -is_alive() – returns True if health > 0  

Example:

    Input: 
      p = Player("John")
      p.take_damage(30)
      p.add_score(50)
      print(p.is_alive())  # True
      
    Output:
      True
---

## Exercise 3

**Problem:**

Create a class Song with title, artist, duration.  
Create a class Playlist with:  
Methods:  
    -add_song(song)  
    -total_duration()  
    -show_songs()  

Example: 

    Input: 
      s1 = Song("Imagine", "John Lennon", 3.5)
      s2 = Song("Hey Jude", "The Beatles", 4.2)
      pl = Playlist()
      pl.add_song(s1)
      pl.add_song(s2)
      pl.show_songs()

    Output:
      1. Imagine - John Lennon (3.5 min)
      2. Hey Jude - The Beatles (4.2 min)
      Total: 7.7 min
      
---

