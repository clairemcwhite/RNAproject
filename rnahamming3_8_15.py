
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



def rna_hamming(s1,s2): #sequence 1, sequence 2
    #matches G's to T's/U's, A's to T's/U's, and G's to C's
    #A hamming distance function that returns the hamming distance of the match between two ssRNA sequences.
    #A hamming distance of 0 means a perfect match
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
    if target[4]-target[2] == 3:
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


  
    

def closerange_target_extend(target,s):
    print "enter closerange"
    print "target: {0}".format(target)

    if target[1] <= 4:  
        return target
    if target[5] >=len(s)-2:
        return target

    
    tmptargetA = target[0:3]
    tmptargetB = target[3:6]
    leftbound = tmptargetA[2]
    rightbound = tmptargetB[1]
    hamm = 0

    count = 1
    testcycles = 0
    extension_order = [[0, 1], [1, 0], [1, 1],  [1, 2], [2, 1], [0,2], [2, 0],[2, 2]]  #02, 20 come after 12, 21
    

    #extensionA= ""
    #extensionB= ""

    #testing offsets
    while testcycles <8:
        
        hamm = 0
        extensionA= ""
        extensionB= ""
        extend = 1
        extendAseed = extension_order[testcycles][0]
        extendBseed = extension_order[testcycles][1]
        
        
        #extensionA =  s[tmptargetA[1]-extendAseed-1:tmptargetA[1]]
        #extensionB = s[tmptargetB[2] +1:tmptargetB[2]+extendBseed+1]
        #print extensionA
        #print extensionB
        count = 0
        print "enterhamming loop"
        print extension_order[testcycles]
        while hamm == 0:
                
                newtarget = [s[tmptargetA[1]-len(extensionA): leftbound], tmptargetA[1]-extendAseed -len(extensionA), leftbound, s[rightbound: tmptargetB[2]+ len(extensionB)], rightbound,tmptargetB[2]+extendBseed+ len(extensionB) -1]
                
                print "running..." + str(count)
                extensionA =  s[tmptargetA[1]-extendAseed-extend:tmptargetA[1]]
                extensionB = s[tmptargetB[2]:tmptargetB[2]+extendBseed+extend]
                 
                #something is off with checking for matches...figure out next
                hamm = hamm + rna_hamming(extensionA[0:1], extensionB[-1])
                print "this went to hamm, extensionAbegin : {0}, extensionBend: {1}".format(extensionA[0:1], extensionB[-1])
                
                
                print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}".format(tmptargetA, tmptargetB, extensionA, extensionB)  

                extend = extend + 1

                count = count + 1
                
                    
        if count<2:  #the new indexing is off  newtarget. 2, 4 = bad
 

            testcycles = testcycles + 1
        elif count>1:
            #newtarget = [s[tmptargetA[1]-extendAseed -len(extensionA): leftbound], tmptargetA[1]-extendAseed -len(extensionA), leftbound, s[rightbound: tmptargetB[2]+extendBseed+ len(extensionB)], rightbound,tmptargetB[2]+extendBseed+ len(extensionB) ]  
            print extension_order[testcycles]
            #print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}, {4}".format(tmptargetA, tmptargetB, extensionA, extensionB, testcycles)
            print "about to be returned : {0}".format(newtarget)
            return newtarget

    
    return target            
              
            
        
    #return (tmptargetA + tmptargetB)




##def reduceloop(target, s):  #functional
##
##    #consider a formed helix as a single nt long position
##    #also reduces full length of s so that only regions local to the existing fold are considered
##    #s_reduced = s[0:target[1]+1] + "-" + s[target[5]:len(s) + 1]
##    new_s = s[target[1]-12:target[1]] + "-" + s[target[5]:target[5]+12]
##
##    s_reduced = new_s
##    #print s[target[1]-25:target[5]+25]
##    #return s_reduced

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
   
    while j <(leftmiddle-2):
        
        piece = s[j:j+size]
        if len(piece)<3:
            break
        else:

            lefthalf.append([piece, j, j+size]) 
        
        j = j + 1

    j = rightmiddle

    while j<(end-size):

        piece = s[j:j+size]

        if len(piece)<3:
            break
        else:
        
            righthalf.append([piece, j, j+size]) 
        
        j = j + 1
   
    #print target        
    pieces = [lefthalf] + [righthalf]
    #print pieces
    return pieces

def exclude_match(targets):

    mindistance = 100
    target = []
    for candidate in targets:
        current_distance = candidate[2]-candidate[4]
        if current_distance < mindistance:
            mindistance = current_distance

            target = [candidate]
    return target
    


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
        target = exclude_match(targets)
                        

    return target


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
                            
                            
                            #print "after outwards " + str(target)
                            if not target in targets:
                                print "closetarget round 1 for {0}".format(target)
                                close_target = closerange_target_extend(target, s)
                                print "close_target after round 1: {0}".format(close_target)
                                print "closetarget round 2 for {0}".format(close_target)
                                close_target2 = closerange_target_extend(close_target, s)
                                print "target after round 2: {0}".format(close_target2)
                                print "\n"
                                #print "after nondup " + str(targets) + "  "
                                targets.append(target)
                                targets.append(close_target)
                                targets.append(close_target2)

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
        print group
        groupkey = groupkey + 1
        #group = target_extend_outwards2(group, s)
        
        #print reduceloop(group, s)
        #print "FIRST FOLD"
        #print group
        
        
        #inhelix_pieces = piece_inhelix(group, s, 3, 3)  #extension may be broken?
        #print inhelix_pieces
        #inhelix_pieces = piece_inhelix(group, s, 3, 12)
        #inhelix_pieces.append(piece_inhelix(group, s, 3, 12))  #extension may be broken?
        #print inhelix_pieces
        #if inhelix_pieces:
        #
        #    sectargets = piece_match2(inhelix_pieces)
        #groupdict[groupkey] = group
        #altarms.append([groupkey])
        #print group
        arms.append([group, 0, 0, 0, 0])
       
##
##        
##        for secgroup in sectargets:
##            #seckey = seckey +1
##            secgroup = target_extend_outwards2(secgroup, s)
##            #print reduceloop(secgroup, s)
##            #print "SECOND FOLD"
##            #print secgroup
##            inhelix_pieces = piece_inhelix(secgroup, s, 3, 12)
##            #altarms.append([groupkey, seckey])
##            arms.append([group, secgroup, 0, 0, 0])
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
       print arm
       #print arm
   # print len(arms)       
##            
        #print len(redtargets)  #only 82 target seed for the 16s 28 arms
            #need to get an accurate structure and sequence of a 16s
    #print len(redtargets)


#s1 = "AAATAAAGAAA"
#s2 = "TTTTTTTATTT"
s=seq_file
s=s[60:110]
print s[25:37]
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

print s[15:23] +" " + s[25:33] + "[['GAAGAAGC', 15, 23, 'GCTTCTTT', 25, 33], 0, 0, 0, 0]"
print s[12:23] +" " +  s[25:38] + "[['CAGGAAGAAGC', 12, 23, ''GCTTCTTTGCTG', 25, 38]], 0, 0, 0, 0]"
#print s[6:23] +" " +  s[25:38] + "[['GTAACAGGAAGAAGC', 6, 23, 'GCTTCTTTGCTGA', 25, 38], 0, 0, 0, 0]"

