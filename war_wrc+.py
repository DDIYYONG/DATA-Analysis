#1994~2022년 최종순위와 war,wrc+의 관계를 알아보자
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
from matplotlib.patches import Ellipse, Polygon

font_path = "C:/Windows/Fonts/NGulim.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv("자료실/엘지트윈스.csv")

fig, ax = plt.subplots()
fig.set_size_inches(25, 12)
ax.plot(df['연도'], df['war'], linewidth = 4, alpha = 0.5, color = 'gray')
ax.plot(df['연도'], df['war'], linewidth = 4, color = '#1D2238')
ax.scatter(df['연도'], df['war'], linewidth = 4, color = '#1D2238', marker = 'o', s = 1000)
ax.plot(df['연도'], df['wrc+'], linewidth = 4, alpha = 0.5, color = 'red')
ax.plot(df['연도'], df['wrc+'], linewidth = 4, color = '#7d3848')
ax.scatter(df['연도'], df['wrc+'], linewidth = 4, color = '#7d3848', marker = 'o', s = 1000)
ax.set_ylim([0, 140])
ax2 = ax.twinx()
ax2.plot(df['연도'],df['최종순위'],linewidth = 4, alpha = 0.5, color = 'red')
ax2.set_ylim([-10, 18])
fig.gca().invert_yaxis()
ax.grid(True, axis = 'y')
ax.set_title('엘지트윈스 (1994 - 2022)', fontsize = 20, fontweight='bold')
for i in range(len(df['연도'])):
    ax.text(df['연도'][i], df['war'][i], df['연도'][i], color = 'white', verticalalignment = 'center' , horizontalalignment = 'center' , fontweight='bold', fontsize = 15)
for i in range(len(df['연도'])):
    ax.text(df['연도'][i], df['wrc+'][i], df['연도'][i], color = 'white', verticalalignment = 'center' , horizontalalignment = 'center' , fontweight='bold', fontsize = 15)
ax.tick_params(bottom = False, labelbottom = False)
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax.tick_params(axis = 'y', labelsize = 15)
ax.spines['left'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['right'].set_linewidth(0)
ax.spines['bottom'].set_linewidth(1)
ax.spines['bottom'].set_color('#BFBFBF')
ax.legend(labels=["wrc+","war"])
ax2.legend(labels=["순위권"],loc='upper right', bbox_to_anchor=(1.001, 0.94))




plt.show()