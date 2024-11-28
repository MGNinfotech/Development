class ListEncrypt:#Style 1

    def __init__(self):
        self.intArray1 =[14,9,12,11,7,13,16,5,17,12,9,15,18,14,19,11,16,12,18,10,20,15,12,19,25,14,28,7,16,11]
        self.charSet1="`1234567890-=[];,./ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^*()_+abcdefghijklmnopqrstuvwxyz{}|:?"
    def encryptData(self,str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet1.find(s)
            if i%2==0:
            #4
                ch1=ch+self.intArray1[i%len(self.intArray1)]
                if ch1>=len(self.charSet1):
                #5
                    ch1=ch1-len(self.charSet1)
                #5
            #4
            else:
            #4
                ch1=ch-self.intArray1[i%len(self.intArray1)]
                if ch1<0:
                #5
                    ch1=len(self.charSet1)+ch1
                #5
            #4
            v_ch=self.charSet1[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr
    def decryptData(str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet1.find(s)
            if i%2==0:
            #4
                ch1=ch-self.intArray1[i%len(self.intArray1)]
                if ch1<0:
                #5
                    ch1=len(self.charSet1)+ch1
                #5
            #4
            else:
            #4
                ch1=ch+self.intArray1[i%len(self.intArray1)]
                if ch1>=len(self.charSet1):
                #5
                    ch1=ch1-len(self.charSet1)
                #5
            #4
            v_ch=self.charSet1[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr

class NewEnryption: #Style 2
    def __init__(self):
        self.intArray2=[16,12,18,10,14,9,12,9,15,18,14,19,11,20,15,12,19,25,12,11,7,13,16,5,17,14,28,7,16,11]
        self.charSet2='`123efghijklmnopqrst456-=[7890];,./ABCDEFGHuvwxXYZ~!@#$%^*()_+abcdyz{}|:?IJKLMNOPQRSTUVW'
    def encryptData(self,str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet2.find(s)
            if i%2==0:
            #4
                ch1=ch+self.intArray2[i%len(self.intArray2)]
                if ch1>=len(self.charSet2):
                #5
                    ch1=ch1-len(self.charSet2)
                #5
            #4
            else:
            #4
                ch1=ch-self.intArray2[i%len(self.intArray2)]
                if ch1<0:
                #5
                    ch1=len(self.charSet2)+ch1
                #5
            #4
            v_ch=self.charSet2[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr
    def decryptData(self, str):

        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet2.find(s)
            if i%2==0:
            #4
                ch1=ch-self.intArray2[i%len(self.intArray2)]
                if ch1<0:
                #5
                    ch1=len(self.charSet2)+ch1
                #5
            #4
            else:
            #4
                ch1=ch+self.intArray2[i%len(self.intArray2)]
                if ch1>=len(self.charSet2):
                #5
                    ch1=ch1-len(self.charSet2)
                #5
            #4
            v_ch=self.charSet2[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr

class SpringEncryption: #Style 3
    def __init__(self):
        self.intArray3=[16,12,18,10,14,9,12,9,15,18,14,19,11,20,15,12,19,25,12,11,7,13,16,5,17,14,28,7,16,11]
        self.charSet3="`123efghijklmnopqrst456-=[7890];,./ABCDEFGHuvwxXYZ~!@#$%^*()_+abcdyz{}|:?IJKLMNOPQRSTUVW\""
    def encryptData(str):

        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet3.find(s)
            if i%2==0:
            #4
                ch1=ch+self.intArray3[i%len(self.intArray3)]
                if ch1>=len(self.charSet3):
                #5
                    ch1=ch1-len(self.charSet3)
                #5
            #4
            else:
            #4
                ch1=ch-self.intArray3[i%len(self.intArray3)]
                if ch1<0:
                #5
                    ch1=len(self.charSet3)+ch1
                #5
            #4
            v_ch=self.charSet3[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr
    def decryptData(str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet3.find(s)
            if i%2==0:
            #4
                ch1=ch-self.intArray3[i%len(self.intArray3)]
                if ch1<0:
                #5
                    ch1=len(self.charSet3)+ch1
                #5
            #4
            else:
            #4
                ch1=ch+self.intArray3[i%len(self.intArray3)]
                if ch1>=len(self.charSet3):
                #5
                    ch1=ch1-len(self.charSet3)
                #5
            #4
            v_ch=self.charSet3[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr

class AlphaNumericCrypto: #Style 4
    def __init__(self):
        self.intArray4=[16,12,18,10,14,9,12,9,15,18,14,19,11,20,15,12,19,25,12,11,7,13,16,5,17,14,28,7,16,11]
        self.charSet4="123efghijklmnopqrst456ABCDEFGHuvwxXYZ7890abcdyzIJKLMNOPQRSTUVW"
    def encryptData(self,str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet4.find(s)
            if i%2==0:
            #4
                ch1=ch+self.intArray4[i%len(self.intArray4)]
                if ch1>=len(self.charSet4):
                #5
                    ch1=ch1-len(self.charSet4)
                #5
            #4
            else:
            #4
                ch1=ch-self.intArray4[i%len(self.intArray4)]
                if ch1<0:
                #5
                    ch1=len(self.charSet4)+ch1
                #5
            #4
            v_ch=self.charSet4[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr
    def decryptData(self,str):
        retStr=""
        i=0
        for s in str:
        #3
            ch=self.charSet4.find(s)
            if i%2==0:
            #4
                ch1=ch-self.intArray4[i%len(self.intArray4)]
                if ch1<0:
                #5
                    ch1=len(self.charSet4)+ch1
                #5
            #4
            else:
            #4
                ch1=ch+self.intArray4[i%len(self.intArray4)]
                if ch1>=len(self.charSet4):
                #5
                    ch1=ch1-len(self.charSet4)
                #5
            #4
            v_ch=self.charSet4[ch1:ch1+1]
            retStr=retStr+v_ch
            i+=1
        #3
        return retStr
