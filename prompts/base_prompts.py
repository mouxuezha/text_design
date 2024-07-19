import pickle,os 

class base_prompot():
    def __init__(self):
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
        
PROMPT_TEMPLATES = {
        "llm_chat": {
            "default":
                '{{ input }}',

            "with_history":
                'Answer my questions considering the coversation history.'
                'If you do not know the answer, just say do not know. \n\n'
                'Current conversation:\n'
                '{history}\n',
                
            "embrace":
                '请作为兵棋推演游戏的玩家，设想一个陆战作战场景。'
                '我方为红方，拥有坦克、步兵战车、自行迫榴炮、无人突击车和无人机、导弹发射车等装备，步兵下车后作战，'
                '我方需要攻取位于经纬度坐标(2.7100,39.7600)的夺控点，要将陆战装备移动到夺控点处并消灭夺控点附近敌人，地图范围为经度2.6000到2.8000，纬度范围为39.6500到39.8500，导弹发射车不能机动。地图西北方向为海洋，其余部分为陆地。陆地中间部分为山区，装备单位经过山区会由于坡度地形因素，导致行进速度减慢，夺控点周围是一片平原。'
                '每隔一定步数，我将告诉你敌我态势和其他信息，并由你来尝试生成作战指令。\n'
                '在生成指令时，可以考虑历史态势和指令，下面是我们的对话历史：\n'
                '{history}'
                '请按照以下格式给出作战指令。进攻指令：[move, obj_id , x=int, y=int], 如坦克mbt_1进攻坐标为(2.7100, 39.7600)，则指令为[move, obj_id=mbt_1, x=2.7100, y=39.7600] \n停止指令：[stop, obj_id], 如坦克mbt_1停止当前行动，则指令为[stop, obj_id=mbt_1] \n步兵下车指令: [off_board, obj_id],如步战车ifv_1内步兵立刻下车,则指令为[off_board, obj_id=ifv_1]',
        
            "jieshuo_embrace":
                '请作为解说员，解说一场兵棋推演比赛，尽量讲清楚双方作战过程和行动逻辑。场景如下：'
                '红方拥有坦克、步兵战车、自行迫榴炮、无人突击车和无人机、导弹发射车等装备，步兵下车后作战，'
                '红方需要攻取位于经纬度坐标(2.7100,39.7600)的夺控点，要将陆战装备移动到夺控点处并消灭夺控点附近敌人，地图范围为经度2.6000到2.8000，纬度范围为39.6500到39.8500，导弹发射车不能机动。地图西北方向为海洋，其余部分为陆地。陆地中间部分为山区，装备单位经过山区会由于坡度地形因素，导致行进速度减慢，夺控点周围是一片平原。'
                '蓝方则试图阻击，拥有更多的步兵力量和反导能力。'
                '每隔一定步数，我将告诉你红蓝态势和其他信息，并由你来生成解说词\n'
                '在生成指令时，可以考虑历史态势和指令，下面是我们的对话历史：\n'
                '{history}',
            #
            # "embrace": embrace_lang + '在生成指令时，可以考虑历史态势和指令，下面是我们的对话历史：\n {history}'
            "hanggai_embrace":
                '接下来我会问你一些航空航天领域的基础内容，请根据你的知识给出正确回答。'
                '{history}'
        
        }
    }
