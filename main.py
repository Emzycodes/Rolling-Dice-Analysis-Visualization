from die import Die
from plotly import offline
from plotly.graph_objects import Bar, Layout

die1 = Die() # sets the instance of the Die class
die2 = Die()
 
results = []
for rolls in range(1000):
    result = die1.roll_die() + die2.roll_die()
    results.append(result)


# Analyze the results
frequencies = []
max_number = die1.sides + die2.sides
for value in range(2,max_number +1):
    frequency = results.count(value)
    frequencies.append(frequency)

# plot the graph
x_values = list(range(2,max_number +1))
data = [Bar(x=x_values, y=frequencies)]
x_axix_config = {'title': 'Result', 'dtick': 1}
y_axix_config = {'title' : 'Frequency Of Result'}
my_layout = Layout(title = 'Results of rolling two Dice 1000 times', xaxis = x_axix_config,
                    yaxis = y_axix_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6.html')


