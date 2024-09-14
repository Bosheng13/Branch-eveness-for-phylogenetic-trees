fi=open(r'F://test//Whole----trimed-tree-final.txt','r', encoding='utf-8')   #####output of the script 'rearrange-tree.py'
fo=open(r'F://test//whole-out_evolution_tree.txt','w', encoding='utf-8')  #####intermdeiate file

import math
import copy
import numpy as np
import re
op=[]
cp=[]
lbl=[]
i=0



for line in fi:
    for i in range(0,len(line)-1):
        #print(i,"open parenthesis")
        if line[i]=="(":
            op.append(line[i])
        else:
            op.append('NULL')         
    i=0
    for i in range(0,len(line)-1):
        #print(i,"closed parenthesis")
        if line[i]==")":
            cp.append(line[i])
        else:
            cp.append('NULL')     
    i=0
    #print(lbl)
    for i in range(0,len(line)-1):
        #print(i,"label")
        if line[i] !=")" and line[i] !="(" and line[i] !="," and line[i]!= ";":
            lbl.append(line[i])
        else:
            continue
    i=0
#print("#####&&&&&&",lbl)


sto=[]
newtree=[]
newtree=list(line)

sto=copy.copy(lbl)  #####must use copy(), otherwise lbl will change with sto
sto=np.unique(sto)
sto=list(sto)
#print("###$$$$",sto)
x=0
for i in range(0,len(sto)):
    x=0
    #print("this is lbl")
    for j in range(0,len(newtree)):
        if sto[i]==newtree[j]:
            #print("find",i,j)
            #print(sto[i],newtree[j])
            x=x+1
            #print(newtree)
            newtree[j]=sto[i]+str(x)
            #print("$$$$",newtree)
            #print(x)
        else:
            continue
newlbl=[]
for i in range(0,len(newtree)):
    if newtree[i] !=")" and newtree[i] !="(" and newtree[i] !="," and newtree[i]!= ";":
        newlbl.append(newtree[i])
    else:
        continue
lbl=newlbl




#lbl=sto
#newtree=''.join(newtree)
sto=[]



op=[]
cp=[]
lbl=[]

for i in range(0,len(newtree)):
    #print(i,"open parenthesis")
    if newtree[i]=="(":
        op.append(newtree[i])
    else:
        op.append('NULL')         
i=0
for i in range(0,len(newtree)):
    #print(i,"closed parenthesis")
    if newtree[i]==")":
        cp.append(newtree[i])
    else:
        cp.append('NULL')     
i=0
for i in range(0,len(newtree)):
        #print(i,"label")
    if newtree[i] !=")" and newtree[i] !="(" and newtree[i] !="," and newtree[i]!= ";":
        lbl.append(newtree[i])
    else:
        continue
i=0
print("#####&&&&&&",lbl)






####find leaves
op1=[]
cp1=[]
i=0
j=0
x=0
for i in range(0,len(line)-1):
        j=0
        flag=0
        if cp[i]==")":
            flag=0
            cp1.append(i)
            #print("cp1=",cp1)
            for j in range(i,-1,-1):
                #print(j)
                if op[j]=="(":
                    #print("########find###############")
                    op1.append(j)
                    #print("op1=",op1)   ####op1 contain the position of open parenthesis, cp1 contain the position of close parenthesis
                    flag=1
                    break
                else:
                    continue
            if flag==1:
                cp[i]="NULL"
                op[j]="NULL"
            else:
                #print("error","cpi=",i,"opj=",j)
                break
            flag=0
        else:
            continue

#####根据已有的位置找出进化树内容
lencp1=len(cp1)
lenop1=len(op1)
tree=[]
i=0
j=0
if lencp1 != lenop1:
        print("error, cp1 length not equal with op1")
else:
    for i in range(0,lencp1):
        for j in range(op1[i],cp1[i]+1):
            tree.append(newtree[j])
        tree.append('\n')
        j=0        
            
