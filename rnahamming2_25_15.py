
#seq_file =
#"GGGGCCGTAGCTCAGCTGGGAGAGCACCTGCTTTGCAAGCAGGGGGTCGTCGGTTCGATCCCGTCCGGCTCCACCA"
#This one has 3bp long complement to find.  Program will only fold
#4bp+ stretches now
#http://trna.bioinf.uni-leipzig.de/DataOutput/Result?ID=tdbD00003770
#alanine from Brucella melitensis

#seq_file = "GGGGGCUCUGUUGGUUCUCCCGCAACGCUACUCUGUUUACCAGGUCAGGUCCGGAAGGAAGCAGCCAAGGCAGAUGACGCGUGUGCCGGGAUGUAGCUGGCAGGGCCCCCACC"
#seq_file = 'GCCGGGCGCGGTGGCGCGTGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCTGGAGGATCGCTTGAGTCCAGGAGTTCTGGGCTGTAGTGCGCTATGCCGATCGGGTGTCCGCACTAAGTTCGGCATCAATATGGTGACCTCCCGGGAGCGGGGGACCACCAGGTTGCCTAAGGAGGGGTGAACCGGCCCAGGTCGGAAACGGAGCAGGTCAAAACTCCCGTGCTGATCAGTAGTGGGATCGCGCCTGTGAATAGCCACTGCACTCCAGCCTGGGCAACATAGCGAG'
#http://www.ncbi.nlm.nih.gov/nuccore/527047183?report=fasta

#seq_file = "AAATTGAAGAGTTTGATCATGGCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAACAGGAAGAAGCTTGCTCTTTGCTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCTGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCGCAAGACCAAAGAGGGGGACCTTCGGGCCTCTTGCCATCGGATGTGCCCAGATGGGATTAGCTAGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGATGACCAGCCACACTGGAACTGAGACACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCAGCCATGCCGCGTGTATGAAGAAGGCCTTCGGGTTGTAAAGTACTTTCAGCGGGGAGGAAGGGAGTAAAGTTAATACCTTTGCTCATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTCAGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCATCTGATACTGGCAAGCTTGAGTCTCGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACGAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTCGACTTGGAGGTTGTGCCCTTGAGGCGTGGCTTCCGGAGCTAACGCGTTAAGTCGACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTGGTCTTGACATCCACGGAAGTTTTCAGAGATGAGAATGTGCCTTCGGGAACCGTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGGTCCGGCCGGGAACTCAAAGGAGACTGCCAGTGATAAACTGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGACCAGGGCTACACACGTGCTACAATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTCATAAAGTGCGTCGTAGTCCGGATTGGAGTCTGCAACTCGACTCCATGAAGTCGGAATCGCTAGTAATCGTGGATCAGAATGCCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGGTAGCTTAACCTTCGGGAGGGCGCTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGGGAACCTGCGGTTGGATCACCTCCTTA"
#http://rna.ucsc.edu/rnacenter/xrna/xrna_gallery.html
#http://www.ebi.ac.uk/ena/data/view/A14565&display=fasta
#http://www.arb-silva.de/browser/ssu-121/silva/CP001368
#currently reliably(?) finding hairpin turn ends
seq_file = "AAATTGAAGAGTTTGATCATGGCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAACAGGAAGAAGCTTGCTTCTTTGCTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCTGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCGCAAGACCAAAGAGGGGGACCTTCGGGCCTCTTGCCATCGGATGTGCCCAGATGGGATTAGCTAGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGATGACCAGCCACACTGGAACTGAGACACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCAGCCATGCCGCGTGTATGAAGAAGGCCTTCGGGTTGTAAAGTACTTTCAGCGGGGAGGAAGGGAGTAAAGTTAATACCTTTGCTCATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTCAGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCATCTGATACTGGCAAGCTTGAGTCTCGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACGAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTCGACTTGGAGGTTGTGCCCTTGAGGCGTGGCTTCCGGAGCTAACGCGTTAAGTCGACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTGGTCTTGACATCCACGGAAGTTTTCAGAGATGAGAATGTGCCTTCGGGAACCGTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGGTCCGGCCGGGAACTCAAAGGAGACTGCCAGTGATAAACTGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGACCAGGGCTACACACGTGCTACAATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTCATAAAGTGCGTCGTAGTCCGGATTGGAGTCTGCAACTCGACTCCATGAAGTCGGAATCGCTAGTAATCGTGGATCAGAATGCCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGGTAGCTTAACCTTCGGGAGGGCGCTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGGGAACCTGCGGTTGGATCACCTCCTTA" #
#seq_file = "GAAGTCGTAACAAGGTAACCGTAGGGGAACCTGCGGTTGGATCACCTCCT"
#seq_file = seq_file[0:500]
from Bio.Seq import Seq
from collections import defaultdict

# new strategy: get nuclei
# built out with Ns for shorter segments
# of the secondary folds, select the one closest to the ends of the primary fold


