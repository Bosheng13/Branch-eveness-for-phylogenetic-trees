fi=open(r'F://test//Test-tree.txt','r', encoding='utf-8')    ####input the newick tree file and its pathway in user's device
fo=open(r'F://test//Whole--trimed-tree.txt','w', encoding='utf-8')  ###output of the intermediate file

i=0
for line in fi:
    lst_line=list(line)
    length=len(lst_line)
    
    for i in range(0,length):
        if i>=len(lst_line):
            break
        if lst_line[i]==":":
            k=i
            for k in range(i,length):
                #print(lst_line[k],"position=",k)
                if lst_line[k]=='(' or lst_line[k]==')' or lst_line[k]==',' or lst_line[k]==']':
                    #print(":start",i,"end:",k)
                    if lst_line[k]==']':
                        lst_line.pop(k)
                    for j in range(k-1,i-1,-1):
                        lst_line.pop(j)
                    break
                else:
                    continue
        else:
            continue

            
ss=''.join(lst_line) 
fo.write(ss+'\n')

fo.close()
fi.close()


fi2=open(r'F://test//Whole--trimed-tree.txt','r', encoding='utf-8')  
fo2=open(r'F://test//Whole----trimed-tree-final.txt','w', encoding='utf-8')  ##output of this script
i=0
pos1=0
pos2=0
label=[]
for line2 in fi2:
    lst_line2=line2.split(',')
    for i in range(0,len(lst_line2)):
        j=0
        k=0
        pos1=0
        pos2=0
        flag=0
        label=[]
        before=[]
        after=[]
        label2=[]
        final=[]
        for j in range(0,len(lst_line2[i])):
            if lst_line2[i][j] != '(' and flag==0:
                pos1=j+1
                flag=1
                continue
            if flag==1 and j==len(lst_line2[i])-1 and lst_line2[i][j] != ')':
                pos2=j
                print(pos2,j)
            if lst_line2[i][j] ==')' and flag==1:
                pos2=j-1
                break
            else:
                continue
        for k in range(pos1-1,pos2):
            label.append(lst_line2[i][k])
            #print(label)
            #print("??")
        for k in range(0,pos1-1):
            before.append(lst_line2[i][k])
        for k in range(pos2+1,len(lst_line2[i])):
            print(lst_line2[i])
            after.append(lst_line2[i][k])
        #label=list(label)
        label2=''.join(label)
        #print(label)
        #print("#######")
        #print(label2)
        if "evm.model.PGRX" in label2:   ###the original name of tree leaves belongs to different species ('evm.model.PGRX...' here refers leaves of Periplaneta americana. We renamed it as 'P')
            label="P"
        if "PSN" in label2:     
            label="B"
        if "evm.model.BLKM" in label2:
            label="C"
        if "Znev" in label2:
            label="Z"
        if "Cfor_Cluster" in label2:
            label="C"
        if "PNF" in label2:
            label="S"
        if "Psp_RS" in label2:
            label="R"
        if "Mnat" in label2:
            label="M"
        #before=''.join(before)
        print("*******")
        print(before)
        print(after)
        print(label)
        
        after=''.join(after)
        before.append(label)
        before.append(after)
        lst_line2[i]=''.join(before)
        print("label change finished", "i=",i,"label:",lst_line2[i])
        final=','.join(lst_line2)
        
                
            
fo2.write(final)                
        
        

        

fo2.close()
fi2.close()













