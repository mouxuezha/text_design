# https://www.xuetangx.com/learn/BUAA08201000711/BUAA08201000711/19317637/exercise/42949890?channel=i.area.course_list_all
# 学堂在线上面的航空航天技术课程，的技术部分的课后练习题拿，拿过来了。
import pickle,os 
import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from prompts.base_prompts import base_prompot

class hanggai_prompot(base_prompot):
    def __init__(self) -> None:
        super.__init__()
        self.name = r"auto_test/hanggai_prompot.pkl"
        self.get_neirong()
        pass

    def get_neirong(self):
        # 直接硬编码在这了，反正后面也没有什么太多的修改需求。

        timu_single  = "目前计算机和计算技术在飞机设计制造过程中所占的工作量已达到多少？"
        daan_single = "70%以上"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "空气动力学发展的主要分支包括哪些？"
        daan_single = "计算空气动力学、实验空气动力学、飞行空气动力学"
        self.get_neirong_single(timu_single,daan_single)      

        timu_single  = "CFD可以在哪些方面取代风洞实验？"
        daan_single = "常规风洞实验"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "飞机气动设计方法和流程主要包括哪些？"
        daan_single = "概念/初步设计阶段，风洞试验阶段，飞行试验阶段"
        self.get_neirong_single(timu_single,daan_single)            

        timu_single  = "湍流阻力大约是层流阻力的多少倍？"
        daan_single = "5至7倍"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "机翼层流控制的主要方法包括哪些？"
        daan_single = "改变机翼构型、在机翼上表面进行吸气、在机翼前缘进行吸气"
        self.get_neirong_single(timu_single,daan_single)  
        
        timu_single  = "关于涡流发生器的四种说法中错误的是哪个？说法1，形状像小三角形的翼片。说法2，可以抑制机翼气流分离、减小阻力。说法3，可以增加机翼升力，说法4，布置在发动机短舱从而抑制短舱的气流分离。"
        daan_single = "布置在发动机短舱从而抑制短舱的气流分离。"
        self.get_neirong_single(timu_single,daan_single)          

        timu_single  = "抑制气流分离的方法主要有哪些？"
        daan_single = "采用涡流发生器、在气流分离部位进行吹气控制、在机翼前缘发射高速气流、控制翼型迎角"
        self.get_neirong_single(timu_single,daan_single)                 

        timu_single  = "前缘涡在机翼上产生的涡升力可占到总升力的多少？"
        daan_single = "20%以上"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "翼梢尾涡会产生哪些影响？"
        daan_single = "影响机场效率、影响飞机起降效率、增加诱导阻力"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "在机体的噪声控制方面，属于被动控制的措施有哪些？"
        daan_single = "加装整流罩"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "飞机机体噪声的主要噪声源有哪些？"
        daan_single = "增升装置的气动噪声、起落架气动噪声、机体部件之间的气动干扰噪声"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "适合于高超声速飞机的发动机是哪种？"
        daan_single = "冲压式发动机"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "采用涡轮风扇发动机的飞机包括？"
        daan_single = "第三代飞机、第四代飞机"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "活塞式发动机的做功行程是？"
        daan_single = "燃烧"
        self.get_neirong_single(timu_single,daan_single)  

        timu_single  = "活塞式发动机的主要特点包括？"
        daan_single = "低速飞行时效率高、飞行速度超过700-800km/h后推进效率急剧降低、主要用于小型和低速飞机"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "空气喷气发动机的最基本类型是？"
        daan_single = "涡轮喷气发动机"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "涡轮喷气发动机的核心机包括？"
        daan_single = "压气机、涡轮、燃烧室"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "目前性能较好的民用涡轮风扇发动机的涵道比已经接近多少？"
        daan_single = "10"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "战斗机采用的涡轮风扇发动机的特点为？"
        daan_single = "涵道比低、有加力燃烧室、发动机装在机体内"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "第一代、第二代、第三代飞机中哪代具有推力矢量技术？"
        daan_single = "第四代"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "能够实现推力矢量技术的发动机喷管包括？"
        daan_single = "二元推力矢量喷管、轴对称推力矢量喷管、安装折流板、可转向垂直起降喷管"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "涡轮螺桨发动机螺旋桨产生的拉力或推力占总推力的多少比例？"
        daan_single = "90%"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "涡轮轴发动机与活塞式发动机相比主要优点包括？"
        daan_single = "功率大、质量轻、噪音小"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "冲压发动机对空气的压缩是通过什么部件完成的？"
        daan_single = "进气道"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "冲压发动机对空气的压缩是通过什么部件完成的？"
        daan_single = "进气道"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "冲压发动机的特点包括哪些？"
        daan_single = "低速飞行时效率低、高速飞行时进气压缩性能好、通常和其他类型发动机组合使用"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "美国的“太阳神”无人机共有多少个螺旋桨？"
        daan_single = "14个"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "电动力装置的电力来源主要来自于？"
        daan_single = "太阳能电池、蓄电池、燃料电池"
        self.get_neirong_single(timu_single,daan_single) 
        
        # 从这里开始是航天的了。
        timu_single  = "火箭发动机的推重比可达？"
        daan_single = "80-120"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "火箭发动机和航空发动机相比其优点包括哪些？"
        daan_single = "推力不受飞行姿态的影响、推力更大、推重比更高"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "以下哪种发动机属于化学火箭发动机？太阳能火箭发动机，电火箭发动机，固-液混合火箭发动机，核火箭发动机"
        daan_single = "固-液混合火箭发动机"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "非化学能火箭发动机被加速喷出的工质通常采用哪些物质？"
        daan_single = "氢、氦、氩、氙"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "控制液体火箭发动机推力大小的最关键的部分是？"
        daan_single = "流量控制活门"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "液体火箭发动机的推进剂输送系统包括哪些类型？"
        daan_single = "泵压式、挤压式"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "固体火箭发动机的推力大小可以采用什么进行控制？"
        daan_single = "设计不同的药柱形状"
        self.get_neirong_single(timu_single,daan_single) 

        timu_single  = "关于“民兵”Ⅲ导弹，以下说法正确的是？洲际导弹，弹道导弹，第三级采用的是固体火箭发动机，射程超过12000公里"
        daan_single = "洲际导弹，弹道导弹，第三级采用的是固体火箭发动机，射程超过12000公里"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "当双向摆动喷管的上下两个喷管同时向上或向下偏转时，可以控制火箭的什么运动？"
        daan_single = "俯仰"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "火箭发动机的推力方向可以采用什么方法进行控制？"
        daan_single = "二次喷射技术、摆动喷管、燃气舵"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "固体火箭发动机和液体火箭发动机相比的主要优势为？"
        daan_single = "结构简单、使用方便"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "固体火箭发动机通常用在哪些方面？"
        daan_single = "探空火箭、空空导弹、火箭助推器"
        self.get_neirong_single(timu_single,daan_single)


        timu_single  = "化学能火箭发动机的比冲最高可达多少？"
        daan_single = "5000m/s"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "火箭发动机的主要性能指标包括哪些？"
        daan_single = "推力、冲量、比冲"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "液体火箭发动机、固体火箭发动机、核火箭发动机和离子火箭发动机中，比冲最高的是哪种？"
        daan_single = "离子火箭发动机"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "电火箭发动机按加速工质的方式不同，可分为哪些类型？"
        daan_single = "电热推进、静电推进、电磁推进"
        self.get_neirong_single(timu_single,daan_single)
        
        # 对应课件里的第八章
        timu_single  = "两个主起落架位于飞机重心后面，前面有一个前起落架，这种起落架布局形式是？"
        daan_single = "前三点式起落架"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "起落架的作用包括哪些？"
        daan_single = "重要的承力部件，吸收着陆冲击能量，地面滑跑、操纵"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "航空母舰起飞甲板的长度一般是多长？"
        daan_single = "100米"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "关于襟翼以下描述正确的是？仅在飞机起飞时打开，仅在飞机着陆时打开，在飞机起飞和着陆时都打开，是飞机的增升装置"
        daan_single = "在飞机起飞和着陆时都打开，是飞机的增升装置"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "仪表着陆系统的指点信标是用来为飞机提供什么信息的？"
        daan_single = "距机场的距离"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "飞机着陆过程中可以采取的辅助着陆措施包括哪些？"
        daan_single = "打开阻力伞，放下襟翼，拦阻钩拦阻，采用反推力装置"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "美国波音公司的“扫描鹰”无人机采用的是什么发射方式。？"
        daan_single = "弹射发射"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "无人机的起飞或发射方式包括哪些？"
        daan_single = "零长度发射、载机空中发射、垂直起飞、人力投掷"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "无人机拦阻网回收触网时的过载一般不能大于多少？"
        daan_single = "6g"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "无人机的着陆和回收方式包括哪些？"
        daan_single = "直升机空中回收，天钩回收，伞降回收，水平滑行着陆"
        self.get_neirong_single(timu_single,daan_single)
        
        # 第九章了，航天发射的
        timu_single  = "确定“哈雷彗星”探测器的发射窗口时适合选择什么发射窗口？"
        daan_single = "年发射窗口"
        self.get_neirong_single(timu_single,daan_single)
        
        timu_single  = "确定发射窗口时需要考虑的因素包括哪些？"
        daan_single = "地面观察和跟踪条件，在轨运行要求，落地点限制"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "航天器的入轨点是指什么？"
        daan_single = "进入轨道的初始位置"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "航天器的发射轨道包括哪些？"
        daan_single = "直接入轨，滑行入轨，过渡入轨"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "航天器返回时的“黑障区”位于航天器返回轨道的什么阶段？"
        daan_single = "再入段"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "关于航天器返回时的再入角描述正确的是哪些？再入角是航天器飞行速度方向与当地水平线之间的夹角，再入角太小可能会因为高温被烧毁，再入角太大可能会擦过大气层飞走，再入角太大可能会因为高温被烧毁"
        daan_single = "再入角是航天器飞行速度方向与当地水平线之间的夹角，再入角太大可能会因为高温被烧毁"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "航天器返回时制动过载最大的再入方式是什么？"
        daan_single = "纯弹道式"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "采用半弹道式再入方式再入的航天器包括哪些？"
        daan_single = "神舟系列飞船，联盟号飞船"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "美国的“勇气号”火星探测器采用的是什么软着陆方式？"
        daan_single = "气囊弹跳式"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "采用着陆腿式软着陆的月球探测器包括哪些？"
        daan_single = "嫦娥三号，阿波罗飞船"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "V-2导弹是一种什么导弹？"
        daan_single = "弹道式"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "导航可以提供的信息包括哪些？"
        daan_single = "位置信息，方位信息，速度信息"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "惯性导航的最大优点是什么？"
        daan_single = "完全自主导航"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "以下什么技术导航属于无线电导航？DME测距机，INS导航，全向信标导航，DVOR导航"
        daan_single = "DME测距机，全向信标导航，DVOR导航"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "世界四大卫星导航系统中，具有短报文通信功能的导航系统是？"
        daan_single = "北斗导航"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "卫星导航系统一般包括哪几大组成部分？"
        daan_single = "卫星系统，地面站组，用户设备"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "景象匹配导航属于几维匹配导航？"
        daan_single = "二维匹配导航"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "图像匹配导航技术较适合于什么阶段？"
        daan_single = "末制导，组合导航，地形跟踪和地形回避"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "中国的红旗-2（HQ-2）防空导弹属于什么制导？"
        daan_single = "非瞄准线指令制导"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "以下关于遥控制导的导弹描述正确的是？设备简单，需要知道目标的信息，机动性强，可以根据指令随时改变飞行轨迹"
        daan_single = "设备简单，机动性强，可以根据指令随时改变飞行轨迹"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "电视寻的制导的核心部件是什么？"
        daan_single = "电视自动寻的头"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "主动雷达寻的制导的特点是？"
        daan_single = "具有发射后不管的能力，自带雷达和天线，受天气和时间影响小，抗干扰能力强"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "目前我国飞得最远的航天器是？"
        daan_single = "嫦娥二号"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "中国的航天测控系统主要由哪些部分组成？"
        daan_single = "地面控制中心，测控站，海上测量船，天基中继卫星"
        self.get_neirong_single(timu_single,daan_single)
        
        # 11章了，飞行器隐身技术
        timu_single  = "作战平台采用隐身技术后，平台RCS降低10dB，则对方雷达探测发现平台的距离可降低约多少？"
        daan_single = "44%"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "可能被对方传感器探测到的特征信号包括哪些？"
        daan_single = "雷达信号，红外信号，声音信号，辐射信号"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "F-22属于第几代隐身飞机？"
        daan_single = "3"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "以下哪些飞机曾采用过隐身措施？F-117，U-2，SR-71，F-22"
        daan_single = "F-117，U-2，SR-71，F-22"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "雷达隐身中RCS是指？"
        daan_single = "雷达散射截面"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "以下飞机头向的RCS≤0.05的飞机包括哪些？幻影2000，B-2，F-22，F-117"
        daan_single = "B-2，F-22，F-117"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "外形隐身，材料隐身，阻抗加载，结构隐身中属于主动雷达隐身技术是？"
        daan_single = "阻抗加载"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "减缩目标RCS的技术途径主要包括哪些？"
        daan_single = "有源对消技术，外形隐身，采用隐身材料，等离子体技术"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "红外辐射本质上是什么辐射？"
        daan_single = "电磁辐射"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "红外隐身技术的主要目标就是减缩飞行器平台的什么红外辐射能量？"
        daan_single = "中红外，远红外"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "对于飞行器而言，不能被射频探测系统发现的射频信号包括哪些？"
        daan_single = "红外信号"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "射频探测系统对飞行器的威胁包括哪些？"
        daan_single = "反辐射导弹，波达方位定位器，雷达告警接收机，电子对抗设备"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "人耳可听到的声波的频率范围是？"
        daan_single = "20Hz-20000Hz"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "飞行器声学隐身的主要技术包括哪些？"
        daan_single = "避免表面空腔，降低发动机排气速度，采用整流技术"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "下列关于可见光隐身的主要技术途径描述不正确的是？尽量在云层内飞行，采用电致变色材料，设计亮度和颜色可调的蒙皮，利用烟幕遮挡和伪装"
        daan_single = "尽量在云层内飞行"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "光学隐身技术是武器平台规避什么的隐身技术？"
        daan_single = "可见光探测，肉眼可见，望远镜观测，激光仪器探测"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "星敏感器，成像光谱仪，姿态控制发动机，太阳能帆板中属于“嫦娥一号”有效载荷的是？"
        daan_single = "成像光谱仪"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "空间探测器对星球的探测方式包括哪些？"
        daan_single = "环绕探测，取样返回，近旁掠过，实地探测"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "宇宙飞船一般由哪几大部分组成？"
        daan_single = "返回舱，轨道舱，服务舱"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "载人飞船的核心舱是？"
        daan_single = "返回舱"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "截至到目前为止，世界上一共发射了几个空间站？"
        daan_single = "10"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "空间站一般由几大部分组成？"
        daan_single = "工作舱，生活舱，过渡舱"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "美国的航天飞机一共装了几台主发动机？"
        daan_single = "3台"
        self.get_neirong_single(timu_single,daan_single)

        timu_single  = "航天飞机一般由哪几大部分组成？"
        daan_single = "火箭助推器，外挂储箱，轨道器"
        self.get_neirong_single(timu_single,daan_single)

    def get_neirong_single(self,timu,neirong):
        num_single = len(self.timu_dic) + 1
        timu_dict_single = {"题目":timu,"参考答案":neirong,"答案":"void","对错":"None"}
        self.timu_dic[str(num_single)] = timu_dict_single   

if __name__ == "__main__":
    hanggai = hanggai_prompot()