tree=''.join(tree)
fo.write(tree)
fo.close()
fi.close()

print("tree output finished")

fi2=open(r'F://test//whole-out_evolution_tree.txt','r', encoding='utf-8')
fo2=open(r'F://test//Whole--final_list.txt','w', encoding='utf-8')           ##final output    
i=0
j=0
k=0
l=0
n=0
o=0
output=[]
m=0
sto=[]
sto1=[]
sto2=[]

def remove_digits(string):
    result=re.sub(r'\d','',string)
    return result

output.append("Leaves")
output.append("\t")
for m in range(0,len(lbl)-1):
    output.append(m+1)
    output.append("\t")
output.append("\n")
for i in range (0,len(lbl)-1):
    shannon_list=[]
    branch_list=[]
    str3=[]
    for line1 in fi2:
        strr=[]
        str1=[]
        str2=[]
        count=0
        uniq_count=0
        shannon=0
        g=0
        fg=0

        strr=line1
        shannon=0
        strr=strr.replace('(','')
        strr=strr.replace(')','')
        str2=strr.split(',')
        strr=strr.replace(',','')
        strr=strr.replace('\n','')
        str2[-1]=str2[-1].replace('\n','')
        strr=remove_digits(strr)
        if str3=='':
            str3=[]
        else:
            if str2==str3:
                break
            else:
                str2=str2
        str3=str2
        str1=list(set(strr))
        uniq_count=len(str1)
        for g in range(0,len(str2)):
            if lbl[i]==str2[g]:
                fg=1
                break
            else:
                continue
          
        shannon_res=[]
        if fg==1:
            #print("strr=",strr)
            #print("str2",str2)
            j=0
            k=0
            l=0  
            for j in range(0,len(str1)):
                fct_num=0
                Pi=0
                for k in range(0,len(strr)):
                    if str1[j]==strr[k]:
                        fct_num=fct_num+1
                    else:
                        continue         
                #print("tree length=",len(str2),"   species=",fct_num)
                Pi=fct_num/len(strr)
                shannon_res.append((-1*Pi*math.log(Pi))/math.log(len(strr)))
                sum_shannon=0
                #print("shannon_res",shannon_res)
                #print("j=",j)
            for l in range(0,len(shannon_res)):
                shannon=shannon+shannon_res[l]
                #print("l=",l)
                #print("##","final shannon=",shannon)

            branch_list.append(len(strr))
            #print(branch_list,'&&')
            shannon_list.append(shannon)
            #print("######shannon list#######",shannon_list)
        else:
            continue
    #print("branch",i, ",calculating",lbl[i])
    n=0
    if len(branch_list) != len(shannon_list):
        print("error,the length of branch_list not equal with shannon_list")
    output.append(lbl[i])
    print(lbl[i])
    print("i=",i)
    output.append("\t")
    output.append(0)
    output.append("\t")
    
    posti=0
    for n in range(2,len(lbl)+1):
        o=0
        iffind=0
        for o in range(0,len(branch_list)):
            if n== branch_list[o]:
                output.append(shannon_list[o])
                output.append('\t')
                #print("find","n=",n,"o=",o,branch_list[o],output)
                iffind=1
                posti=o
                break
            else:
                #print("not find","n=",n,"o=",o,branch_list[o],output)
                continue
        #print("now o is",o,";","n is ",n)
        #print(posti)
        if iffind==0 and 2 not in branch_list and n>2:
            output.append(shannon_list[posti])
            output.append('\t')
            continue
        if iffind==0 and 2 not in branch_list:
            output.append("0")
            output.append('\t')
            #print(branch_list,"not 2")
            continue
        elif iffind==0 and 2 in branch_list:
            output.append(shannon_list[posti])
            output.append('\t')
            
    output.append('\n')
    fi2.seek(0)
    
        
print("all program finished")
output = ''.join(map(str,output))
fo2.write(output+'\n')
fi2.close()
fo.close()
fo2.close()
        
    
        
            
                    

