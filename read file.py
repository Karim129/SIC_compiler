from typing import Counter

import math
def location_counter_table(keyword):  # search for keyword properties
    location_codes = {
        "FIX": ["1", "C4"],
        "FLOAT": ["1", "C0"],
        "HIO": ["1", "F4"],

        "NORM": ["1", "C8"]

        , "SIO": ["1", "F0"]

        , "TIO": ["1", "F8"]

        , "ADDR": ["2", "90"]

        , "CLEAR": ["2", "B4"]

        , "COMPR": ["2", "A0"]

        , "DIVR": ["2", "9C"]

        , "MULR": ["2", "98"]

        , "RMO": ["2", "AC"]

        , "SHIFTL": ["2", "A4"]

        , "SHIFTR": ["2", "A8"]

        , "SUBR": ["2", "94"]

        , "SVC": ["2", "B0"]

        , "TIXR": ["2", "B8"]

        , "ADD": ["3", "18"]

        , "ADDF": ["3", "58"],

        "AND": ["3", "40"]

        , "COMP": ["3", "28"]

        , "COMPF": ["3", "88"]

        , "DIV": ["3", "24"]

        , "DIVF": ["3", "64"]

        , "J": ["3", "3C"]

        , "JEQ": ["3", "30"]

        , "JGT": ["3", "34"]

        , "JLT": ["3", "38"]

        , "JSUB": ["3", "48"]

        , "LDA": ["3", "00"]

        , "LDB": ["3", "68"]

        , "LDCH": ["3", "50"]

        , "LDF": ["3", "70"]

        , "LDL": ["3", "08"]

        , "LDS": ["3", "6C"]

        , "LDT": ["3", "74"]

        , "LDX": ["3", "04"]
        , "LPS": ["3", "D0"]
        , "MUL": ["3", "20"]
        , "MULF": ["3", "60"]
        , "OR": ["3", "44"]
        , "RD": ["3", "D8"]
        , "RSUB": ["3", "4C"]
        , "SSK": ["3", "EC"]
        , "STA": ["3", "0C"]
        , "STB": ["3", "78"]
        , "STCH": ["3", "54"]
        , "STF": ["3", "80"]
        , "STI": ["3", "D4"]
        , "STL": ["3", "14"]
        , "STS": ["3", "7C"]
        , "STSW": ["3", "E8"]
        , "STT": ["3", "84"]
        , "STX": ["3", "10"]
        , "SUB": ["3", "1C"]
        , "SUBF": ["3", "5C"]
        , "TD": ["3", "E0"]
        , "TIX": ["3", "2C"],
        "WD": ["3", "DC"]

        
    }

    return location_codes[keyword]
def cal_object(location,label,instruction,reference,base,table):
    object_code=[]
    for i in range(len(reference)):
        if instruction[i]=="END" or instruction[i]=="BASE" or instruction[i]=="RESW" or instruction[i]=="RESB":
            continue
        elif (instruction[i].strip())[0]=="+":
            
            obj=location_counter_table( (instruction[i])[1:]   )
            object_code.append(formate4(location[i],label[i],instruction[i],reference[i],obj[1]))
        elif instruction[i] == "RESW" or instruction[i] == "RESB" or instruction[i]=="BASE":
            object_code.append("------")
        elif instruction[i]=="WORD":
            clc_oj=format(int(reference[i]),"b").zfill(24)
            object_code.append(clc_oj)
        elif instruction[i]=="BYTE":
            xORc=reference[i]
            if xORc[0].strip()=="X":
                clc_oj=(reference[i])[2:6]
                object_code.append(clc_oj)
            elif xORc[0].strip()=="C":
                oj=reference[i]
                #print(type(oj))
                object_code.append(str(ord(oj[2]))+str(ord(oj[3]))+str(ord(oj[4]))+str(ord(oj[5])))
          
        else:
            if location_counter_table(instruction[i])[0]=="3":
                pc=location[i+1]
                if reference[i]=="*":
                    
                    object_code.append(format(int(location_counter_table(instruction[i])[1],16),"b"))
                    continue
                elif (instruction[i])[0]=="+":
                    obj=location_counter_table((instruction[i])[1:])
                else:
                    obj=location_counter_table(instruction[i])
        
                object_code.append(clc_formate3(location[i],label[i],instruction[i],reference[i],obj[1],pc,table[base]))
            elif location_counter_table(instruction[i])[0]=="2":
                r1=(reference[i].split(','))
                if r1[0]=="*":
                    object_code.append(calc_formate20(instruction[i]))
                elif len(r1)==1:
                    object_code.append(calc_formate21(instruction[i],r1[0]))
                    
                else:
                    object_code.append(calc_formate2(instruction[i],r1[0],r1[1]))
            else:
                object_code.append(location_counter_table(instruction[i])[1])
    return object_code         
                
    
    

