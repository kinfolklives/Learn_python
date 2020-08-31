import random 

class Lotto:
    def __init__(self):
        self.lotto=[0,0,0,0,0,0]

    def createLottoNum(self):
        # n = random.randint(1,10)
        # self.lotto[0] = n 
        # n = random.randint(1,10)
        # self.lotto[1] = n 
        # n = random.randint(1,10)
        # self.lotto[2] = n
        # ---
        # for i in range(0,6):
        #     n  = random.randint(1,10)
        #     self.lotto[i] = n 
        # ---
        """
        1. 값을 하나 랜덤하게 추출한다. 
        2. 이 값이 배열에 존재하는지 확인한다. 
        만약에 존재하면 1번으로 돌아간다. 
        존재하지 않으면 배열에 넣고 카운트를 하나 증가시킨다. 
        카운트가 6이 될때까지
        """
        cnt = 0
        while(cnt<6):
            n =random.randint(1,10)
            if n not in self.lotto:
                self.lotto[cnt] = n 
                cnt += 1
        # print(self.lotto)
    
    def matching(self, lottoNum):
        nums = lottoNum.split(",")
        nums = [int(i) for i in nums]
        
        matchCnt = 0;
        for i in nums:
            if i in self.lotto:
                matchCnt=matchCnt+1
        if matchCnt == 6:
            return "********* 1등에 당첨 되셨습니다.  ************"
        else:
            return str(matchCnt) + "개 맞췄습니다"

lotto = Lotto()
lotto.createLottoNum()
print(lotto.matching('1,3,4,5,6,9'))
