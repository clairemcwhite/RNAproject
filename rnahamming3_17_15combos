
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
    #it's not making pieces in the right places
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
   
    while j <(leftmiddle-3):
        
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
def target_extend_outwards2(target, s): # not used ever... get rid of?
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


def exclude_match(targets):

    mindistance = 100
    target = []
    for candidate in targets:
        current_distance = candidate[4]-candidate[2]
        if current_distance < mindistance:
            mindistance = current_distance

            target = [candidate]
    return target
    


def piece_match2(pieces):
    targets =[]
    print pieces
    if pieces:
        lefthalf = pieces[0]
        righthalf = pieces [1]

    
        for left in lefthalf:
            for right in righthalf:
                if len(left[0]) ==len(right[0]):

                        if rna_hamming(left[0], right[0]) == 0:
                            target = left + right
                            print target
                            print "extend out"
                            target = target_extend_outwards(target, s)  #FIX HERE#it's not extending far enough?
                            #pair matching is off.  Need to redo architecture to add on one base at a time,...
                            
                            print target
                            targets.append(target)
        target = exclude_match(targets)
                        

    return target



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

def seed_make(pieces, s): # working completely
    targets =[]
    #print str(pieces)
    pieces_copy = pieces
    for piece in pieces:
        for piece_copy in pieces_copy:
            if piece[2] < piece_copy[1] and 4<(piece_copy[1]-piece[2])<17:

                #if piece[1] > seqlength:
                #    piece[1] = piece[1]-seqlength

                if len(piece[0]) ==len(piece_copy[0]):

                    if rna_hamming(piece[0], piece_copy[0]) == 0:

                        range1=set(range(piece[1],piece[2]))
                        range2=set(range(piece_copy[1], piece_copy[2]))
                        if not range1.intersection(range2):
                            target = piece + piece_copy  #the zero is the gap penalty
                            
                            #print "target: {0}".format(target)
                            #print "before extend " + str(target)
                            target = target_extend_inwards(target, s)
                            #print "after inwards " + str(target)
                            target = target_extend_outwards(target, s)
                            #print "after outwards " + str(target)
                            
                            
                            #print "after outwards " + str(target)
                            if not target in targets:
                                #print "closetarget round 1 for {0}".format(target)
                                #close_target = closerange_target_extend(target, s)
                                #print "close_target after round 1: {0}".format(close_target)
                                #print "closetarget round 2 for {0}".format(close_target)
                                
                                #print "target after round 2: {0}".format(close_target2)

                                
                                #print "target after round 3: {0}".format(close_target3)
                                
                                #print "target after round 3: {0}".format(close_target4)

                                #print "\n"
                                #print "after nondup " + str(targets) + "  "
                                targets.append(target)
#                                close_target = closerange_target_extend(target, s)
##                                if not close_target in targets:
##                                    targets.append(close_target)
##                                    close_target2 = closerange_target_extend(close_target, s)
##                                    if not close_target2 in targets:
##                                        targets.append(close_target2)
##                                        close_target3 = closerange_target_extend(close_target2, s)
##                                        if not close_target3 in targets:
##                                                targets.append(close_target3)
##                                                close_target4 = closerange_target_extend(close_target3, s)
##                                                if not close_target4 in targets:
##                                                    targets.append(close_target4)

    return targets

def piece_maker(s, size): #working # not to be used in this version
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

def target_extend_outwards(target, s): # used just for the initial seed
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

def target_extend_inwards(target, s):  
    #add on internally until hamming threshold is reached
    if target[4]-target[2] < 4:  # this is never happening   
        print "target already less than 4"
        return target
    targetA = target[0:3]
    targetB = target[3:6]
    leftbound = targetA[1]
    rightbound = targetB[2]
    hamm = 0
    while hamm==0 and (targetB[1] - targetA[2]) > 4:
        tmptargetA = [s[leftbound:targetA[2]+1], leftbound, targetA[2]+1]
        tmptargetB = [s[targetB[1]-1:rightbound], targetB[1]-1, rightbound]

        hamm = rna_hamming(tmptargetA[0], tmptargetB[0])
        if hamm!=0 or (tmptargetB[1] - tmptargetA[2]) < 4:
            return (targetA + targetB)
      
        else:
            targetA=tmptargetA
            targetB = tmptargetB

    #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (targetA + targetB )




