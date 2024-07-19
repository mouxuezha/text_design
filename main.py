# 尽量统一把所有的运行的入口都放在这里，防止整乱了。


from prompts.hanggai_prompot import hanggai_prompot
from model_communication.model_communication import model_communication
from model_communication.model_comm_langchain import ModelCommLangchain

class auto_run():
    def __init__(self,model="hanggai") -> None:
        self.model = model
        self.LLM_model = "qianfan" # 这里可以改，默认是qianfan,还有智谱啥的
        self.model_communication = ModelCommLangchain(model_name=self.LLM_model,Comm_type=self.model)
        self.runnig_location = r"auto_test"

        if model == "hanggai":
            self.__hanggai_init()
        pass

    def __hanggai_init(self):
        self.prompts = hanggai_prompot() # 初始化一张空的试卷
        pass

    def run(self):
        if self.model == "hanggai":
            self.__hanggai_init() # 初始化一张空的试卷
            for index in range(1,self.prompts.num+1):
                # 一题一题给它写了。
                self.run_single_hanggai(index=index)
            # 然后把试卷保存一下。
            self.prompts.save_results(self.runnig_location+r"/results_hanggai"+self.LLM_model+r".pkl")
        pass 

    def run_single_hanggai(self,index:int):
        # 这个就是航概的跑第几题那种。

        geshu = self.prompts.num

        timu = self.prompts.get_timu_index(index=index)

        print("第{}题，共{}题".format(index,geshu))
        print(timu)

        # 然后让大模型通信去给它做了。
        daan_LLM = self.model_communication.communicate_with_model(timu)
        print("答案：\n"+daan_LLM)

        # 然后把答案填到试卷上。
        self.prompts.save_daan_index(index=index,daan=daan_LLM)
        
        # # 然后保存一下。
        # self.prompts.save_results(self.runnig_location+r"/{}.pkl".format(index))
        # # 倒也不用每一波都存一下。

        pass
    
    def hanggai_pigai(self, index_start=1):
        # 先把做完的试卷读取进来。
        self.prompts.load_results(self.runnig_location+r"/results_hanggai"+self.LLM_model+r".pkl")

        # 然后每一步人工批改一下：
        for i in range(index_start, self.prompts.num+1):
            timu = self.prompts.get_timu_index(index=i)
            daan = self.prompts.get_daan_index(index=i)
            cankao_daan = self.prompts.get_cankao_daan_index(index=i)
            print("第{}题：".format(i))
            print(timu)
            print("\nLLM答案：\n " + daan)
            print("\n参考答案：\n " + cankao_daan)
            # 输入判断对错。
            TF=input("对错：")
            self.prompts.save_TF_index(index=i, TF=TF)

       # 然后把试卷保存一下。
        self.prompts.save_results(self.runnig_location+r"/results_hanggai"+self.LLM_model+r".pkl")

    def hanggai_check(self):
        location = self.runnig_location+r"/results_hanggai"+self.LLM_model+r".pkl"
        # 把卷子读取进来得了几分。# 先把做完批改完的试卷读取进来。
        self.prompts.load_results(location)

        self.prompts.get_overall_performance(location)

if __name__ == "__main__":
    runner = auto_run(model="hanggai")
    flag = 2
    if flag == 0:
        runner.run()
    elif flag ==1:
        runner.hanggai_pigai(index_start=1)
    elif flag ==2:
        runner.hanggai_check()

    