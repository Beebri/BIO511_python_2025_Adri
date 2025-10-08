# Practical 2: Python Loops
#=================================================================================================
#3.0 make a list 
mylist = ["grape", "apple", "banana", "orange", "kiwi", "mango", "pear"]
type(mylist)
print(mylist)
print(mylist[0])
##=================================================================================================
#3.1 simple loops
for fruit in mylist:
    print(fruit)
    
#enumerated_list = enumerate(mylist)
#print(list(enumerated_list))
#import pdb; pdb.set_trace()
print("loop of interest)")
for i in enumerate(mylist):
    print(f"0 index:{i[0]}") 
    print(i[1])
    
for i in enumerate(mylist):
    if i[0] < 6:
        print(f"0 index:{i[0]}") 
        print(i[1])
##=================================================================================================
# 3.2 Nested loops
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']
for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)
# Stop and Start codon filtering
stop_codon = 
start_codon = 
for sequence in sequences:
  for codon in codons:
   if codon in sequence is 'TAG':
     print( "stop codon" + codon + "is in" + sequence)
   elif
