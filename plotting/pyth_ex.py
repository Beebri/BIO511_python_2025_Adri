#3.1==========================================================================
import seaborn as sns
penguins = sns.load_dataset("penguins")
penguins = penguins.dropna()
print(penguins)#
#scatter plot matplotlib
import matplotlib.pyplot as plt
plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'],)
plt.title('Flipper Length vs Body Mass (Penguins)')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.savefig('penguins_matplotlib.png')
#Scatter plot plotly
import plotly.express as px
fig = px.scatter(
    penguins,
    x='flipper_length_mm',
    y='body_mass_g',
    title='Flipper Length vs Body Mass (Penguins)')
fig.write_html('penguins_plotly.html')
#scatter plot seaborn
plt.figure(figsize=(6,4))
sns.scatterplot(
    data=penguins,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species'
)
plt.title('Flipper Length vs Body Mass (Penguins)')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.savefig('penguins_seaborn.png')
#plotline plot
from plotnine import ggplot, aes, geom_point, ggtitle 
from plotnine.ggplot import ggsave
p = (ggplot(penguins, aes(x='flipper_length_mm', y='body_mass_g', color='species'))
    + geom_point()
    + ggtitle('Flipper Length vs Body Mass (Penguins)'))

ggsave(p,'penguins_plotnine.png')
#plot = last_plot())
#3.2==========================================================================
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(data=penguins, x='bill_length_mm')
plt.title('Distribution of Penguin Bill Lengths')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Count')
plt.savefig('penguins_bill_length_histogram.png')