#true fold
#[['GAGTAAAG', 24, 32, 'CTTTGCTC', 39, 47], ['GCGGG', 11, 16, 'CCCGC', 57, 62], ['TTTC', 6, 10,



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

        elif charA == "N" or charB =="N" or charC == "N":
            hamming = hamming + 0


        else:
            hamming = hamming + 1
        #print "hamming" + str(hamming)
        #print "s1" + str(s1)
        #print "s1rev" + str(s1rev)
        #print "s2" + str(s2)
    return hamming



def piece_maker(s, size): #working
    pieces =[]

    s = s# + s[0:biggest]
    length = len(s)
    j = 0  #beginning of piece
    end = length-1  #end of piece
    k=j+size
    while j<length-size:
        while k > j+size-2:
            piece = s[j:k+1]
            if piece.isalpha(): #for later when  sequences with dashes are run through
                pieces.append([piece, j, k+1]) # all the pieces with positional information #the positional tracking is off)
            k = k - 1
            #print k

        j = j + 1
        if j==length-size and j!=length:
            size = size -1
        k=j+size
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
        #print "TMP A" + str(tmptargetA)
        tmptargetB = [s[rightbound:targetB[2]+1], rightbound, targetB[2]+1]
        #print "TMP B" + str(tmptargetB)
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

def target_extend_inwards(target, s):  #This is where to deal with small (1-2bp each side) bulges
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
    #extend unbroken hairpin seeds that fall outside of the initial 32nt long segments(2 10nt matches+ 11nt max loop)
   #add on outer end until hamming threshold is reached
    #this will be a rare event
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

def closerange_target_extend2(target, s):
    tmptarget = target
    
    hamm = 0

    while hamm == 0:
        tmptarget = [s[target[1]-1:target[2]], target[1]-1, target[2], s[target[4]:target[5]+1], tmptarget[4], target[5]+1]
        hamm = rna_hamming(s[tmptarget[1]-1], s[tmptarget[5]]) 
        if hamm == 0:
            target= tmptarget
            
            
            
        else:
            return target
                         
    #print str(s[target[1]-1:target[2]]) + "  " + str(s[target[4]:target[5]+1])
    return tmptarget
    

def closerange_target_extend(target,s):
    if target[4]-target[2] == 4:
        return target
    tmptargetA = target[0:3]
    tmptargetB = target[3:6]
    leftbound = tmptargetA[2]
    rightbound = tmptargetB[1]
    hamm = 0
    extendA = 1
    
    #first try lef

    while hamm == 0:
        
        while extendA <3:
            
            newtmptargetA = [s[tmptargetA[1]-extendA]+extendA*"N"+tmptargetA[0], tmptargetA[1]-extendA, leftbound]
            newtmptargetB = [s[rightbound:tmptargetB[2]+2], rightbound, tmptargetB[2]+2]
            hamm = rna_hamming(newtmptargetA[0], newtmptargetB[0])
            if hamm!= 0:
                #return (tmptargetA + tmptargetB)
                extendA = extendA + 1
                break
            else:
               tmptarget = (newtmptargetA + newtmptargetB)
               #tmptarget = target_extend_outwards(tmptarget, s)
               print "this happened1"
               print tmptarget

               target = closerange_target_extend2(tmptarget, s)
               print "this happened2"
               print target
               #print str(s[target[1]-1:target[2]]) + "  " + str(s[target[4]:target[5]+1])
               return target
            
            #targetA=tmptargetA
            #targetB = tmptargetB
            #if targetA[1] == 0 or targetB[2] == len(s):
                #print "end targetA {0}, and targetB {1}".format(targetA, targetB)
    #return (targetA + targetB)

        #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (tmptargetA + tmptargetB)




def reduceloop(target, s):  #functional

    #consider a formed helix as a single nt long position
    #also reduces full length of s so that only regions local to the existing fold are considered
    #s_reduced = s[0:target[1]+1] + "-" + s[target[5]:len(s) + 1]
    new_s = s[target[1]-12:target[1]] + "-" + s[target[5]:target[5]+12]

    s_reduced = new_s
    #print s[target[1]-25:target[5]+25]
    #return s_reduced

def piece_inhelix(target, s, size, extend): #make pieces in local regions surrounding a previously formed helix.   
    
    lefthalf = []
    righthalf=[]
    pieces =[]
    maxlen = len(s)
    
    begin = target[1]-extend+1
    leftmiddle = target[1]
    rightmiddle = target[5]
    end = target[5]+extend +2

    if begin == leftmiddle:
        return pieces
    if rightmiddle + size >= end:
        return pieces
    if maxlen > end:
        maxlen = end
    
    
    
    length = leftmiddle-begin
    j = begin
    if j < 0 :
        j = 0
    
    
    print target
    

    while j <(leftmiddle-2):
        
        
        piece = s[j:j+size]
        if len(piece)<3:
            break
        else:
       
        #print piece
            lefthalf.append([piece, j, j+size]) 
        #print lefthalf
        j = j + 1

    
    j = rightmiddle
   
   
    while j<(end-size):

        piece = s[j:j+size]

        if len(piece)<3:
            break
        else:
        
            righthalf.append([piece, j, j+size]) 
        
        j = j + 1
        
        
    print target        
    pieces = [lefthalf] + [righthalf]
    print pieces
    return pieces


