def remove_dup(chord):
        chord_notes = [];

        for i in range(len(chord)):
            chord_notes[i] = chord[i].pitch%12  #remove octaves

        chord_notes.sort()  #sort notes
        chord_uniq = list(set(chord_notes)) #remove duplicates
        
        return chord_uniq;