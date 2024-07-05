import pickle,os 

class base_prompot():
    def __init__(self) -> None:
        self.timu_dic = {} 
        self.name = r"auto_test/base_prompot.pkl"
        pass

    def save_results(self):
        pickle.dump(self.timu_dic,open(self.name,"wb"))

    def load_results(self):
        self.timu_dic = pickle.load(open(self.name,"rb"))
    
    def set_location(self,name):
        self.name = name
        if os.path.exists(self.name):
            pass
        else:
            raise Exception("base_prompot:文件不存在")