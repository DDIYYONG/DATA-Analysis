#1994년 우승시즌과 2008년 꼴등시즌의 팀내 상위 war 선수들 수치비교해보자
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import font_manager, rc
from matplotlib.offsetbox import AnchoredText

font_path = "C:/Windows/Fonts/NGulim.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv("자료실/엘지트윈스비교.csv")
# print(df)
f, ax = plt.subplots(figsize=(7,8))
anchored_text = AnchoredText("war: 대체 수준 대비 승리 기여", loc=1)
ax.add_artist(anchored_text)

plt.subplots_adjust(top=0.90)
sb.violinplot(x='시즌',y='war',data = df)
plt.xlabel("시즌",fontsize = 14)
plt.ylabel("war",fontsize = 14)
mybox={'facecolor':'white','edgecolor':'k','boxstyle':'round'}
plt.text(10,2008,'dd',bbox=mybox)
plt.suptitle("war 분포도",fontsize= 20)
plt.show()