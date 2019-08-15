import time as t

class Mytimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.borrow = [0,12,31,24,60,60]
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self,other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += str(result[index]) + self.unit[index]
        return prompt

    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示：请先调用stop()停止计时'
        print('计时开始')

    #停止计时
    def stop(self):
        if not self.begin:
            self.prompt = '提示：请先调用start()开始计时'
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束')

    #内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            temp = self.end[index]- self.begin[index]
            if temp < 0:
                #测试高位是否有得借，没有借的话再向更高位借……
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i +=1
                    
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)
                
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
                
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
        
t1 = Mytimer()
t2 = Mytimer()
t1.start()
t2.start()
