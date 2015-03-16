#seq_file = "GGGGCCGTAGCTCAGCTGGGAGAGCACCTGCTTTGCAAGCAGGGGGTCGTCGGTTCGATCCCGTCCGGCTCCACCA"
#This one has 3bp long complement to find.  Program will only fold 4bp+ stretches now
#http://trna.bioinf.uni-leipzig.de/DataOutput/Result?ID=tdbD00003770
#alanine from Brucella melitensis

#seq_file = "GGGGGCUCUGUUGGUUCUCCCGCAACGCUACUCUGUUUACCAGGUCAGGUCCGGAAGGAAGCAGCCAAGGCAGAUGACGCGUGUGCCGGGAUGUAGCUGGCAGGGCCCCCACC"
#seq_file = 'GCCGGGCGCGGTGGCGCGTGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCTGGAGGATCGCTTGAGTCCAGGAGTTCTGGGCTGTAGTGCGCTATGCCGATCGGGTGTCCGCACTAAGTTCGGCATCAATATGGTGACCTCCCGGGAGCGGGGGACCACCAGGTTGCCTAAGGAGGGGTGAACCGGCCCAGGTCGGAAACGGAGCAGGTCAAAACTCCCGTGCTGATCAGTAGTGGGATCGCGCCTGTGAATAGCCACTGCACTCCAGCCTGGGCAACATAGCGAG'
#http://www.ncbi.nlm.nih.gov/nuccore/527047183?report=fasta

seq_file = "AATTTTAAAGAGTTTGATCCTGGCTCAGGATTAACGCTGGCGGCATGCCTAATACATGCAAATCGAACGAAGCCTTTTAGGCTTAGTGGTGAACGGGTGAGTAACACGTATCCAATCTACCCTTAAGTTGGGGATAACTAGTCGAAAGATTAGCTAATACCGAATAATAACATCAATATCGCATGAGAAGATGTAGAAAGTCGCTCTTTGTGGCGACGCTTTTGGATGAGGGTGCGACGTATCAGATAGTTGGTGAGGTAATGGCTCACCAAGTCAATGACGCGTAGCTGTACTGAGAGGTAGAACAGCCACAATGGGACTGAGACACGGCCCATACTCCTACGGGAGGCAGCAGTAGGGAATTTTTCACAATGGGCGCAAGCCTTATGAAGCAATGCCGCGTGAACGATGAAGGTCTTATAGATTGTAAAGTTCTTTTATATGGGAAGAAACGCTAAGATAGGAAATGATTTTAGTTTGACTGTACCATTTGAATAAGTATCGGCTAACTATGTGCCAGCAGCCGCGGTAATACATAGGATGCAAGCGTTATCCGGATTTACTGGGCGTAAAACGAGCGCAGGCGGGTTTGTAAGTTTGGTATTAAATCTAGATGCTTAACGTCTAGCTGTATCAAAAACTGTAAACCTAGAGTGTAGTAGGGAGTTGGGGAACTCCATGTGGAGCGGTAAAATGCGTAGATATATGGAAGAACACCGGTGGCGAAGGCGCCAACTTGGACTATCACTGACGCTTAGGCTCGAAAGTGTGGGGAGCAAATAGGATTAGATACCCTAGTAGTCCACACCGTAAACGATCATCATTAAATGTCGGCCCGAATGGGTCGGTGTTGTAGCTAACGCATTAAATGATGTGCCTGGGTAGTACATTCGCAAGAATGAAACTCAAACGGAATTGACGGGGACCCGCACAAGTGGTGGAGCATGTTGCTTAATTTGACAATACACGTAGAACCTTACCTAGGTTTGACATCTATTGCGATGCTATAGAAATATAGTTGAGGTTAACAATATGACAGGTGGTGCATGGTTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCCTTTCGTTAGTTACTTTTCTAGCGATACTGCTACCGCAAGGTAGAGGAAGGTGGGGATGACGTCAAATCATCATGCCCCTTATATCTAGGGCTGCAAACGTGCTACAATGGCTAATACAAACTGCTGCAAAATCGTAAGATGAAGCGAAACAGAAAAAGTTAGTCTCAGTTCGGATAGAGGGCTGCAATTCGTCCTCTTGAAGTTGGAATCACTAGTAATCGCGAATCAGACATGTCGCGGTGAATACGTTCTCGGGTCTTGTACACACCGCCCGTCAAACTATGGGAGCTGGTAATATCTAAAACCGCAAAGCTAACCTTTTGGAGGCATGCGTCTAGGGTAGGATCGGTGACTGGAGT"


from Bio.Seq import Seq

def rna_hamming(s1,s2):
    #matching G's to T's.,
    #is currently also matching C's to T's
    
    
    s1rev = str(Seq(s1).reverse_complement())
    the_zip = zip(s1rev, s2, s1)
    hamming = 0
    
    for charA, charB, charC in the_zip:
        #print "CharA: {0}, CharB: {1}".format(charA, charB)
        if charA == charB:
             hamming = hamming + 0
             
        elif charC == "G" and charA == "C" and charB == "T":
                hamming = hamming + 0
        elif charC == "T" and charA == "G" and charB == "T":
                hamming = hamming + 0                           
        else:
            hamming = hamming + 1
    return hamming        