def closerange_target_extend(target,s, order):  #index tracking is off on both sides, but offsets are working.  
    #print "enter closerange"
    #print "target: {0}".format(target)

    if target[1] <= 4:  
        return target
    if target[5] >=len(s)-2:
        return target
    #gap = target[6]
    
    tmptargetA = target[0:3]
    tmptargetB = target[3:6]
    leftbound = tmptargetA[2]
    rightbound = tmptargetB[1]
    hamm = 0

    count = 1
    testcycles = 0
    #extension_order = [[0, 1], [1, 0], [1, 1],  [1, 2], [2, 1], [0,2], [2, 0],[2, 2]]  #02, 20 come after 12, 21
    if order == "long":
        extension_order = ['00', '10', '01', '11', '02', '20', '22', '03', '30', '04', '40', '05', '50', '06', '60', '21', '12','31', '13', '23', '32', '33', '42', '24', '43', '34', '44', '52', '25', '53', '35', '54', '45', '55', '63', '36', '64', '46', '65', '56', '66', '74', '47', '75', '57', '76', '67', '77', '87', '78', '88', '89', '98', '99']
        setthatneeds4  = ['03', '30']
        setthatneeds5 = ['04', '40', '05', '50', '06', '60']
    if order == "short":
        extension_order = ['00', '10', '01', '11', '21', '12', '02', '20', '22', '03', '30', '31', '13', '23', '32', '33', '42', '24','04', '40', '42', '24', '43', '34', '44', '52', '25', '53', '35', '05', '50', '06', '60', '54', '45', '55', '63', '36', '64', '46', '65', '56', '66', '74', '47', '75', '57', '76', '67', '77', '87', '78', '88', '89', '98', '99']
        setthatneeds4  = ['03', '30']
        setthatneeds5 = ['04', '40', '05', '50', '06', '60']
        
    
    #program number for count to be over to bridge gaps

    while testcycles <len(extension_order):
        #print "testcycles: {0}".format(testcycles)
        
        
        hamm = 0
        extensionA= "placeholder"
        extensionB= "placeholder"
        extend = 1
        extendAseed = int(extension_order[testcycles][:1])
        extendBseed = int(extension_order[testcycles][-1])
    
     
        count = 0
        ##print "enterhamming loop"
        #print extension_order[testcycles]
        while hamm == 0 and extensionA:
                #current_gap = gap + max(extension_order[testcycles][0], extension_order[testcycles][1])
                
                newtarget = [s[tmptargetA[1]-len(extensionA): leftbound], tmptargetA[1]-len(extensionA), leftbound, s[rightbound: tmptargetB[2]+ len(extensionB)], rightbound,tmptargetB[2]+len(extensionB)]
                
                #print "running..." + str(count)
                extensionA =  s[tmptargetA[1]-extendAseed-extend:tmptargetA[1]]
                extensionB = s[tmptargetB[2]:tmptargetB[2]+extendBseed+extend]
                 
          
                hamm = hamm + rna_hamming(extensionA[0:1], extensionB[-1])
                #print "this went to hamm, extensionAbegin : {0}, extensionBend: {1}".format(extensionA[0:1], extensionB[-1])

                
                
                #print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}".format(tmptargetA, tmptargetB, extensionA, extensionB)  

                extend = extend + 1


                count = count + 1
                #print count
                #print testcycles
                
                    
        if count<3:  

            testcycles = testcycles + 1
        elif extension_order[testcycles] in setthatneeds4:
                if count>4: 
                    #print "found one in set that needs 4"
                    #print "about to be returned : {0}".format(newtarget)
                    return newtarget
                else:
                    testcycles = testcycles + 1
        elif extension_order[testcycles] in setthatneeds5:
                if count>5: 
                    #print "found one in set that needs 5"
                    #print "about to be returned : {0}".format(newtarget)
                    return newtarget
                else:
                    testcycles = testcycles + 1
            
            
            
        elif not extension_order[testcycles] in setthatneeds4:
            if count>2:  
                #newtarget = [s[tmptargetA[1]-extendAseed -len(extensionA): leftbound], tmptargetA[1]-extendAseed -len(extensionA), leftbound, s[rightbound: tmptargetB[2]+extendBseed+ len(extensionB)], rightbound,tmptargetB[2]+extendBseed+ len(extensionB) ]  
                #print extension_order[testcycles]
                #print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}, {4}".format(tmptargetA, tmptargetB, extensionA, extensionB, testcycles)
                #print "about to be returned : {0}, not in setthatneeds4".format(newtarget)
                return newtarget

    
    return target            
              
            
        
    #return (tmptargetA + tmptargetB)

