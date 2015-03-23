#so far is making groups of nearest neighbor threes.

#search in the sequence itself for distance extenders.
#then fill that in with a selection of arms
#look more into the criteria for having a three arm.

#Should be able to cut many two threes after they don't lead to immediate extensions. Must be bounded by extension or lead directly into and extension.
#single arms don't need to be bounded by extension.  
#Can start messing with this once make_arms has given 100% accurate list.
#search for long 2o extensions which include no mismatches and up to insert per side.  enforce {00, 10, 01} extension order

#in the same way that hairpin size defines what can be a hairpin region and guides make_arms.py,
#   long internal loopless matches guid the construction of the full 2o structure
#As the long internal matches are  used by the RNA to choose correct arms form the search space, a long internal match overrules arms which overlap it



def listify(arms):
    newarms=[]

    for arm in arms:
        newarm = eval(arm)
        newarms.append(newarm)  
    return newarms

def piece_maker(s, size): #used to fragment sequence  #Make 4 long min pieces?  Use long pieces to look for matches first.  Extend and try to build off 3bps and #Make file over in arm_maker and just read off of that.  
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
    #print pieces
    return pieces

def piece_match2(pieces):
    targets =[]
    #print pieces
    if pieces

    
        for piece1 in pieces:
            for piece2 in pieces:
               
                if rna_hamming(piece1[0], piece2[0]) == 0:
                    if piece2[1]-piece1[2]>25:
                        target = piece1 + piece2
                        print target
                        print "extend out"
                        target = target_extend_outwards(target, s) #allowing 1 bp (non C) mismatch
                        #pair matching is off.  Need to redo architecture to add on one base at a time,...
                        target = target_extend_inwards(target, s)
                        print target
                        targets.append(target)
            
                        

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

        elif charA == "-" or charB =="-" or charC == "-":
            hamming = hamming + 0

        else:
            hamming = hamming + 1
    return hamming

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

    count_gapA = 0
    count_gapB = 0
    
    hamm = 0
    while hamm == 0:
        tmptargetA = [s[targetA[1]-1:leftbound], targetA[1]-1, leftbound]
        #print "TMP A" + str(tmptargetA)
        tmptargetB = [s[rightbound:targetB[2]+1], rightbound, targetB[2]+1]
        #print "TMP B" + str(tmptargetB)
        hamm = rna_hamming(tmptargetA[0][0:1], tmptargetB[0][-1])  #just take hamming of the added on characters)
        if hamm!= 0:
            hamm = 0
            tmptargetA = [s[targetA[1]-2:leftbound], targetA[1]-2, leftbound]
            #print "TMP A" + str(tmptargetA)
            tmptargetB = [s[rightbound:targetB[2]+1], rightbound, targetB[2]+1]
            #print "TMP B" + str(tmptargetB)
            hamm = rna_hamming(tmptargetA[0][0:1], tmptargetB[0][-1])
            
            if hamm == 0:
                count_gapA =1
                targetA = tmptargetA
                targetB = tmptargetB
                else:
                    hamm = 0
                    tmptargetA = [s[targetA[1]-1:leftbound], targetA[1]-1, leftbound]
                    #print "TMP A" + str(tmptargetA)
                    tmptargetB = [s[rightbound:targetB[2]+2], rightbound, targetB[2]+2]
                    #print "TMP B" + str(tmptargetB)
                    hamm = rna_hamming(tmptargetA[0][0:1], tmptargetB[0][-1])
                    if hamm == 0:
                        targetA = tmptargetA
                        targetB = tmptargetB
                    else:
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
    if target[4]-target[2] < 28:  # this is never happening   
        print "target already less than 28"
        return target
    targetA = target[0:3]
    targetB = target[3:6]
    leftbound = targetA[1]
    rightbound = targetB[2]
    hamm = 0
    while hamm==0 and (targetB[1] - targetA[2]) > 28:
        tmptargetA = [s[leftbound:targetA[2]+1], leftbound, targetA[2]+1]
        tmptargetB = [s[targetB[1]-1:rightbound], targetB[1]-1, rightbound]

        hamm = rna_hamming(tmptargetA[0], tmptargetB[0])
        if hamm!=0# or (tmptargetB[1] - tmptargetA[2]) < 28:
            hamm = 0
            tmptargetA = [s[targetA[1]+2:leftbound], targetA[1]+2, leftbound]
            #print "TMP A" + str(tmptargetA)
            tmptargetB = [s[rightbound:targetB[2]-1], rightbound, targetB[2]-1]
            #print "TMP B" + str(tmptargetB)
            hamm = rna_hamming(tmptargetA[0][-1], tmptargetB[0][0:1])
            if hamm == 0:
                targetA = tmptargetA
                targetB = tmptargetB
                else:
                    hamm = 0
                    tmptargetA = [s[targetA[1]+1:leftbound], targetA[1]+1, leftbound]
                    #print "TMP A" + str(tmptargetA)
                    tmptargetB = [s[rightbound:targetB[2]-2], rightbound, targetB[2]-2]
                    #print "TMP B" + str(tmptargetB)
                    hamm = rna_hamming(tmptargetA[0][-1], tmptargetB[0][0:1])
                    if hamm == 0:
                        targetA = tmptargetA
                        targetB = tmptargetB
                    else:
                        return (targetA + targetB)
      
        else:
            targetA=tmptargetA
            targetB = tmptargetB

    #print "end targeta {0}, and targetB {1}".format(targetA, targetB)
    return (targetA + targetB )


