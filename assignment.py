# assignment.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def borrow_book(self, title):
        if title in self.books:
            self.books.remove(title)
            return f'You borrowed "{title}"'
        else:
            return f'"{title}" is not available'

    def return_book(self, title):
        self.books.append(title)

    def show_books(self):
        if not self.books:
            return "No books available"
        result = "Available books:\n" + "\n".join(self.books)
        return result


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def add_score(self, points):
        self.score += points

    def is_alive(self):
        return self.health > 0


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def show_songs(self):
        if not self.songs:
            return "No songs in playlist"
        output = []
        for i, song in enumerate(self.songs, start=1):
            output.append(f"{i}. {song.title} - {song.artist} ({song.duration} min)")
        output.append(f"Total: {self.total_duration()} min")
        return "\n".join(output)