def end_arm_extension(target, s):
        #print "enter closerange"
    #print "target: {0}".format(target)

    if target[1] <= 4:  
        return target
    if target[5] >=len(s)-2:
        return target
    #gap = target[6]
    
    tmptargetA = target[0:3]
    tmptargetB = target[3:6]
    leftbound = tmptargetA[2]
    rightbound = tmptargetB[1]
    hamm = 0

    count = 1
    testcycles = 0
    
    extension_order = ['11']

    while testcycles <len(extension_order):
        #print "testcycles: {0}".format(testcycles)
        
        
        hamm = 0
        extensionA= "placeholder"
        extensionB= "placeholder"
        extend = 1
        extendAseed = int(extension_order[testcycles][:1])
        extendBseed = int(extension_order[testcycles][-1])
    
     
        count = 0
        ##print "enterhamming loop"
        #print extension_order[testcycles]
        while hamm == 0 and extensionA:
                #current_gap = gap + max(extension_order[testcycles][0], extension_order[testcycles][1])
                
                newtarget = [s[tmptargetA[1]-len(extensionA): leftbound], tmptargetA[1]-len(extensionA), leftbound, s[rightbound: tmptargetB[2]+ len(extensionB)], rightbound,tmptargetB[2]+len(extensionB)]
                
                #print "running..." + str(count)
                extensionA =  s[tmptargetA[1]-extendAseed-extend:tmptargetA[1]]
                extensionB = s[tmptargetB[2]:tmptargetB[2]+extendBseed+extend]
                 
          
                hamm = hamm + rna_hamming(extensionA[0:1], extensionB[-1])
                #print "this went to hamm, extensionAbegin : {0}, extensionBend: {1}".format(extensionA[0:1], extensionB[-1])

                
                
                #print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}".format(tmptargetA, tmptargetB, extensionA, extensionB)  

                extend = extend + 1


                count = count + 1
                #print count
                #print testcycles
                
                    
       
        if count>1: 
            #print "found one in set that needs 4"
            #print "about to be returned : {0}".format(newtarget)
            return newtarget
        else:
            testcycles = testcycles + 1

    
    return target            



#s1 = "AAATAAAGAAA"
#s2 = "TTTTTTTATTT"
s=seq_file
print len(s)
folds = defaultdict(list)

def controlpanel(s):
#print rna_hamming(s1,s2)

    pieces = piece_maker(s,2)
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
    #inhelix_pieces =[]
    targets = []
    
    seeds = seed_make(pieces, s)
    print "reduced seed list len: {0}".format(len(seeds))
    
    for seed in seeds:
        close_target = closerange_target_extend(seed, s, "short")
        extra = end_arm_extension(close_target, s)
        if not extra in targets:
            targets.append(extra)
        count = 0
        #print "round short"
        while count < 4:

            close_target = closerange_target_extend(close_target, s, "short")
            if not close_target in targets:
                targets.append(close_target)
                extra = end_arm_extension(close_target, s)
                if not extra in targets:
                    targets.append(extra)
            count = count + 1
        close_target = closerange_target_extend(seed, s, "long")
        count = 0
        #print "round long"  #made for finding 502ish-546 arm
        while count < 4:

            close_target = closerange_target_extend(close_target, s, "long")
            if not close_target in targets:
                targets.append(close_target)
                extra = end_arm_extension(close_target, s)
                if not extra in targets:
                    targets.append(extra)
            count = count + 1
       
                
##                close_target2 = closerange_target_extend(close_target, s)
##                if not close_target2 in targets:
##                    targets.append(close_target2)
##                    close_target3 = closerange_target_extend(close_target2, s)
##                    if not close_target3 in targets:
##                            targets.append(close_target3)
##                            close_target4 = closerange_target_extend(close_target3, s)
##                            if not close_target4 in targets:
##                                targets.append(close_target4)
        arms.append(seed)
        for target in targets:
            arms.append(target)
        targets = []
    
            
        #print group
        #seedkey = seedkey + 1
        #group = target_extend_outwards2(group, s)
        
        #print reduceloop(group, s)
        #print "FIRST FOLD"
        #print group
        
        
        
        #print inhelix_pieces
        #inhelix_pieces = piece_inhelix(group, s, 4, 15)
        #inhelix_pieces.append(piece_inhelix(group, s, 3, 12))  #extension may be broken?
        #print inhelix_pieces
        #if inhelix_pieces:
        
            #sectargets = piece_match2(inhelix_pieces)
        #groupdict[groupkey] = group
        #altarms.append([groupkey])
        #print group
        
        #arms.append([seed, 0, 0])
        
       

        
        #for secgroup in sectargets:
            #seckey = seckey +1
            #secgroup = target_extend_outwards2(secgroup, s)
            #print reduceloop(secgroup, s)
            #print "SECOND FOLD"
            #print secgroup
##            inhelix_pieces = piece_inhelix(secgroup, s, 3, 12)
##            #altarms.append([groupkey, seckey])
##            arms.append([group, secgroup, 0])
##            #secdict[seckey] = secgroup
##            tritargets = piece_match2(inhelix_pieces)
##            
##            for trigroup in tritargets:
##                #trikey = trikey + 1
##                #altarms.append([groupkey, seckey, trikey])
##                arms.append([group, secgroup, trigroup])
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
s=s[403:554]
#s=s[495:550]
#print s[25:37]
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

#Program architecture rewrite:
#extend in a pattern.  10 01 11 21 12 02 20 22 03 30 31 13 23 32 33 42 24 43 34 44 52 25 53 35 54 45 55  63 36 64 46 65 56 66 74 47 75 57 76 67 77 87 78 88 89 98 99
#as you get higher , you need a longer bridge at the end
# for 1 1 just need a 1 brdige
# for up to 2, need 2 bridge, not AT TA
#for three  just need 2 bridge
# for 5 even, just need a 2 bridge

#determine rules for necessaary bridges.