def seedmake(arms, s):
#Makes groups of 1, 2, and 3 to search for a geographic end
##
    seeds = []
    for arm1 in arms:
        seeds.append(arm1)
        
        prev = ''
        count = 1
        for arm2 in arms:
            if (arm2[1]-arm1[5])>0 and (arm2[1]-arm1[5])< 8:
                if count > 1 and arm2[1] == prev:
                   
##                    print "2o extension2"
##                    print arm1
##                    print arm2
                    seed = [s[arm1[1]:arm2[5]], arm1[1], arm2[5]]
##                    print seed
                    seeds.append(seed)
##                    print '\n'
                elif count == 1:
##                    print arm1
##                    print arm2
                    seed = [s[arm1[1]:arm2[5]], arm1[1], arm2[5]]
##                    print seed
                    seeds.append(seed)
                    prev = arm2[1]
                    count = count + 1
##                    print '\n'
                count2 = 1
                prev2 = ''
                if len(arm1[0])>8:
                
                    for arm3 in arms:
                        if len(arm3[0]) >8:
                          
                           if (arm3[1]-seed[2])>0 and (arm3[1]-seed[2])< 8:
                                #print "is this happening"
                                if count2 > 1 and arm3[1] == prev2:
                                   
    ##                                print "2o extension3"
    ##                                print seed
    ##                                print arm3
                                    seed = [s[seed[1]:arm3[5]], seed[1], arm3[5]]
    ##                                print seed
                                    seeds.append(seed)
    ##                                print '\n'
                                elif count2 == 1:
##                                    print "2o extension3"
##                                    print seed
##                                    print arm3
                                    seed = [s[seed[1]:arm3[5]], seed[1], arm3[5]]
                                    #print seed
                                    seeds.append(seed)
                                    
                                    prev2 = arm3[1]
                                    count2 = count2 + 1
    ##                                print '\n'
    return seeds
                    
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
                    dashedA =   str(newtarget[0][0:count-1])+(extendAseed)*'-'+ str(target[6])
                    dashedB =   str(target[7])+extendBseed*'-'+ str(newtarget[3][-(count-1):])
                    newtarget.append(dashedA)
                    newtarget.append(dashedB)
                    #print dashedA
                    #print dashedB
                    #print newtarget
                    #print '\n'
                    return newtarget
                else:
                    testcycles = testcycles + 1
        elif extension_order[testcycles] in setthatneeds5:
                if count>5: 
                    #print "found one in set that needs 5"
                    #print "about to be returned : {0}".format(newtarget)
                    dashedA =   str(newtarget[0][0:count-1])+(extendAseed)*'-'+ str(target[6])
                    dashedB =   str(target[7])+extendBseed*'-'+ str(newtarget[3][-(count-1):])
                    newtarget.append(dashedA)
                    newtarget.append(dashedB)
                    #print dashedA
                    #print dashedB
                    #print newtarget
                    #print '\n'
                    return newtarget
                else:
                    testcycles = testcycles + 1
            
            
            
        elif not extension_order[testcycles] in setthatneeds4:
            if count>2:  
                #newtarget = [s[tmptargetA[1]-extendAseed -len(extensionA): leftbound], tmptargetA[1]-extendAseed -len(extensionA), leftbound, s[rightbound: tmptargetB[2]+extendBseed+ len(extensionB)], rightbound,tmptargetB[2]+extendBseed+ len(extensionB) ]  
                #print extension_order[testcycles]
                #print "targetA, target B, extensionA, extentionB: {0}, {1}, {2}, {3}, {4}".format(tmptargetA, tmptargetB, extensionA, extensionB, testcycles)
                #print "about to be returned : {0}, not in setthatneeds4".format(newtarget)
                dashedA =   str(newtarget[0][0:count-1])+(extendAseed)*'-'+ str(target[6])
                dashedB =   str(target[7])+extendBseed*'-'+ str(newtarget[3][-(count-1):])
                newtarget.append(dashedA)
                newtarget.append(dashedB)
                #print dashedA
                #print dashedB
                #print newtarget
                #print '\n'
                return newtarget

    
    return target            
              
            
                       
def controlpanel:            

    s_file = "ecoli_16s.txt"
    seq=open(s_file, 'r')
    s = seq.read().strip()
    seq.close()
    #s = [line.strip() for line in open(s_file, 'r')]
                
     
            
    a = "arms.txt"

    arms = [line.strip() for line in open(a, 'r')]

    arms = listify(arms)
    seeds = seedmake(arms, s)
    #for seed in seeds:
       # print seed

    print len(seeds)

    piece_maker(s,12)
    


controlpanel()

