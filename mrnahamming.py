from Bio.Seq import Seq


def rna_hamming(s1,s2): #working
    #matches G's to T's/U's, A's to T's/U's, and G's to C's
    #A hamming distance function that returns the hamming distance of the match between two ssRNA sequences.
    
    
    

    s1rev = str(Seq(s1).reverse_complement()) 
    
    
    the_zip = zip(s1rev, s2, s1[::-1])
   
    
    hamming = 0

    for charA, charB, charC in the_zip:
        
        if charA == charB:
             hamming = hamming + 0

        elif charA == "C" and charB == "T" and charC == "G":
                hamming = hamming + 0
        
        elif charA == "A" and charB == "G" and charC == "T":
                hamming = hamming + 0
                
        elif charA == "C" and charB == "U" and charC == "G":
                hamming = hamming + 0
        
        elif charA == "A" and charB == "G" and charC == "U":
                hamming = hamming + 0
        else:
            hamming = hamming + 1
        #print "hamming" + str(hamming)
        #print "s1" + str(s1)
        #print "s1rev" + str(s1rev)
        #print "s2" + str(s2)
    return hamming

def piece_maker(s, smallest, biggest): #working
    print "piece_maker start"
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
    print pieces
    return pieces


def piece_match(pieces, s):
    print "starting piece_match"
    targets =[]
    
    pieces_copy = pieces
    for piece in pieces:
        for piece_copy in pieces_copy:
            if piece[2] < piece_copy[1]:

                

                if len(piece[0]) ==len(piece_copy[0]):

                    if rna_hamming(piece[0], piece_copy[0]) == 0:
                        print "one match"

                        range1=set(range(piece[1],piece[2]))
                        range2=set(range(piece_copy[1], piece_copy[2]))
                        if not range1.intersection(range2):
                            target = piece + piece_copy
                            #print "target: {0}".format(target)
                            #print "before extend " + str(target)
                            #target = target_extend_inwards(target, s)
                            #print "after inwards " + str(target)
                            #target = target_extend_outwards(target, s)
                            #print "after outwards " + str(target)
                            if not target in targets:
                                #print "after nondup " + str(targets) + "  "
                                targets.append(target)

    return targets

def controlpanel(s):
    print "starting"
    pieces = piece_maker(s,12, 20)
    #print pieces
    targets = piece_match(pieces, s)
    print targets


