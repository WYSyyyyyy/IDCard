# -*- coding:utf-8 -*-



#身份证计算公式
def calIDCard(idNum):
    idc_len = len(idNum)
    print('身份证长度为：'+ str(idc_len))
class IDCard():
    num_1 = 0

    def run(self, idNum):
        idc_len = len(idNum)
        if idc_len == 18:
            self.idCard = idNum
            self.qiepian()
            # self.sum()
            # self.shunxuhao()
            self.shengri()

        else:
            print('身份证不是18位，请重新输入18位二代身份证。')
        
    def qiepian(self):
        self.num_0 = int(self.idCard[0])
        self.num_1 = int(self.idCard[1])
        self.num_2 = int(self.idCard[2])
        self.num_3 = int(self.idCard[3])
        self.num_4 = int(self.idCard[4])
        self.num_5 = int(self.idCard[5])
        self.num_6 = int(self.idCard[6])
        self.num_7 = int(self.idCard[7])
        self.num_8 = int(self.idCard[8])
        self.num_9 = int(self.idCard[9])
        self.num_10 = self.idCard[10]
        self.num_11 = self.idCard[11]
        self.num_12 = self.idCard[12]
        self.num_13 = self.idCard[13]
        self.num_14 = int(self.idCard[14])
        self.num_15 = int(self.idCard[15])
        self.num_16 = int(self.idCard[16])
        # self.num_17 = int(self.idCard[17])
    
    #第一步，计算综合
    def sum(self):
        idSum = 0
        idSum += self.num_0 * 7
        idSum += self.num_1 * 9
        idSum += self.num_2 * 10
        idSum += self.num_3 * 5
        idSum += self.num_4 * 8
        idSum += self.num_5 * 4
        idSum += self.num_6 * 2
        idSum += self.num_7 * 1
        idSum += self.num_8 * 6
        idSum += self.num_9 * 3
        idSum += self.num_10 * 7
        idSum += self.num_11 * 9
        idSum += self.num_12 * 10
        idSum += self.num_13 * 5
        idSum += self.num_14 * 8
        idSum += self.num_15 * 4
        idSum += self.num_16 * 2

        yushu = idSum % 11
        predictNum = ''
        if yushu == 0:
            predictNum = '1'
        elif yushu == 1:
            predictNum = '0'
        elif yushu == 2:
            predictNum = 'X'
        elif yushu == 3:
            predictNum = '9'
        elif yushu == 4:
            predictNum = '8'
        elif yushu == 5:
            predictNum = '7'
        elif yushu == 6:
            predictNum = '6'
        elif yushu == 7:
            predictNum = '5'
        elif yushu == 8:
            predictNum = '4'
        elif yushu == 9:
            predictNum = '3'
        elif yushu == 10:
            predictNum = '2'
        
        if predictNum == self.idCard[17]:
            print('校验成功，这是真的身份证。')

    def shunxuhao(self):
        idSum = 0
        idSum += self.num_0 * 7
        idSum += self.num_1 * 9
        idSum += self.num_2 * 10
        idSum += self.num_3 * 5
        idSum += self.num_4 * 8
        idSum += self.num_5 * 4
        idSum += self.num_6 * 2
        idSum += self.num_7 * 1
        idSum += self.num_8 * 6
        idSum += self.num_9 * 3
        idSum += self.num_10 * 7
        idSum += self.num_11 * 9
        idSum += self.num_12 * 10
        idSum += self.num_13 * 5

        idSumMin = idSum
        idSumMax = idSum + 9*14
        yushu = 11

        jiaoyanma = self.idCard[17]
        if jiaoyanma == '0':
            yushu = '1'
        elif jiaoyanma == '1':
            yushu = '0'
        elif jiaoyanma == '2':
            yushu = 'X'
        elif jiaoyanma == '3':
            yushu = '9'
        elif jiaoyanma == '4':
            yushu = '8'
        elif jiaoyanma == '5':
            yushu = '7'
        elif jiaoyanma == '6':
            yushu = '6'
        elif jiaoyanma == '7':
            yushu = '5'
        elif jiaoyanma == '8':
            yushu = '4'
        elif jiaoyanma == '9':
            yushu = '3'
        elif jiaoyanma == 'X':
            yushu = '2'

        # print(idSumMin,idSumMax,yushu)
        num = []
        for x in range(idSumMin, idSumMax):
            if x % 11 == int(yushu):
                num.append(x)
        
        for x in num:
            for i in range(9):
                for j in range(9):
                    for k in range(9):
                        if k%2 == 1:
                            continue
                        if (i*8 + j*4 + k*2) == (x-idSumMin):
                            print('顺序号为：'+str(i)+str(j)+str(k))

    def shengri(self):
        idSum = 0
        idSum += self.num_0 * 7
        idSum += self.num_1 * 9
        idSum += self.num_2 * 10
        idSum += self.num_3 * 5
        idSum += self.num_4 * 8
        idSum += self.num_5 * 4
        idSum += self.num_6 * 2
        idSum += self.num_7 * 1
        idSum += self.num_8 * 6
        idSum += self.num_9 * 3
        # idSum += self.num_10 * 7
        idSum += self.num_14 * 8
        idSum += self.num_15 * 4
        idSum += self.num_16 * 2

        jiaoyanma = self.idCard[17]
        if jiaoyanma == '0':
            yushu = '1'
        elif jiaoyanma == '1':
            yushu = '0'
        elif jiaoyanma == '2':
            yushu = 'X'
        elif jiaoyanma == '3':
            yushu = '9'
        elif jiaoyanma == '4':
            yushu = '8'
        elif jiaoyanma == '5':
            yushu = '7'
        elif jiaoyanma == '6':
            yushu = '6'
        elif jiaoyanma == '7':
            yushu = '5'
        elif jiaoyanma == '8':
            yushu = '4'
        elif jiaoyanma == '9':
            yushu = '3'
        elif jiaoyanma == 'X':
            yushu = '2'
        idSumMin = idSum
        #1*7,前面为身份证号，后面为要乘的数
        idSumMax = idSum + 1*7+9*9+3*10+9*5

        num = []
        for x in range(idSumMin,idSumMax):
            if x%11 == int(yushu):
                num.append(x)
        n = 0
        for x in num:
            for i in range(1+1):
                for j in range(9+1):
                    if i == 0 and j == 0:
                        continue
                    if i ==1 and j > 2:
                        continue
                    for k in range(3+1):
                        for l in range(9+1):
                            if k == 0 and l == 0:
                                continue
                            if k == 3 and l > 1:
                                continue
                            if (i*7+j*9+k*10+l*5) == x - idSumMin:
                                print('生日为：'+str(i)+str(j)+str(k)+str(l))
                            n += 1
        print('总共运算'+str(n)+'次！')


if __name__ == "__main__":
    calIDCard = IDCard()
    # calIDCard.run('452402199209265175')
    # calIDCard.run('4524021992****5175')
    # calIDCard.run('6104301992****052X')
    # calIDCard.run('4128251990****702X')
    # calIDCard.run('440785199807214611')
    calIDCard.run('3710821980****7111')
    