import sys
sys.stdout.reconfigure(encoding='utf-8')

print(None == False)
from defs import occurance

ipa = "The First Noel the Angels did say Was to certain poor shepherds in fields where they lay In fields where they lay keeping their sheep On a cold winter's night that was so deep Noel Noel Noel Noel Born is the King of Israel They looked up and saw a star Shining in the East beyond them far And to the earth it gave great light And so it continued both day and night Noel Noel Noel Noel Born is the King of Israel"
print(occurance(ipa.lower().split(' ')).keys())