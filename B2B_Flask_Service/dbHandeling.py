import cx_Oracle
from utility import readPropertyFile,writeLog
from encryption import NewEnryption
def getConnection(user,password,dbconstr):
    dict1={}
    try:
        
        con = cx_Oracle.connect(user+'/'+password+'@'+dbconstr)
        dict1['CONNECTION']=con
        dict1['RESPDESC']="SUCCESS"
        dict1['RESPCODE']=0
        return dict1
    except cx_Oracle.DatabaseError as er:
        print('There is error in the Oracle database:', er)
        dict1['CONNECTION']=None
        dict1['RESPDESC']="Error..."+str(er)
        dict1['RESPCODE']=1
        return dict1

def validateHeader(connectionID,connectionPassword):
    errorpoint=0.81
    conDict=readPropertyFile('b2b.properties')
    errorpoint=0.82
    respcode=0
    respdesc=''
    #print(conDict)
    if conDict != None :
        NE= NewEnryption()
        tCon=getConnection(NE.decryptData(conDict['DATABASEUSER']),NE.decryptData(conDict['DATABASEPASSWORD']),NE.decryptData(conDict['DATABASEURL']))
        cn=tCon["CONNECTION"]
        errorpoint=0.83
        retcon= None
        if cn!=None:
            try:
                errorpoint=0.84
                my_cursor=cn.cursor()
                errorpoint=0.85
                query="select dup_username,dup_password,dup_connstr from dbuserpass where dup_modulename ='B2B_PYTHON'"
                query=query+" and dup_clientid = '"+connectionID+"' and  dup_apikey = '"+connectionPassword+"'"
                #writeLog('validateHeader',query)
                rowcount=0
                my_cursor.execute(query)
                errorpoint=0.86
                rs = my_cursor.fetchall()
                errorpoint=0.87
                while rowcount<len(rs):
                    #print(rs[0][0],'     ',rs[0][1],'       ',rs[0][2])
                    #NE= NewEnryption()
                    dbuser = NE.decryptData(rs[0][0])
                    dbpass = NE.decryptData(rs[0][1])
                    dnconstr = NE.decryptData(rs[0][2])
                    #print(dbuser,dbpass,dnconstr)
                    errorpoint=0.88
                    tCon=getConnection(dbuser,dbpass,dnconstr)
                    retcon= tCon["CONNECTION"]
                    if retcon == None:
                        respcode=1
                        errorpoint=0.89
                        respdesc=tCon["RESPDESC"]
                    else:
                        respcode=0
                        errorpoint=0
                        respdesc='SUCCESS'
                    rowcount+=1
            except Exception as e:
                print('Error in validateHeader ',e)
                respcode=1
                retcon= None
                respdesc=str(e)
        else:
            respcode=405
            retcon= None
            respdesc='Master Connection is null'+tCon['RESPDESC']
    else:
        respcode=1
        retcon= None
        respdesc='Unable to read property file'
    dict1={}
    dict1['RESPCODE']=errorpoint
    dict1['CONNECTION']=retcon
    dict1['RESPDESC']=respdesc
    return dict1

def validateCustomer(conn,json):
    if conn!=None:
        try:
            my_cursor=conn.cursor()
            cur_var=my_cursor.var(str)
            #my_cursor.callproc("B2B_Interface.dp_valtrn",[json, cur_var])
            my_cursor.callproc("B2B_Interface.dp_validate",[json, cur_var])
            return cur_var.getvalue()
        except Exception as e:
            print('error',e)
            str1= "ERROR--"+str(e)
            return str1

def postTransaction(conn,json):
    if conn!=None:
        try:
            my_cursor=conn.cursor()
            cur_var=my_cursor.var(str)
            my_cursor.callproc("B2B_Interface.dp_post",[json, cur_var])
            return cur_var.getvalue()
        except Exception as e:
            print('error',e)
            str1= "ERROR--"+str(e)
            return str1
