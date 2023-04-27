#홈런 대비 삼진개수
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import font_manager, rc
import matplotlib.ticker as mticker

font_path = "C:/Windows/Fonts/NGulim.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
df = pd.read_csv("자료실/홈런대비삼진.csv")
x=df['삼진']
y=df['홈런']

z= np.polyfit(x,y,1)
p= np.poly1d(z)
plt.subplots_adjust(top=0.87)
plt.scatter(x,y,)
plt.plot(x,p(x),'-',c='blue')
plt.xlabel("삼진(개)",fontsize = 14)
plt.ylabel("홈런(개)",fontsize = 14)
plt.suptitle("홈런대비 삼진수",fontsize = 20)
plt.show()