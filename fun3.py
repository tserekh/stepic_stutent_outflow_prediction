# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 00:59:10 2016

@author: Artem
"""
def make_3d():
    #list1=['discovered','passed','started_attempt','viewed']
    #list2=['choice', 'code', 'number', 'string', 'text', 'video']
    list1 = ['passed']
    list2 = ['all']
    #list2 = ['choice']    
    list12=[]    
    for el1 in list1:
        for el2 in list2:
                list12.append( [el1, el2] )
    return list12


def get_X(filename,word,word2):
    f=open(filename,"r")
    print("opened") 
    data=f.read()
    list_train=data.split("\n")
    del list_train[-1]
    del list_train[0]
    #df_train all train data
    df_train=[]
    for row in list_train:
        sp_row=row.split(",")
        df_train.append(sp_row)

    f=open("C:/Users/Artem/Documents/stepic/kaggle/structure.csv","r")
    print("opened") 
    data=f.read()
    list_structure=data.split("\n")
    del list_structure[-1]
    del list_structure[0]
    #df_structure=[] - list of step ids
    df_structure=[]
    for row in list_structure:
        sp_row=row.split(",")
        df_structure.append(int(sp_row[5]))
#pattern - pattern for future row in X matrix
    pattern={}
    
    for el in df_structure:
        pattern[el]=900000000
    pattern[0]=0
   #make dictionary for users id
    
    id_dic={}
    for el in df_train:
        id_dic[int(el[0])]=pattern.copy()

    for el in df_train:
        
        ID=int(el[0])
        action=el[1]
        step_id=int(el[2])
        step_type=el[4]
        id_dic[ID][0]=int(ID)
        if (action==word or step_type==word2):
            if (int(el[3])!=900000000):
                if(int(el[3])<1440000000):
                    id_dic[ID][step_id]=int(el[3])-1403598242
                else:
                    id_dic[ID][step_id]=int(el[3])-1442178044
    semi=dic_to_list(id_dic)
    
    X=[]
    for el in semi:
        X.append(dic_to_list(el))
    return X

def dic_to_list(dic):
    list1=[]
    for el in sorted(dic):
        list1.append(dic[el])
    return list1

def get_targed(filename):
    f=open(filename,"r")
    print("opened") 
    data=f.read()
    list1=data.split("\n")
    del list1[-1]
    del list1[0]
    df=[]
    for row in list1:
        sp_row=row.split(",")
        df.append(int(sp_row[2]))
    return(df)
def  cbind(list1,list2):
    list12=[]
    for i in range(len(list1)):
        list12.append(list1[i]+list2[i])
    return list12