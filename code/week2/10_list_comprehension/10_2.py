# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 10. list compehension

# Παράδειγα 10.1
# Να δημιουργήσετε μια λίστα με τα
# αρχικά γράμματα όλων των λέξεων της πρώτης στροφής
# του εθνικού μας ύμνου.


ymnos = '''
Σὲ γνωρίζω ἀπὸ τὴν κόψι
τοῦ σπαθιοῦ τὴν τρομερή,
σὲ γνωρίζω ἀπὸ τὴν ὄψι,
ποὺ μὲ βιὰ μετράει τὴν γῆ.
'''

first = [ (x[0], ord(x[0])) for x in ymnos.split() ]
print(first)