def piece_match2(pieces):
    targets =[]
    if pieces:
        lefthalf = pieces[0]
        righthalf = pieces [1]

    
        for left in lefthalf:
            for right in righthalf:
                if len(left[0]) ==len(right[0]):

                        if rna_hamming(left[0], right[0]) == 0:
                            target = (left + right)
                            target = target_extend_outwards(target, s)
                            target = target_extend_inwards(target, s)
                            targets.append(target)
                        

    return targets


def piece_match(pieces, s):
    targets =[]
    #print str(pieces)
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
                            #print "before extend " + str(target)
                            target = target_extend_inwards(target, s)
                            #print "after inwards " + str(target)
                            target = target_extend_outwards(target, s)
                            #print "after outwards " + str(target)
                            #target = closerange_target_extend(target, s)
                            
                            #print "after outwards " + str(target)
                            if not target in targets:
                                #print "after nondup " + str(targets) + "  "
                                targets.append(target)

    return targets





#hairpin loop size fine for now



#s1 = "AAATAAAGAAA"
#s2 = "TTTTTTTATTT"
s=seq_file
print len(s)
folds = defaultdict(list)

def controlpanel(s):
#print rna_hamming(s1,s2)

    pieces = piece_maker(s,3)
    arms = []
    #altarms = []
    #folddict1 = {}
    #folddict2 ={}
    #folddict3={}
    groupkey = 0
    seckey = 0
    trikey = 0
    groupdict= {}
    secdict={}
    tridict = {}


    
    redtargets = piece_match(pieces, s)
    print "reduced target list len: {0}".format(len(redtargets))
    for group in redtargets:
        #print group
        groupkey = groupkey + 1
        #group = target_extend_outwards2(group, s)
        
        #print reduceloop(group, s)
        #print "FIRST FOLD"
        #print group
        
        
        #inhelix_pieces = piece_inhelix(group, s, 3, 3)  #extension may be broken?
        #print inhelix_pieces
        inhelix_pieces = piece_inhelix(group, s, 3, 12)
        #inhelix_pieces.append(piece_inhelix(group, s, 3, 12))  #extension may be broken?
        #print inhelix_pieces
        if inhelix_pieces:
        
            sectargets = piece_match2(inhelix_pieces)
        #groupdict[groupkey] = group
        #altarms.append([groupkey])
        arms.append([group, 0, 0, 0, 0])
       

        
        for secgroup in sectargets:
            #seckey = seckey +1
            secgroup = target_extend_outwards2(secgroup, s)
            #print reduceloop(secgroup, s)
            #print "SECOND FOLD"
            #print secgroup
            inhelix_pieces = piece_inhelix(secgroup, s, 3, 12)
            #altarms.append([groupkey, seckey])
            arms.append([group, secgroup, 0, 0, 0])
##            #secdict[seckey] = secgroup
##            tritargets = piece_match2(inhelix_pieces)
##            
##            for trigroup in tritargets:
##                #trikey = trikey + 1
##                #altarms.append([groupkey, seckey, trikey])
##                arms.append([group, secgroup, trigroup, 0, 0])
##                #tridict[trikey] = trigroup
##                #print "THIRD FOLD"
##                #print thrgroup
##                inhelix_pieces = piece_inhelix(trigroup, s, 3, 12)
##                quadtargets = piece_match2(inhelix_pieces)
##                for quadgroup in quadtargets:
##                        arms.append([group, secgroup, trigroup, quadgroup, 0])
##                        inhelix_pieces = piece_inhelix(quadgroup, s, 3, 12)
##                        quinttargets = piece_match2(inhelix_pieces)
##                        for quintgroup in quinttargets:
##                            arms.append([group, secgroup, trigroup, quadgroup, quintgroup])
##                        
##               

    for arm in arms:
       #print "arm"
       print arm
    print len(arms)       
##            
        #print len(redtargets)  #only 82 target seed for the 16s 28 arms
            #need to get an accurate structure and sequence of a 16s
    print len(redtargets)


#s1 = "AAATAAAGAAA"
#s2 = "TTTTTTTATTT"
s=seq_file
s=s[420:510]
print len(s)
controlpanel(s)
#print "s[1490: 1540]" + str(s[1490:1540])
#print "s[79:90]" + str(s[79:90])
#print "s[149:160]" + str(s[149:160])
#print "s[249:260]" + str(s[249:260])
#print "s[1439:1460]" + str(s[1439:1460])

#AAATTGAAGAGTTTGATCATGGCTCAGATT
#AAAUUGAAGAGUUUGAUCAUGGCUCAGAUU

#next: build dictionary FF:SF:TF

#STRUCTURE INDEX = 1, PROGRAM INDEX = 0

#right half matches structure numbering
#left half matches structure numbering -1