def formate4(location,label,instruction,reference,op_code):
    
    e=1
    if len(reference.split(","))==2:
        x=1
        reference=reference.split(',')[0]
    else:
        x=0
    if reference[0]=="#":
        reference=reference[1:]
        if reference[1:].isdigit():
            addresses=format(int(reference),"b").zfill(20)
        else:
            addresses=format(int(table[reference]),"b")
            
         
        i,n=1,0
        
    elif reference[0]=="@":
        i,n=0,1
        reference=reference[1:]
        addresses=format(int(table[reference]),"b")
    else:
        i,n=1,1
        addresses=table[reference]
    
        addresses=int(addresses,16)
    
        addresses=format(addresses,"b").zfill(20)
        op_code=format(int(op_code,16),"b")[:-2]
    return op_code+str(n)+str(i)+str(x)+"0"+"0"+"1"+addresses
def calc_formate2(instruction,r1,r2):
    register={ 
     "A": "0",
     "X":"1",
      "B":"4",
      "S":"5",
      "T":"6",
       "F":"7"
       }
    x=format(int((location_counter_table(instruction))[1],16),"b").zfill(8)
    x1=format(int(str(register[r1])+str(register[r2]),16),"b").zfill(8)
    
    return x+x1
def calc_formate21(instruction,r1):
    register={ 
     "A": "0",
     "X":"1",
      "B":"4",
      "S":"5",
      "T":"6",
       "F":"7"
       }
    x=format(int((location_counter_table(instruction))[1],16),"b").zfill(8)
    x1=format(int(str(register[r1]),16),"b").zfill(8)
    
    return x+x1
def calc_formate20(instruction):
    register={ 
     "A": "0",
     "X":"1",
      "B":"4",
      "S":"5",
      "T":"6",
       "F":"7"
       }
    x=format(int((location_counter_table(instruction))[1],16),"b").zfill(8)
    
    
    return x
def clc_formate3(location,label,instruction,reference,op_code,pc,base):
    e=0
    b=0
    p=0
    x=0
    if len(reference.split(","))==2:
        x=1
        reference=reference.split(",")[0]
    else:
        x=0
        
    
    if reference[0]=="#":
        i,n=1,0
        reference=reference[1:]
        if reference.isdigit():
            disp=int(reference,10)
            
        else:
            
            TA=table[reference]
            disp=int(TA,16)
    elif reference[0]=="@":
        i,n=0,1
        reference=reference[1:]
        TA=table[(reference.split(","))[0]]
        disp=int(TA,16)-int(pc,16)
        
    else:
        i,n=1,1
        
        TA=table[reference]
        
        disp=int(TA,16)-int(pc,16)
    if -2048<disp and disp<2047:
        p=1
        b=0
        op_code=bin(int(op_code,16))[:-2]
        disp=str(bin(disp))[2:]
        #print(type(disp))
        x1=op_code[2:]+str(n)+str(i)+str(x)+str(b)+str(p)+str(e)+disp.zfill(15)
        
        return x1
        
    elif 2047<disp and disp<4095:
        disp=int(TA,16)-int(base,16)
        p=0
        b=1
        op_code=bin(int(op_code,16))[:-2]
        return op_code[2:]+str(n)+str(i)+str(x)+str(b)+str(p)+str(e)+str(bin(disp).zfill(15))
        
    
        
    
    else:
        formate4(location,label,instruction,reference,op_code)
        

        
def divide_chunks(l,location_counter): #l is oject code
    t=""
    tList=[]
    Counter=0
    for i in range(len(l)):
        if instruction[i]=="RESW" or instruction[i]=="RESB":
            if t!="":
                tList.append(t)
                t = ""
            Counter = 0
            continue
        elif instruction[i]!="RESW"or instruction[i]!="RESB":
            if Counter==0:
                t+=str(location_counter[i])+"#$"+str(l[i]) 
                Counter=Counter+1
            elif Counter==10:
                tList.append(t) #i=10, counter =10
                t = ""
                if instruction[i]!="RESW" or instruction[i]!="RESB":
                    t=str(location_counter[i])+"#$"+str(l[i])
                    Counter=1
                Counter = 0
                continue
                
            else:
                t+=str(l[i]) 
                Counter=Counter+1
        elif instruction[i]=="BASE":
            continue
        
 
                
    tList.append(t)        
    return tList
    
  
