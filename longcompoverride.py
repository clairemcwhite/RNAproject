#takes a sequence. Then breaks it into 21 letter long areas sequentially (0 through 22, 1 through 23, 2 through 24 , n-21 through n.
#makes every possible variant "chunk" of those 21 letters
#it then makes a list of every reverse complement "comp" of those chunks
#if a reverse complement chunk is found in the original chunck list, it is kept as an intersect:
#
#
# the first round is checking for 4bp and greater complements.
#The second round will check for complements of 4bp with an internal mismatch (not made yet)
#wikipedia hs srp structures

#Database with dotbracket
#http://www.lix.polytechnique.fr/~ponty/enseignement/MathewsRNASorted.faa

# current goals:
#1. make a count of bonds per unit of length ( 25?).  If there are a certain number of bonds/unit lenght/ then override local bonding.  Do this step before calculating last folded posiotion.
#though longer bonds realisticaly supercede local bonds after local bonds form.  However, position of large bonded stretches then influences the conformation of loal bonds after that.
#so long bonded stretches are the primary determiner of foldedness?
#Look into RNA chaperones.

#2. make a bonded region to - translator.
# TGGGGA...ACCCCT -> T----A....A----T, and T-A and A-T




from Bio.Seq import Seq
import pairwise2alignrnamod as pairwise2
from Bio.pairwise2 import format_alignment
from operator import itemgetter

def hamming_distance(s1, s2):
    
    """Return the Hamming distance between equal-length sequences"""
    #print s1
    s1rev = str(Seq(s1).reverse_complement())
    
    #alignments = pairwise2.align.globalxx(s1, s2)
    
    #return alignments
    
    
    for a in pairwise2.align.globalxx(s1rev, s2):
        #print(format_alignment(*a))
        if a[2] > 25:
            print 'a:   '+ str(a)
            print 's1:   '+ str(s1)
            print 's1rev:   '+ str(s1rev)
            print 's2:   '+ str(s2) + "\n"
            return a
        else:
            return 0
       
        

def revcomp_hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""

    s1 = str(Seq(s1).reverse_complement())
    
    the_zip = zip(s1, s2)
    if sum(ch1 != ch2 for ch1, ch2 in the_zip)==0:
        #print "the matching zip" + str(the_zip)
        return sum(ch1 != ch2 for ch1, ch2 in the_zip)
    
  
    
def internal_hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    s1 = str(Seq(s1).reverse_complement())
    the_zip = zip(s1[1:-1], s2[1:-1])
    if s1[:1] == s2[:1] and s1[-1:] == s2[-1:]:  #check for one mismatch internally if the beginning and end are the same
        
        return sum(ch1 != ch2 for ch1, ch2 in the_zip)
    else:
        return 0

#use hamming distance to deal with wobble pair problem
mismatchtargets = []


#seq_file = "GGGGCCGTAGCTCAGCTGGGAGAGCACCTGCTTTGCAAGCAGGGGGTCGTCGGTTCGATCCCGTCCGGCTCCACCA"
#This one has 3bp long complement to find.  Program will only fold 4bp+ stretches now
#http://trna.bioinf.uni-leipzig.de/DataOutput/Result?ID=tdbD00003770
#alanine from Brucella melitensis

#seq_file = "GGGGGCUCUGUUGGUUCUCCCGCAACGCUACUCUGUUUACCAGGUCAGGUCCGGAAGGAAGCAGCCAAGGCAGAUGACGCGUGUGCCGGGAUGUAGCUGGCAGGGCCCCCACC"

seq_file = 'GCCGGGCGCGGTGGCGCGTGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCTGGAGGATCGCTTGAGTCCAGGAGTTCTGGGCTGTAGTGCGCTATGCCGATCGGGTGTCCGCACTAAGTTCGGCATCAATATGGTGACCTCCCGGGAGCGGGGGACCACCAGGTTGCCTAAGGAGGGGTGAACCGGCCCAGGTCGGAAACGGAGCAGGTCAAAACTCCCGTGCTGATCAGTAGTGGGATCGCGCCTGTGAATAGCCACTGCACTCCAGCCTGGGCAACATAGCGAG'
#http://www.ncbi.nlm.nih.gov/nuccore/527047183?report=fasta


