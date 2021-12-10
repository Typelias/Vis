from bokeh.plotting import figure, show
import pandas as pd

dataset = pd.read_csv('Swedish_Population_Statistics.csv')

print(dataset)

region = dataset['region']
y2012 = dataset['2012']

p = figure(title="Simple line example", x_axis_label="Population", y_range=region)
#p.line(x, y, legend_label="Temp.", line_width=2)
p.hbar(y=region, right=y2012)

#show(p)