seq_file = "TTTAATTTCTCCGAGGCCAGCCAGAGCAGGTTTGTTGGCAGCAGTACCCCTCCAGCAGTCACGCGACCAGCCAATCTCCCGGCGGCGCTCGGGGAGGCGGCGCGCTCGGGAACGAGGGGAGGTGGCGGAACCGCGCCGGGGCCACCTTAAGGCCGCGCTCGCCAGCCTCGGCGGGGCGGCTCCCGCCGCCGCAACCAATGGATCTCCTCCTCTGTTTAAATAGACTCGCCGTGTCAATCATTTTCTTCTTCGTCAGCCTCCCTTCCACCGCCATATTGGGCCACTAAAAAAAGGGGGCTCGTCTTTTCGGGGTGTTTTTCTCCCCCTCCCCTGTCCCCGCTTGCTCACGGCTCTGCGACCCGACGCCGGCAAGGTTTGGAGAGCGGCTGGGTTCGCGGGACCCGCGGGCTTGCACCCGCCCAGACTCGGACGGGCTTTGCCACCCTCTCCGCTTGCCTGGTCCCCTCTCCTCTCCGCCCTCCCGCTCGCCAGTCCATTTGATCAGCGGAGACTCGGCGGCCGGGCCGGGGCTTCCCCGCAGCCCCTGCGCGCTCCTAGAGCTCGGGCCGTGGCTCGTCGGGGTCTGTGTCTTTTGGCTCCGAGGGCAGTCGCTGGGCTTCCGAGAGGGGTTCGGGCTGCGTAGGGGCGCTTTGTTTTGTTCGGTTTTGTTTTTTTGAGAGTGCGAGAGAGGCGGTCGTGCAGACCCGGGAGAAAGATGTCAAACGTGCGAGTGTCTAACGGGAGCCCTAGCCTGGAGCGGATGGACGCCAGGCAGGCGGAGCACCCCAAGCCCTCGGCCTGCAGGAACCTCTTCGGCCCGGTGGACCACGAAGAGTTAACCCGGGACTTGGAGAAGCACTGCAGAGACATGGAAGAGGCGAGCCAGCGCAAGTGGAATTTCGATTTTCAGAATCACAAACCCCTAGAGGGCAAGTACGAGTGGCAAGAGGTGGAGAAGGGCAGCTTGCCCGAGTTCTACTACAGACCCCCGCGGCCCCCCAAAGGTGCCTGCAAGGTGCCGGCGCAGGAGAGCCAGGATGTCAGCGGGAGCCGCCCGGCGGCGCCTTTAATTGGGGCTCCGGCTAACTCTGAGGACACGCATTTGGTGGACCCAAAGACTGATCCGTCGGACAGCCAGACGGGGTTAGCGGAGCAATGCGCAGGAATAAGGAAGCGACCTGCAACCGACGATTCTTCTACTCAAAACAAAAGAGCCAACAGAACAGAAGAAAATGTTTCAGACGGTTCCCCAAATGCCGGTTCTGTGGAGCAGACGCCCAAGAAGCCTGGCCTCAGAAGACGTCAAACGTAAACAGCTCGAATTAAGAATATGTTTCCTTGTTTATCAGATACATCACTGCTTGATGAAGCAAGGAAGATATACATGAAAATTTTAAAAATACATATCGCTGACTTCATGGAATGGACATCCTGTATAAGCACTGAAAAACAACAACACAATAACACTAAAATTTTAGGCACTCTTAAATGATCTGCCTCTAAAAGCGTTGGATGTAGCATTATGCAATTAGGTTTTTCCTTATTTGCTTCATTGTACTACCTGTGTATATAGTTTTTACCTTTTATGTAGCACATAAACTTTGGGGAAGGGAGGGCAGGGTGGGGCTGAGGAACTGACGTGGAGCGGGGTATGAAGAGCTTGCTTTGATTTACAGCAAGTAGATAAATATTTGACTTGCATGAAGAGAAGCAATTTTGGGGAAGGGTTTGAATTGTTTTCTTTAAAGATGTAATGTCCCTTTCAGAGACAGCTGATACTTCATTTAAAAAAATCACAAAAATTTGAACACTGGCTAAAGATAATTGCTATTTATTTTTACAAGAAGTTTATTCTCATTTGGGAGATCTGGTGATCTCCCAAGCTATCTAAAGTTTGTTAGATAGCTGCATGTGGCTTTTTTAAAAAAGCAACAGAAACCTATCCTCACTGCCCTCCCCAGTCTCTCTTAAAGTTGGAATTTACCAGTTAATTACTCAGCAGAATGGTGATCACTCCAGGTAGTTTGGGGCAAAAATCCGAGGTGCTTGGGAGTTTTGAATGTTAAGAATTGACCATCTGCTTTTATTAAATTTGTTGACAAAATTTTCTCATTTTCTTTTCACTTCGGGCTGTGTAAACACAGTCAAAATAATTCTAAATCCCTCGATATTTTTAAAGATCTGTAAGTAACTTCACATTAAAAAATGAAATATTTTTTAATTTAAAGCTTACTCTGTCCATTTATCCACAGGAAAGTGTTATTTTTCAAGGAAGGTTCATGTAGAGAAAAGCACACTTGTAGGATAAGTGAAATGGATACTACATCTTTAAACAGTATTTCATTGCCTGTGTATGGAAAAACCATTTGAAGTGTACCTGTGTACATAACTCTGTAAAAACACTGAAAAATTATACTAACTTATTTATGTTAAAAGATTTTTTTTAATCTAGACAATATACAAGCCAAAGTGGCATGTTTTGTGCATTTGTAAATGCTGTGTTGGGTAGAATAGGTTTTCCCCTCTTTTGTTAAATAATATGGCTATGCTTAAAAGGTTGCATACTGAGCCAAGTATAATTTTTTGTAATGTGTGAAAAAGATGCCAATTATTGTTACACATTAAGTAATCAATAAAGAAAACTTCCATAGCTATT"
s = seq_file

controlpanel(s)




    