#######position marking
prevpos1=0#locations of previous folds
prevpos2=0
prevpos3=0
prevpos4=0
maxmark = 0 #the furthest point that the loop has been folded
firstfoldpos = 0 #location of the first fold (for folding 3' end to 5' end)
last = 0

#####file related
tempseq_file2 =''
extendedseq_file = []
dashedseq_file =''
tempseq_file = seq_file
length = len(seq_file)

#####storage
nonoverlapcomp = []
paired = []
testlist= []
pieces =[]
targets = []
local = []
longpieces=[]


#######counters
start = 0 # 9 for trnas, 0 otherwise. 
n = 4 # start looking for reverse complements of 4bp or above.
counter = 0
print "starting..."


"Looking for n long nuc segment with most bonds"  
#############################################################
j = 0  #beginning of piece
end = length-1  #end of piece

while j<end-30:
    
    longpiece = seq_file[j:j+30]

    #if piece.isalpha(): #for later when  sequences with dashes are run through
        #pieces.append(piece)  # all the pieces
    longpieces.append([longpiece, start+j, start+j+20]) # all the pieces with positional information #the positional tracking is off)

    j = j + 1
#print longpieces
    

longpieces_copy = longpieces
for longpiece in longpieces:
    for longpiece_copy in longpieces_copy:
        if longpiece[2] < longpiece_copy[1]:

          longdistance = hamming_distance(longpiece[0], longpiece_copy[0])
          #if longdistance != 0:
              #print str(longpiece) + "  " + str(longpiece_copy) + str(longdistance)
          #print "alignments   " + str(longdistance)
          #if longdistance < 25:
           #     print "{0} is separated from {1} by hamming of {2}".format(longpiece, longpiece_copy, longdistance)
            #    print longpiece_copy[0]

        
    ##                targets.append(piece + piece_copy)
    ##                ########################################
    ##                if (piece_copy[1]-piece[2])<25:
    ##                    if piece[1] > last:
                
    ##
    ##                        range1=set(range(piece[1],piece[2]))
    ##                        range2=set(range(piece_copy[1], piece_copy[2]))
    ##                        if not range1.intersection(range2): 
    ##                            
    ##                            local.append(piece + piece_copy)
    ##                            last = piece_copy[2]
    ##                         #print "last" + str(last)
                     ############################################### 


print "Past the long pieces part"