def cal_location_counter(instruction, reference, start):  # return location counter list and uncompleted object code
   
    location_table = []
    B=""
    location_table.append(hex(start)) 
    for i in range(len(instruction)):
        if instruction[i] == "RESW":
            location = start+ (int(reference[i]) * 3) #calculate location counter 
            location_table.append(hex(location))
            start += int(reference[i]) * 3 #increase the start
            
        elif instruction[i] == "RESB":
            if reference[i]=="*":
                location_table.append(hex(start+1))
                start+=1
            else:
                
                location = start + int(reference[i])
                location_table.append(hex(location))
                start += int(reference[i])
                
        elif instruction[i]=="WORD":
            location = start + 3
            location_table.append(hex(location))
            start += 3
            
        elif instruction[i]=="BYTE":
            xORc=reference[i]
            if xORc[0].strip()=="X":
                
                location = start + (len(reference[i])-3)//2
                location_table.append(hex(location))
                start +=  len(reference[i])-3
                
            elif xORc[0].strip()=="C":
                location = start + len(reference[i])-3
                location_table.append(hex(location))
                start +=  len(reference[i])-3
                
        elif (instruction[i])[0]=="+":
            location = start + 4
            location_table.append(hex(location))
            start +=  4
            
        elif instruction[i]=="BASE":
            location = start 
            location_table.append(hex(location))
            start +=  0
            B=reference[i] #base
            



        else:
            l=location_counter_table(instruction[i].strip()) # return size that location will increase and instruction code
            
            location = start + int(l[0])
            location_table.append(hex(location))
            start += int(l[0])
            
    return location_table,B
"""def calculate_tRecord_size(list_of_tRcord):
    return_list=[]
    for i in list_of_tRcord:
        begin=i[:6]
        length=len(i[9:])/6
        length=math.ceil(length)
        index_of_first=0
        for j in range(len(location_counter)):
            if location_counter[j]==begin:
                index_of_first=j
                break
        defference=int(location_counter[length+index_of_first],16)-int(location_counter[index_of_first],16)
        
        return_list.append(i.replace("#$",hex(defference)[2:] )   )
    return return_list"""


f = open("inSICXE.txt", "r")
start = 0
label = []
instruction = []
reference = []
pogram_name=""


for line in f.readlines():
    if line.isspace():
        break

    else:
        x = line.strip().split("\t")
        # print(x)
        if x[0]=="BASE":
            base=x[1]
            print("base"+base)
            continue
        if len(x) == 3:
            if x[1] == "START":
                start = x[2]
                pogram_name=x[0]
                continue
            else:
                label.append(x[0])
                reference.append(x[2])
                instruction.append(x[1])
                continue
        elif len(x)==1 :
            label.append("$")
            reference.append("*")
            instruction.append(x[0])
            continue
        


        else:
            if x[0] == "END":
                continue
            else:
                label.append("$")
                reference.append(x[1])
                instruction.append(x[0])
                continue
        



f.close()
start=int(start,16) #beginig of code as interger 


  


location_counter,base = cal_location_counter(instruction, reference, start)
#print(location_counter)
instruction.append("End")
table={} 
for i in range(len(label)): #create table 
    if label[i]!="$":
        table[label[i]]=location_counter[i]
print(base)       
for i in range(len(label)):
    print(location_counter[i]+"  "+label[i]+"  "+instruction[i]+"  "+reference[i])
object_code=cal_object(location_counter,label,instruction,reference,base,table)
"""for i in object_code:
    print(i)"""
print(len(location_counter))
"""clc_program_lengh=(hex(int(location_counter[-1],16)-int(location_counter[0],16)))[2:]                
head=pogram_name+"00"+(location_counter[0])[2:]+"#00"+"0"*(4-len(clc_program_lengh))+clc_program_lengh
E_record="00"+(location_counter[0])[2:]


t_record=calculate_tRecord_size(divide_chunks(object_code,location_counter))
t_record="\n".join(t_record)
for i in range(len(reference)):
    print(location_counter[i]+"     " + label[i] + "     " + instruction[i] + "      " + reference[i]+"         "+object_code[i])

print("HEAD:\n"+head)
print("TAIL:\n"+t_record)
print("END: "+E_record)
"""
