'''
Ogolnie robie teraz dwa algorytmy
jeden dziala bez splitu na 3, drugi vice versa
oznaczone albo 0 albo 1 po nazwie
te które nic nie mają są stałą częścią kodu

Kod przyjmuje długość kodu podzielną przez 3
'''

#initialising
mrnaToBialkaTranslator0 = {
    'U': {
        'U': {
            'U': 'Phe',
            'C': 'Phe',
            'A': 'Leu',
            'G': 'Leu'
        },
        'C': {
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Ser',
            'G': 'Ser'
        },
        'A': {
            'U': 'Tyr',
            'C': 'Tyr',
            'A': 'STP',
            'G': 'STP'
        },
        'G': {
            'U': 'Cys',
            'C': 'Cys',
            'A': 'STP',
            'G': 'Trp'
        }
    },
    'C': {
        'U': {
            'U': 'Leu',
            'C': 'Leu',
            'A': 'Leu',
            'G': 'Leu'
        },
        'C': {
            'U': 'Pro',
            'C': 'Pro',
            'A': 'Pro',
            'G': 'Pro'
        },
        'A': {
            'U': 'His',
            'C': 'His',
            'A': 'Gln',
            'G': 'Gln'
        },
        'G': {
            'U': 'Arg',
            'C': 'Arg',
            'A': 'Arg',
            'G': 'Arg'
        }
    },
    'A': {
        'U': {
            'U': 'Ile',
            'C': 'Ile',
            'A': 'Ile',
            'G': 'Met'
        },
        'C': {
            'U': 'Thr',
            'C': 'Thr',
            'A': 'Thr',
            'G': 'Thr'
        },
        'A': {
            'U': 'Asn',
            'C': 'Asn',
            'A': 'Lys',
            'G': 'Lys'
        },
        'G': {
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Arg',
            'G': 'Arg'
        }
    },
    'G': {
        'U': {
            'U': 'Val',
            'C': 'Val',
            'A': 'Val',
            'G': 'Val'
        },
        'C': {
            'U': 'Ala',
            'C': 'Ala',
            'A': 'Ala',
            'G': 'Ala'
        },
        'A': {
            'U': 'Asp',
            'C': 'Asp',
            'A': 'Glu',
            'G': 'Glu'
        },
        'G': {
            'U': 'Gly',
            'C': 'Gly',
            'A': 'Gly',
            'G': 'Gly'
        }
    }
}

mrnaToBialkaTranslator1 = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STP', 'UAG': 'STP',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STP', 'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

dnaToMrnaTranslator = {
    'A': 'U',
    'C': 'G',
    'T': 'A',
    'G': 'C'
}
mrnaToDnaTranslator = {
    'A': 'T',
    'U': 'A',
    'C': 'G',
    'G': 'C'
}


#input
#inp = input('Typ, Kod\n').split(', ') # f.e. "mRNA;TGTGCCGAATT"
inp = "DNA, ACACGGCTTAAC".split(', ')
typ, kod = inp
kod = kod.upper()


#logik
dnaOut = ''
mrnaOut = ''
bialkoOut = ''
if typ == 'DNA':
    dnaOut = kod
    #DNA -> mRNA
    for i in range(len(kod)):
        mrnaOut += dnaToMrnaTranslator[kod[i]]
elif typ == 'mRNA' or typ == 'RNA':
    mrnaOut = kod
    #mRNA -> DNA
    for i in range(len(kod)):
        dnaOut += mrnaToDnaTranslator[kod[i]]

#0
for i in range(0, len(mrnaOut), 3):
    bialkoOut += mrnaToBialkaTranslator0[mrnaOut[i]][mrnaOut[i+1]][mrnaOut[i+2]]

#1
def splitOnThree(str):
    return [str[start:start+3] for start in range(0, len(str), 3)]
kod = splitOnThree(mrnaOut)
for i in range(len(kod)):
    bialkoOut += mrnaToBialkaTranslator1[kod[i]]



#print ktory zamienisz na return w kodzie
print(dnaOut)
print(mrnaOut)
print(bialkoOut)