while n > 3: #only looking currently for reverse complements of 4bp or longer
    print "loop starting..."

    pieces = []  #the current sections of block broken up.
    piece_pos =[] #where in the sequence each piece (for checking overlaps)
    piece_comps = [] #The reverse complements of all the pieces

    ##########Which sequence version to use as the working sequence
    if counter == 0:  #there's no loop increasing counter for now
        #if not extendedseq_file:  #if the first fold has not been found yet, use the original file
        working_seq = seq_file

        #else:
        #    working_seq = extendedseq_file  #if the first fold has been found, concatenate the sequence previous to the first fold to the end of the sequence.  (the tail pairs with the head)
    
    if counter ==0: #there's no loop increasing counter for now
        block = working_seq[start:start+length] #the current area of the sequence
    
    ##########This breaks the sequence into pieces like 12345678, 1234567, 123456,...12, 2345678, 234567, 23456, etc...) and creates a list of all chunk reverse complements
    block = block + working_seq[0:10]
    len_block = len(block)
    j = 0  #beginning of piece
    end = length-1  #end of piece
    k=j+10
    while j<end:
        while k > j:
            piece = block[j:k+1]

            if piece.isalpha(): #for later when  sequences with dashes are run through
                #pieces.append(piece)  # all the pieces
                pieces.append([piece, start+j, start+k+1]) # all the pieces with positional information #the positional tracking is off)

                #current = Seq(piece)
                #currentrevcomp = str(current.reverse_complement())
                #piece_comps.append(currentrevcomp)#all the revcomps
                

                
            k = k - 1
        j = j + 1
        k=j+10
     ##########
    
    pieces = sorted(pieces, key = itemgetter(1))
    #at this point, have the full list full of all 
     
        
    pieces_copy = pieces
    for piece in pieces:
        for piece_copy in pieces_copy:
            if piece[2] < piece_copy[1]:
                
                if piece[1] > length:
                    piece[1] = piece[1]-length
            
                if len(piece[0]) ==len(piece_copy[0]) and len(piece[0]) > n-1:
                    #print "before rchd" + str(piece[0])
                    if revcomp_hamming_distance(piece[0], piece_copy[0]) ==0:

                        targets.append(piece + piece_copy)
                        ########################################
                        if (piece_copy[1]-piece[2])<25:
                            if piece[1] > last:

                                range1=set(range(piece[1],piece[2]))
                                range2=set(range(piece_copy[1], piece_copy[2]))
                                if not range1.intersection(range2): 
                                    
                                    local.append(piece + piece_copy)
                                    last = piece_copy[2]
                                 #print "last" + str(last)
                         ############################################### 
                        
                if len(piece[0]) == len(piece_copy[0]) and len(piece[0])>6:
                    if internal_hamming_distance(piece[0], piece_copy[0]) ==1:  #if there's one internal mismatch
                        #targets.append(piece + piece_copy) no mismatch for first override step
                
                        #############################################
                        if (piece_copy[1]-piece[2])<25:
                            if piece[1] > last:
                                #print piece
                                #print piece_comp
                                range1=set(range(piece[1],piece[2]))
                                range2=set(range(piece_copy[1], piece_copy[2]))
                                
                                if not range1.intersection(range2): 
                                    
                                    local.append(piece + piece_copy)
                                    last=piece_copy[2]
                        #################################################           
                #if firstfoldpos == 0:
                    #firstfoldpos = min(target_range)
                    #extendedseq_file = seq_file + seq_file[0:firstfoldpos]
 
    #long comp detection only need to happen once(?).  Then feed remaining sequence back up to  the block market to look for real local folds.
    #do here: make list of "global" folds, where fold are separated by > 40?
    



                  
##    for t in range(len(working_seq)):
##        working_range = range(t, t+20)
##        stringrange=str(t)+ "," +str(t+20)
##        
##        for p in range(len(targets)):
##            current_last = 0
##            
##            if (targets[p][5]-targets[p][1])>100 and targets[p][1]>current_last:
##                if targets[p][1] in working_range:
##                    targets[p][2] = current_last
##                    if stretch.has_key(stringrange):
##                        stretch[stringrange] += (targets[p][2]-targets[p][1])
##                    else:
##                        stretch[stringrange] = (targets[p][2]-targets[p][1])
##                    #print targets[p]
##                    #print working_range
##            print p
##                #if targets[2] in range of t:
##                 #   print targets[2]
##            p = p+1
##        print "tee" + str(t)
##        t = t + 1
##    print stretch        

        
        
    #for pair in targets:
     #   print pair

    #start = 0
    #nonoverlapcomp = []
    n = n-1

#print "all targets:" + str(targets)


    
for i in range(len(targets)):    
#    [(targets[i][j]-length) for j in [4,5] if (targets[i][j] > length-1)]   bad list comprehension 
    if targets[i][4] > length-1:
        targets[i][4] = targets[i][4]-length
        
    if targets[i][5] > length-1:
        targets[i][5] = targets[i][5]-length

print "The original sequence: " + str(seq_file)
        #for making dot bracket format later
    #dot = ""
    #for char in tempseq_file:
    #    if char.isalpha():
    #        dot = dot + "."
    #    else:
    #        dot = dot + char
    #print "Dot bracket format:    "+ str(dot)        

sorted_list = sorted(local, key=itemgetter(1,4))
#print "Folded areas" + str(sorted_list)

for item in range(len(sorted_list)):
    print 'fold #{0}: {1}'.format(item+1, sorted_list[item])
    