def piece_maker(s, smallest, biggest):
    pieces =[]
    
    s = s# + s[0:biggest]
    length = len(s)
    j = 0  #beginning of piece
    end = length-1  #end of piece
    k=j+biggest
    while j<length-biggest:
        while k > j+smallest-2:
            piece = s[j:k+1]
            if piece.isalpha(): #for later when  sequences with dashes are run through
                pieces.append([piece, j, k+1]) # all the pieces with positional information #the positional tracking is off)
            k = k - 1
            #print k
            
        j = j + 1
        if j==length-biggest and j!=length:
            biggest = biggest -1
        k=j+biggest
    return pieces

def target_extend_outwards(target, s):
    #add on outer end until hamming threshold is reached
    if target[1] == 0:
        return target
    if target[5] ==len(s):
        return target
    targetA = target[0:3]
    targetB = target[3:6]
    leftbound = targetA[2]
    rightbound = targetB[1]
    hamm = 0
    while hamm == 0:
        tmptargetA = [s[targetA[1]-1:leftbound], targetA[1]-1, leftbound]
        tmptargetB = [s[rightbound:targetB[2]+1], rightbound, targetB[2]+1]
        hamm = rna_hamming(tmptargetA[0], tmptargetB[0])
        if hamm!= 0:
            return (targetA + targetB)
        else:
            targetA=tmptargetA
            targetB = tmptargetB
            if targetA[1] == 0 or targetB[2] == len(s):
                #print "end targetA {0}, and targetB {1}".format(targetA, targetB)
                return (targetA + targetB)
           
    #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (targetA + targetB)

def target_extend_inwards(target, s): 
    #add on internally until hamming threshold is reached
    if target[4]-target[2] == 4:
        return target
    targetA = target[0:3]
    targetB = target[3:6]
    leftbound = targetA[1]
    rightbound = targetB[2]
    hamm = 0
    while hamm==0 and (targetB[1] - targetA[2]) > 3:
        tmptargetA = [s[leftbound:targetA[2]+1], leftbound, targetA[2]+1]
        tmptargetB = [s[targetB[1]-1:rightbound], targetB[1]-1, rightbound]
        
        hamm = rna_hamming(tmptargetA[0], tmptargetB[0])
        if hamm!=0:
            return (targetA + targetB)
        else:
            targetA=tmptargetA
            targetB = tmptargetB
            if (targetB[1] - targetA[2]) == 3:
                #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
                return (targetA + targetB)
           
    #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (targetA + targetB)

def target_extend_outwards2(target, s):
    #extend unbroken hairpin seeds that fall outside of the initial 20nt range
    if target[1] == 0:
        return target
    if target[5] ==len(s):
        return target
    targetA = target[0:3]
    targetB = target[3:6]
    leftbound = targetA[2]
    rightbound = targetB[1]
    hamm = 0
    while hamm < 1:
        targetA = [s[targetA[1]-1:leftbound], targetA[1]-1, leftbound]
        targetB = [s[rightbound:targetB[2]+1], rightbound, targetB[2]+1]
        hamm = rna_hamming(targetA[0], targetB[0])
        if targetA[1] == 0 or targetB[2] == len(s):
            #print "end targetA {0}, and targetB {1}".format(targetA, targetB)
            return (targetA + targetB)
           
    #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (targetA + targetB)




def piece_match(pieces, s):
    targets =[]
    pieces_copy = pieces
    for piece in pieces:
        for piece_copy in pieces_copy:
            if piece[2] < piece_copy[1] and 3<(piece_copy[1]-piece[2])<12:
                
                #if piece[1] > seqlength:
                #    piece[1] = piece[1]-seqlength
            
                if len(piece[0]) ==len(piece_copy[0]):
                    
                    if rna_hamming(piece[0], piece_copy[0]) == 0:

                        range1=set(range(piece[1],piece[2]))
                        range2=set(range(piece_copy[1], piece_copy[2]))
                        if not range1.intersection(range2): 
                            target = piece + piece_copy
                            #print "target: {0}".format(target)
                            target = target_extend_outwards(target, s)
                            target = target_extend_inwards(target, s)
                            if not target in targets:
                                #print target
                                targets.append(target)
    
    return targets 
                           
#s1 = "AAATAAAGAAA"
#s2 = "TTTTTTTATTT"
s=seq_file
print len(s)

#print rna_hamming(s1,s2)                            

pieces = piece_maker(s,4, 10)                    

redtargets = piece_match(pieces, s)
print "reduced target list :"
for group in redtargets:
    print group
#print len(redtargets)  #only 82 target seed for the 16s 28 arms
    #need to get an accurate structure and sequence of a 16s
    
          

    
    
    
