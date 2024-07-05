# 这个是来一个做题流程，每个题都问一下大模型，然后让它返回东西，然后存起来

import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_communication.model_comm_langchain import ModelCommLangchain