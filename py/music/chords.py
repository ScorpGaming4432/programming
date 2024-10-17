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
        self.intervals = [0] + [(self.notes[i+1] - self.notes[i]) for i in range(self.length-1)]
        self.root = self.notes[0] if self.notes else None
        self.quality = self.determine_quality()

    def determine_root(self):
        for i in range(self.length):
            # Rotate the list to check each note as a potential root
            rotated_notes = self.notes[i:] + self.notes[:i]
            intervals = [(rotated_notes[j] - rotated_notes[0]) % 12 for j in range(1, len(rotated_notes))]
            if intervals == [4, 7] or intervals == [3, 7]:
                return rotated_notes[0]
        return None
    
    def determine_quality(self):
        if self.length == 3:
            intervals = sorted([(self.notes[i] - self.notes[0]) % 12 for i in range(1, self.length)])
            if intervals == [4, 7]:
                return "Major"
            elif intervals == [3, 7]:
                return "Minor"
        return "Unknown"
        

# Testing
print(Note('A4').toint())  # Output will be 57
print(Note(57).tonote())  # Output will be 'A4'

# Chord needs to use Note objects instead of strings
print(Chord(Note('C4'), Note('E4'), Note('G4')).intervals)  # Example of intervals for a C major chord
