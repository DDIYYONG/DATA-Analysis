#투고탸저의 2022시즌 타율밀집도와 타고투저의 2018시즌 타율밀집도 비교
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from matplotlib import font_manager, rc
import matplotlib.ticker as mticker

font_path = "C:/Windows/Fonts/NGulim.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
df = pd.read_csv("자료실/타율.csv")

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.subplots_adjust(wspace=0.5)
plt.subplots_adjust(top=0.8)
sb.distplot(df['2018시즌타율'])
sb.distplot(df['2022시즌타율'])
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.3f'))
plt.xlabel("타율",fontsize = 14)
plt.ylabel("")
plt.title("타율 밀집도")
plt.legend(labels=["2018시즌타율","2022시즌타율"],title = "시즌별 타율 밀집도")

plt.subplot(1,2,2)
plt.plot(df['월별'],df['오지환'],marker='o',c='red')
plt.plot(df['월별'],df['김현수'],marker='o',c='blue')
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.3f'))
plt.xlabel("월",fontsize = 14)
plt.ylabel("타율",fontsize = 14)
plt.ylim([0.150,0.400])
plt.title("월별 타격 사이클")
plt.legend(labels=["오지환 시즌타율","김현수 시즌타율"],title = "월별 선수타율")

plt.suptitle("환경에 의한 타율변화",fontsize = 20)



plt.show()