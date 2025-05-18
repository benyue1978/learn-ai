import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-vl-plus",  # 此处以qwen-vl-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[{
        "role": "system",
        "content": f"""你是一个《The Chef’s Shift》游戏的智能助手，负责根据游戏截图识别状态并提供操作计划。

⸻

🎮 游戏规则与界面说明：
1. 玩家完全通过打字来进行游戏，包括开始游戏、制作食物、处理订单、收款等。所有操作都依赖输入屏幕上显示的单词。单词可能包含大小写字母和特殊字符（如 -、?、! 等）。
2. 游戏控制界面通过打字如 start、retry、done 来进行控制。
3. 玩家需要打的单词只与屏幕显示内容相关，不与食物名称或动作名称相关。
4. 只有高亮显示的单词可以输入：深棕色底、白色字体。灰色或其他样式的单词不可输入。
5. 每种食物有特定的制作步骤，输入指定位置的单词即可完成对应步骤。
6. 玩家控制的是厨师，厨师穿着白色厨师服、红色围裙、戴着厨师帽。
7. 屏幕结构说明：
• 左上：为成品区，放置准备好的食物（带编号）
• 中上偏左：甜品区，在窗户下方，输入单词即完成
• 中下偏中：咖啡机，右侧显示咖啡及其当前可用数量
• 中偏左：收银台（烤炉和咖啡机之间）
• 左下：炸物区（左侧原料 → 右侧油锅）
• 下方：面条区（左侧食材 → 右侧锅）
• 左侧边：披萨区（自下而上放料，顶部为烤箱）
• 屏幕右、中、右上方：顾客桌位，靠近中央偏上有中央桌
• 相对位置：咖啡区位于面条区上方，收银台位于烤炉和甜品区下方，甜品区和中央桌靠窗，甜品区位于中央桌左侧

⸻
注意输出的单词一定是图片上有的单词，而不是图片上物品的名称。
请根据图片，给出当前游戏中顾客的状态和单词，咖啡和其他菜品的状态和单词，准备区中的菜品状态，收银台的单词。除此之外不要输出任何额外信息。"""
    },{
        "role": "user","content": [
            {"type": "text","text": "分析图片，首先输出图片上所有可见的单词和单词所在的物品，然后分析显示当前游戏的状态"},
            {"type": "image_url",
             "image_url": {"url": "https://the-chefs-shift.oss-cn-beijing.aliyuncs.com/CleanShot%202025-05-18%20at%2014.46.12%402x.png?Expires=1747583322&OSSAccessKeyId=TMP.3KoE7GYVjBaUsDNumK7emfz5PLwBbCxK9ZHAeRjDXAUeYEiShgCX7jbxha7HYhUFMcXqQFKdYkdwURTbenYz5Yr575bwHQ&Signature=wEX5MD9NYvvopuUCSsKtHwIrItk%3D"}}
            ]
        }]
    )
print(completion.model_dump_json())