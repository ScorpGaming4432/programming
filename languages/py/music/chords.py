class Note:
    letterconvert = {
        'C': 0, 'C#': 1, 'D': 2,
        'D#': 3, 'E': 4, 'F': 5,
        'F#': 6, 'G': 7, 'G#': 8,
        'A': 9, 'A#': 10, 'B': 11
    }
    
    def __init__(self, n):
        if isinstance(n, str):
            self.sound = n[:-1]
            self.octave = int(n[-1])
        elif isinstance(n, int):
            self.sound = n % 12
            self.octave = n // 12
        else:
            raise ValueError("Input must be a '<note><octave>' or an integer")
    
    def toint(self):
        return self.letterconvert[self.sound] + self.octave * 12
    
    def tonote(self):
        for note, value in self.letterconvert.items():
            if value == self.sound:
                return f"{note}{self.octave}"
        return None

class Chord:
    def __init__(self, *notes: Note):
        self.notes = sorted([note.toint() for note in notes])
        
        self.length = len(self.notes)
        # Add a leading 0 to represent the root as the first interval is always 0
        self.intervals = [(self.notes[i] - self.notes[0]) % 12 for i in range(1, self.length)]
        self.root = self.determine_root()
        self.quality = self.determine_quality()

    def determine_quality(self):
        if self.length == 3:
            intervals = sorted([(self.notes[i] - self.notes[0]) % 12 for i in range(1, self.length)])
            if intervals == [4, 7]:
                return "Major"
            elif intervals == [3, 7]:
                return "Minor"
        return "Unknown"

    def determine_root(self):
        if self.length == 3:
            absnotes = sorted([Note(Note(note).tonote()[:-1] + '0').toint() for note in self.notes])
            return absnotes
        
# Chord needs to use Note objects instead of strings
chord = Chord(Note('A4'), Note('C5'), Note('E5'))
print(chord.notes, chord.intervals)  # Example of intervals for a C major chord
print(chord.root)  # Expected root note

