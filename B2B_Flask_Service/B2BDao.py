import json
from dbHandeling import validateHeader,validateCustomer,postTransaction
from utility import readPropertyFile,writeLog

def validateInputAccountValidation(jsonstring):
    writeLog('validateInputAccountValidation-1-',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    returnjson={}
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        errpoint='.01'
        headerdict={}
        headerdict=paramdict['header']
        errpoint='.02'

        requestdict={}
        requestdict=paramdict['request']
        errpoint='.03'

        serviceName=headerdict['serviceName']
        errpoint='.04'
        messageID=headerdict['messageID']
        errpoint='.05'
        connectionID=headerdict['connectionID']
        errpoint='.06'
        connectionPassword=headerdict['connectionPassword']
        errpoint='.07'
        TransactionReferenceCode=requestdict['TransactionReferenceCode']
        errpoint='.09'
        TransactionDate=requestdict['TransactionDate']
        errpoint='.10'
        InstitutionCode=requestdict['InstitutionCode']
        errpoint='.11'
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        retstr= {'header':{'messageID':messageID,'statusCode':'400','statusDescription':'The parameters are not valid or they are missing.'+str(errpoint)}}
    if bool==True :
        try:
            errpoint='.081111'
            vd=validateHeader(connectionID,connectionPassword)
            errpoint=vd['RESPCODE']
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            print(conn)
            if conn!=None:
                DBparamdict={}
                DBparamdict['VALIDATIONSTR']=TransactionReferenceCode
                defaultDict=readPropertyFile('b2b.properties')
                DBparamdict['VENDORID']=defaultDict['VENDORID']
                #DBparamdict['VENDORREQSTR']=jsonstring
                print(DBparamdict)

                retstr= validateCustomer(conn,str(DBparamdict))
                print(retstr)
                writeLog('validateInputAccountValidation-2',str(retstr))
                retstrjson={}
                retstrjson=json.loads(retstr)
                respcode=retstrjson['RESPCODE']
                errpoint='.02'

                if respcode==0:
                    respdesc={}
                    respdesc=retstrjson['RESPDESC']
                    custname=respdesc['CUSTNAME']
                    accno=respdesc['ACCNO']
                    headerdict={}
                    requestdict={}
                    headerdict['messageID']=messageID
                    headerdict['statusCode']=200
                    headerdict['statusDescription']='Success'

                    requestdict['TransactionReferenceCode']=TransactionReferenceCode
                    requestdict['TransactionDate']=TransactionDate
                    requestdict['TotalAmount']='0.0'
                    requestdict['Currency']=''
                    requestdict['AdditionalInfo']=custname
                    requestdict['AccountNumber']=accno
                    requestdict['AccountName']=custname
                    requestdict['InstitutionCode']=InstitutionCode
                    defaultvalues=readPropertyFile('defaultvalues.properties')
                    requestdict['InstitutionName']=defaultvalues['InstitutionName']

                    returnjson['header']=headerdict
                    returnjson['request']=requestdict
                elif respcode==1:
                    returnjson= {'header':{'messageID':messageID,'statusCode':'404','statusDescription':'The task/operation does not exist.'}}
                else:
                    returnjson= {'header':{'messageID':messageID,'statusCode':'405','statusDescription':'A severe problem has occurred.'}}
            else:
                print('The caller is not authorized for this request.')
                returnjson= {'header':{'messageID':messageID,'statusCode':'401','statusDescription':'The caller is not authorized for this request.'}}
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            returnjson= {'header':{'messageID':messageID,'statusCode':'405','statusDescription':'A severe problem has occurred.'+str(errpoint)+str(e)}}

    else:
        print("A severe problem has occurred."+str(errpoint))
        returnjson= {'header':{'messageID':messageID,'statusCode':'405','statusDescription':'A severe problem has occurred.'+str(errpoint)}}
    writeLog('validateInputAccountValidation-3-',str(returnjson))
    return returnjson


def postTran(jsonstring):
    writeLog('postTran-1-',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    defaultDict=readPropertyFile('defaultvalues.properties')
    returnjson={}
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        #print(
        errpoint='.01'
        headerdict={}
        headerdict=paramdict['header']
        #print(
        errpoint='.02'

        requestdict={}
        requestdict=paramdict['request']
        #print(errpoint)
        errpoint='.03'

        serviceName=headerdict['serviceName']
        #print(errpoint)
        errpoint='.04'
        messageID=headerdict['messageID']
        #print(errpoint)
        errpoint='.05'
        connectionID=headerdict['connectionID']
        #print(errpoint)
        errpoint='.06'
        connectionPassword=headerdict['connectionPassword']
        #print(errpoint)
        errpoint='.07'
        TransactionReferenceCode=requestdict['TransactionReferenceCode']
        #print(errpoint)
        errpoint='.09'
        TransactionDate=requestdict['TransactionDate']
        #print(errpoint)
        errpoint='.10'
        InstitutionCode=requestdict['InstitutionCode']
        #print(errpoint)
        errpoint='.11'
        TotalAmount=requestdict['TotalAmount']
        #print(errpoint)
        errpoint='.12'
        requestdict['Currency']=''
        #print(errpoint)
        errpoint='.13'
        DocumentReferenceNumber=requestdict['DocumentReferenceNumber']
        #print(errpoint)
        errpoint='.14'
        try:
            BankCode=requestdict['BankCode']
            #print(errpoint)
            errpoint='.15'
        except Exception as ex:
            BankCode=defaultDict['BankCode']
            print(errpoint)
            errpoint='.15'
        try:
            BranchCode=requestdict['BranchCode']
            #print(errpoint)
            errpoint='.16'
        except Exception as ex:
            BranchCode=defaultDict['BranchCode']
            print(errpoint)
            errpoint='.16'
        PaymentDate=requestdict['PaymentDate']
        #print(errpoint)
        errpoint='.17'
        requestdict['PaymentReferenceCode']=''
        #print(errpoint)
        errpoint='.18'
        try:
            PaymentReferenceCode=requestdict['PaymentReferenceCode']
            if PaymentReferenceCode==None:
                requestdict['PaymentReferenceCode']=""
            #print(errpoint)
            errpoint='.181'
        except Exception as ex:
            requestdict['PaymentReferenceCode']=""
            print(errpoint)
            errpoint='.181'
        errpoint='.182'
        try:
            PaymentCode=requestdict['PaymentCode']
            if PaymentCode == None:
                requestdict['PaymentCode']=""
            #print(errpoint)
            errpoint='.183'
        except Exception as ex:
            requestdict['PaymentCode']=""
            print(errpoint)
            errpoint='.184'
        errpoint='.185'
        try:
            PaymentMode=requestdict['PaymentMode']
            if PaymentMode == None:
                requestdict['PaymentMode']=defaultDict['PaymentMode']
            #print(errpoint)
            errpoint='.19'
        except Exception as ex:
            PaymentMode=defaultDict['PaymentMode']
            print(errpoint)
            errpoint='.19'
        try:
            PaymentAmount=requestdict['PaymentAmount']
            #print(errpoint)
            errpoint='.20'
        except Exception as ex:
            requestdict['PaymentAmount']=TotalAmount
            print(errpoint)
            errpoint='.20'
        try:
            AdditionalInfo=requestdict['AdditionalInfo']
            #print(errpoint)
            errpoint='.21'
        except Exception as ex:
            requestdict['AdditionalInfo']=DocumentReferenceNumber
            print(errpoint)
            errpoint='.21'
        try:
            AccountNumber=requestdict['AccountNumber']
            #print(errpoint)
            errpoint='.22'
        except Exception as ex:
            requestdict['AccountNumber']=AdditionalInfo
            print(errpoint)
            errpoint='.22'
        requestdict['AccountName']=''
        #print(errpoint)
        errpoint='.23'
        requestdict['InstitutionName']=''
        #print(errpoint)
        errpoint='.24'
        print("header",str(headerdict))
        print("request",str(requestdict))
        paramdict={}
        paramdict['header']=headerdict
        paramdict['request']=requestdict
        writeLog('postTran-2-',str(requestdict))
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        return {'header':{'messageID':messageID,'statusCode':'400'+errpoint,'statusDescription':'The parameters are not valid or they are missing.'}}
    if bool==True :
        try:
            vd=validateHeader(connectionID,connectionPassword)
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            errpoint='.25'
            if conn!=None:
                #print(str(paramdict))
                DBparamdict={}
                DBparamdict['VALIDATIONSTR']=DocumentReferenceNumber
                DBparamdict['TRANREFNO']=TransactionReferenceCode
                propertytDict=readPropertyFile('b2b.properties')
                defaultDict=readPropertyFile('defaultvalues.properties')
                DBparamdict['VENDORID']=propertytDict['VENDORID']
                DBparamdict['TRANAMOUNT']=TotalAmount
                #DBparamdict['VENDORREQSTR']=jsonstring
                DBparamdict['CUSTOMERREFNUMBER']=''
                print(DBparamdict)
                retstr= postTransaction(conn,str(DBparamdict))
                writeLog('postTran-3-',str(retstr));
                if retstr.find("ERROR")>-1:
                    retstr= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}
                else:
                    print(retstr)
                    retstrjson={}
                    retstrjson=json.loads(retstr)
                    respcode=retstrjson['RESPCODE']
                    errpoint='.02'
                    if respcode==0:
                        respdesc={}
                        respdesc=retstrjson['RESPDESC']
                        errpoint='.03'
                        custname=respdesc['CUSTNAME']
                        errpoint='.04'
                        accno=respdesc['ACCNO']
                        headerdict={}
                        requestdict={}
                        headerdict['statusCode']='200'
                        errpoint='.05'
                        headerdict['messageID']=messageID
                        errpoint='.06'
                        headerdict['statusDescription']='Payment successfully received'
                        #headerdict['connectionID']=connectionID
                        #errpoint='.07'
                        #headerdict['connectionPassword']=connectionPassword
                        #errpoint='.08'
                        requestdict['TransactionReferenceCode']=TransactionReferenceCode
                        errpoint='.09'
                        requestdict['TransactionDate']=TransactionDate
                        errpoint='.10'
                        requestdict['TotalAmount']=TotalAmount
                        errpoint='.11'
                        requestdict['Currency']=defaultDict['Currency']
                        errpoint='.12'
                        requestdict['DocumentReferenceNumber']=DocumentReferenceNumber
                        errpoint='.13'
                        requestdict['BankCode']=BankCode
                        errpoint='.14'
                        requestdict['BranchCode']=BranchCode
                        errpoint='.15'
                        requestdict['PaymentDate']=PaymentDate
                        errpoint='.16'
                        requestdict['PaymentReferenceCode']=PaymentReferenceCode
                        errpoint='.17'
                        requestdict['PaymentCode']=PaymentCode
                        errpoint='.18'
                        requestdict['PaymentMode']=PaymentMode
                        errpoint='.19'
                        requestdict['PaymentAmount']=PaymentAmount
                        errpoint='.20'
                        requestdict['AdditionalInfo']=AdditionalInfo
                        errpoint='.21'
                        requestdict['AccountNumber']=AccountNumber
                        errpoint='.22'
                        requestdict['AccountName']=custname
                        errpoint='.23'
                        requestdict['InstitutionCode']=InstitutionCode
                        errpoint='.24'
                        requestdict['InstitutionName']=''
                        errpoint='.25'
                        returnjson['header']=headerdict
                        returnjson['request']=requestdict
                    elif respcode==1:
                        returnjson= {'header':{'messageID':messageID,'statusCode':'404'+errpoint,'statusDescription':'The task/operation does not exist.'}}
                    elif respcode==3:
                        returnjson= {'header':{'messageID':messageID,'statusCode':'402'+errpoint,'statusDescription':'Duplicate transaction detected.'}}
                    else:
                        returnjson= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}
            else:
                print('The caller is not authorized for this request.')
                returnjson= {'header':{'messageID':messageID,'statusCode':'401'+errpoint,'statusDescription':'The caller is not authorized for this request.'}}
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            returnjson= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}

    else:
        print("A severe problem has occurred.")
        returnjson= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}

    writeLog('postTran-4-',str(returnjson));
    return returnjson
