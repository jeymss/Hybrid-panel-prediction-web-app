# -*- coding: utf-8 -*-
"""Warriors 2.1 Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VaESE6fhBt-iY0UmcjQyx70FQwTDsxD

```
# This is formatted as code
```
<h1>Implementation of Internet of Things in Developing Hybrid Energy Harvesting System </h1>
<h3><p>ADRIAN I. DELA CRUZ </p>
<p>JAMES FREDERIC B. DULO </p>
<p>GELAN M. NICOLAN </p>
<p>ARVENELL ABAD </p>
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")
# %matplotlib inline

#Train-Test Split Module
from sklearn.model_selection import train_test_split
#Linear Regression Algorithm from sklearn
from sklearn import linear_model
#Metrics to measure model performance
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
#Standard Scaler for Standardization
from sklearn.preprocessing import StandardScaler
#warnings
import warnings
warnings.filterwarnings('ignore')

#Load the dataset
df = pd.read_csv("Hybrid Panel testing.csv", index_col=0)
#Display the dataset
df

#Preprocessing
df = df.drop(['Average Solar\nVoltage\n(V)','Average Solar\nCurrent (A)','Average Piezo\nVoltage\n(V)','Average Piezo\nCurrent \n(A)'], axis=1)

df.describe()

#check for null values
df.isnull().sum()

#Get the correlation of the attributes
corr = df.corr()
corr

"""
<h2> Model for Solar Power Output prediction. </h2>


"""

plt.scatter(df['Average\nHeat Index\n(°C)'], df['Average Solar\nPower\n(W)'], color='red')
plt.title(' Heat index Vs Solar Power', fontsize=14)
plt.xlabel('Solar Power', fontsize=14)
plt.ylabel('Heat index', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['Average\nHumidity\n(%)'], df['Average Solar\nPower\n(W)'], color='red')
plt.title(' Humidity Vs Solar Power', fontsize=14)
plt.xlabel('Solar Power', fontsize=14)
plt.ylabel('Humidity', fontsize=14)
plt.grid(True)
plt.show()

#Visualize Correlation
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr,cmap=cmap, vmax=.9, square=True, linewidths=.5, ax=ax)
#add title
ax.set_title("Correlation Heatmap")

#Split the dataset to training and testing set
#Lets consider TV and radio to determine the advertising sales
df_train, df_test = train_test_split(df, test_size=0.25, random_state=35)

x_train = df_train[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_train = df_train['Average Solar\nPower\n(W)']

x_test = df_test[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_test = df_test['Average Solar\nPower\n(W)']

#Instantiate the Scaler
scaler = StandardScaler()
#Fit to the TRAIN set
scaler.fit(x_train)
#Apply to the TRAIN set
x_train_s = scaler.transform(x_train)
#Apply to the TEST set
x_test_s = scaler.transform(x_test)

x_train_s
df.head()

#Instantiate the Linear Regression Algorithm
linreg = linear_model.LinearRegression()
#Train the Model
linreg.fit(x_train_s, y_train)

#Verifying Coefficient
pd.DataFrame(linreg.coef_, index=x_train.columns, columns=['Coef'])

# Validate the Model
# Predict the values
y_pred = linreg.predict(x_test_s)
y_pred

#PERFORMANCE METRICS

df_results = pd.DataFrame(y_test)
df_results["Predicted Solar Power"] = y_pred
df_results

# Create a new dataframe containing the predictor variables, test results, and predicted results
results_df = pd.DataFrame({'Heat Index (°C)': x_test['Average\nHeat Index\n(°C)'],
                           'Humidity (%)': x_test['Average\nHumidity\n(%)'],
                           'Actual Solar Power (W)': y_test,
                           'Predicted Solar Power (W)': y_pred})
results_df

#Measure the performance of the model
r2 = r2_score(y_test, y_pred) * 100
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred) 
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(("r2: %.2f") %r2)
print(("mae: %.2f") %mae)
print(("mse: %.2f") %mse)
print(("rmse: %.2f") %rmse)

x_test.columns

#x_test.rename(columns={'Average\nHeat Index\n(°C)': 'Averageheatindex', 'Average\nHumidity\n(%)': 'Averagehumidity'})

#visualizing results
plt.scatter(y_test, y_pred, label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Ideal Predictions')
plt.xlabel('Actual Solar Power Values')
plt.ylabel('Predicted Solar Power Values')
plt.title('Linear Regression Results For Solar Power Prediction')
plt.legend(loc='lower right')
plt.rcParams['figure.figsize'] = (10, 10)
plt.show()

"""<h2> Model for Piezo Power Output Prediction </h2>

"""

plt.scatter(df['Average\nHeat Index\n(°C)'], df['Average Piezo\nPower\n(W)'], color='red')
plt.title(' Heat index Vs Piezo Power', fontsize=14)
plt.xlabel('Piezo Power', fontsize=14)
plt.ylabel('Heat index', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['Average\nHumidity\n(%)'], df['Average Piezo\nPower\n(W)'], color='red')
plt.title(' Humidity Vs Piezo Power', fontsize=14)
plt.xlabel('Piezo Power', fontsize=14)
plt.ylabel('Humidity', fontsize=14)
plt.grid(True)
plt.show()

#Split the dataset to training and testing set
#Lets consider TV and radio to determine the advertising sales
df_train2, df_test2 = train_test_split(df, test_size=0.25, random_state=35)

x_train2 = df_train2[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_train2 = df_train2['Average Piezo\nPower\n(W)']

x_test2 = df_test2[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_test2 = df_test2['Average Piezo\nPower\n(W)']

#Instantiate the Scaler
scaler2 = StandardScaler()
#Fit to the TRAIN set
scaler2.fit(x_train)
#Apply to the TRAIN set
x_train_s2 = scaler2.transform(x_train)
#Apply to the TEST set
x_test_s2 = scaler2.transform(x_test)

x_train_s2
df.head()

#Instantiate the Linear Regression Algorithm
linreg2 = linear_model.LinearRegression()
#Train the Model
linreg2.fit(x_train_s2, y_train2)

#Verifying Coefficient
pd.DataFrame(linreg2.coef_, index=x_train2.columns, columns=['Coef'])

# Validate the Model
# Predict the values
y_pred2 = linreg2.predict(x_test_s2)
y_pred2

df_results = pd.DataFrame(y_test2)
df_results["Predicted Solar Power"] = y_pred2
df_results

# Create a new dataframe containing the predictor variables, test results, and predicted results
results_df2 = pd.DataFrame({'Heat Index (°C)': x_test2['Average\nHeat Index\n(°C)'],
                           'Humidity (%)': x_test2['Average\nHumidity\n(%)'],
                           'Actual Piezo Power (W)': y_test2,
                           'Predicted Piezo Power (W)': y_pred2})
results_df2

#Measure the performance of the model
r22 = r2_score(y_test2, y_pred2) * 100
mae2 = mean_absolute_error(y_test2, y_pred2)
mse2 = mean_squared_error(y_test2, y_pred2) 
rmse2 = np.sqrt(mean_squared_error(y_test2, y_pred2))

print(("r2: %.2f") %r22)
print(("mae: %.2f") %mae2)
print(("mse: %.2f") %mse2)
print(("rmse: %.2f") %rmse2)

#visualizing results
plt.scatter(y_test2, y_pred2, label='Predicted vs Actual')
plt.plot([y_test2.min(), y_test2.max()], [y_test2.min(), y_test2.max()], 'r--', label='Ideal Predictions')
plt.xlabel('Actual Piezo Power Values')
plt.ylabel('Predicted Piezo Power Values')
plt.title('Linear Regression Results For Piezoelectric Power Prediction')
plt.legend(loc='lower right')
plt.rcParams['figure.figsize'] = (15, 15)
plt.show()

"""<h2> Prediction </h2>"""

# temperature = float(input('Enter temperature: '))
# humidity = float(input('Enter humidity: '))

# input_data = scaler.transform([[temperature, humidity]])
# predicted_power = linreg.predict(input_data)[0]
# predicted_power2 = linreg2.predict(input_data)[0]

# print('Predicted solar power:', predicted_power)
# print('Predicted Piezo power:', predicted_power2)

pip install gradio

# import gradio as gr

# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")

# def predict_power(temperature, humidity):
#     input_data = scaler.transform([[temperature, humidity]])
#     predicted_power = linreg.predict(input_data)[0]
#     predicted_power2 = linreg2.predict(input_data)[0]
#     return f'Predicted solar power: {predicted_power:.2f}\nPredicted Piezo power: {predicted_power2:.2f}'

# iface = gr.Interface(predict_power, [temperature, humidity], "text")
# iface.launch()

# import gradio as gr

# # Define input components
# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")

# # Define prediction function
# def predict_power(temperature, humidity):
#     input_data = scaler.transform([[temperature, humidity]])
#     predicted_power = linreg.predict(input_data)[0]
#     predicted_power2 = linreg2.predict(input_data)[0]
#     return f'Predicted solar power: {predicted_power:.2f}\nPredicted Piezo power: {predicted_power2:.2f}'

# # Define header and paragraph components
# header = "Solar and Piezo Power Predictor"
# paragraph = "This app predicts the solar and piezo power output based on the input temperature and humidity."

# # Create interface
# iface = gr.Interface(
#     predict_power, 
#     [temperature, humidity], 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
# )

# # Launch interface
# iface.launch()

# import gradio as gr

# # Define input components
# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")
# needed_power = gr.inputs.Number(label="Needed Power Output (in Watts)")

# # Define prediction function
# def predict_power(temperature, humidity, needed_power):
#     # Predict solar power
#     input_data = scaler.transform([[temperature, humidity]])
#     predicted_solar_power = linreg.predict(input_data)[0]
    
#     # Compute suggested solar panel dimensions
#     panel_length = round((needed_power / predicted_solar_power) ** 0.5, 2)
#     panel_width = round(panel_length * 1.6, 2)
    
#     # Predict piezo power
#     predicted_piezo_power = linreg2.predict(input_data)[0]
    
#     # Compute number of piezo electric transducers needed
#     num_piezo = round(needed_power / predicted_piezo_power)
    
#     return f'Predicted solar power: {predicted_solar_power:.2f}\nSuggested solar panel dimensions: {panel_length} x {panel_width}\nPredicted Piezo power: {predicted_piezo_power:.2f}\nNumber of piezo electric transducers needed: {num_piezo}'

# # Define header and paragraph components
# header = "Warriors Solar and Piezo Power Predictor App"
# paragraph = "Created by warriors group which are CpE students of Jose Rizal University. This app predicts the solar and piezo power output based on the input temperature and humidity. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs)."

# # Create interface
# iface = gr.Interface(
#     predict_power, 
#     [temperature, humidity, needed_power], 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
#     output_flag=None,
#     examples=[
#         ["65", "50", "5"],
#         ["30", "60", "8"],
#         ["35", "70", "12"]
#     ]
# )

# # Launch interface
# iface.launch()

# import gradio as gr

# # Define input components
# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")
# power = gr.inputs.Number(label="Needed Power Output (in Watts)")

# # Define prediction function
# def predict_power(temperature, humidity, power):
#     # Compute the area of the solar panel needed to generate the required power output
#     solar_panel_area = (power / 2) * 1.25
    
#     # Compute the number of piezoelectric transducers needed to generate the required power output
#     piezo_count = round(power / 0.1)
    
#     # Output the results
#     return f'For a needed power output of {power} watts:\n\n- Solar panel area needed: {solar_panel_area:.2f} sq. cm\n- Number of piezoelectric transducers needed: {piezo_count} pcs.'

# # Define header and paragraph components
# header = "Warriors Solar and Piezo Power Predictor App"
# paragraph = "Created by warriors group which are CpE students of Jose Rizal University. This app computes the area of the solar panel and the number of piezoelectric transducers needed to generate a specific power output based on the input temperature and humidity. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs)."

# # Create interface
# iface = gr.Interface(
#     predict_power, 
#     [temperature, humidity, power], 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
#     examples=[
#         ["65", "50", "1"],
#         ["30", "60", "3"],
#         ["35", "70", "5"]
#     ]
# )

# # Launch interface
# iface.launch()

# import gradio as gr

# # Define input components
# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")
# power = gr.inputs.Number(label="Needed Power Output (in Watts)")

# # Define prediction function
# def predict_power(temperature, humidity, power):
#     # Compute the length and width of the solar panel needed to generate the required power output
#     solar_panel_length = round((power / 2) / (5 * 2 / 100)) # Assume 5 watts per panel
#     solar_panel_width = round(solar_panel_length * 142 / 88) # Assume aspect ratio of 88:142
    
#     # Compute the number of piezoelectric transducers needed to generate the required power output
#     piezo_count = round(power / 0.1)
    
#     # Output the results
#     return f'For a needed power output of {power} watts:\n\n- Solar panel length needed: {solar_panel_length} cm\n- Solar panel width needed: {solar_panel_width} cm\n- Number of piezoelectric transducers needed: {piezo_count} pcs.'

# # Define header and paragraph components
# header = "Warriors Solar and Piezo Power Predictor App"
# paragraph = "Created by warriors group which are CpE students of Jose Rizal University. This app computes the length and width of the solar panel and the number of piezoelectric transducers needed to generate a specific power output based on the input temperature and humidity. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs)."

# # Create interface
# iface = gr.Interface(
#     predict_power, 
#     [temperature, humidity, power], 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
#     examples=[
#         ["65", "50", "1"],
#         ["30", "60", "3"],
#         ["35", "70", "5"]
#     ]
# )

# # Launch interface
# iface.launch()

# import math

# def compute_panel_size_and_piezos(power_output):
#     # Compute the solar panel size
#     panel_width = 88
#     panel_length = 142
#     panel_area = panel_width * panel_length
#     required_area = power_output / 2
#     scaling_factor = math.sqrt(required_area / panel_area)
#     panel_width *= scaling_factor
#     panel_length *= scaling_factor

#     # Compute the number of piezoelectric transducers needed
#     piezo_power = 0.5 / 12 # Each piezo can produce 0.5W / 12 = 0.0416666... W
#     piezo_count = math.ceil(power_output / piezo_power)

#     return (panel_width, panel_length, piezo_count)


# import gradio as gr

# # Define input components
# power_output = gr.inputs.Number(label="Power Output (in Watts)")

# # Define prediction function
# def predict_panel_and_piezos(power_output):
#     panel_width, panel_length, piezo_count = compute_panel_size_and_piezos(power_output)
#     return f'Solar panel size: {panel_width:.2f} x {panel_length:.2f} mm\nNumber of piezoelectric transducers needed: {piezo_count}'

# # Define header and paragraph components
# header = "Solar Panel and Piezoelectric Transducer Calculator"
# paragraph = "Enter the required power output and the calculator will estimate the size of the solar panel and the number of piezoelectric transducers needed to produce that amount of power."

# # Create interface
# iface = gr.Interface(
#     predict_panel_and_piezos, 
#     power_output, 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
#     examples=[
#         ["1"],
#         ["2"],
#         ["3"],
#         ["4"]
#     ]
# )

# # Launch interface
# iface.launch()

# import gradio as gr
# from gradio.mix import Parallel
# from gradio.interface import Panel

# # Define input components
# temperature = gr.inputs.Number(label="Temperature")
# humidity = gr.inputs.Number(label="Humidity")
# power_output = gr.inputs.Number(label="Power Output Needed (in watts)")

# # Define prediction functions
# def predict_power(temperature, humidity):
#     input_data = scaler.transform([[temperature, humidity]])
#     predicted_power = linreg.predict(input_data)[0]
#     predicted_power2 = linreg2.predict(input_data)[0]
#     return f'Predicted solar power in watts: {predicted_power:.2f}\nPredicted Piezo power in watts: {predicted_power2:.2f}'

# def predict_dimensions(power_output):
#     if power_output < 0.5:
#         piezo_count = round(power_output / 0.0417)
#         return f'Solar panel dimension: 88mm x 142mm\nNumber of Piezoelectric Transducers: {piezo_count} pcs'
#     else:
#         dimensions = [88, 142]
#         piezo_count = 12
#         while (power_output > 2):
#             dimensions[0] *= 2
#             dimensions[1] *= 2
#             power_output /= 4
#             piezo_count *= 4
#         piezo_count += round(power_output / 0.5)
#         return f'Solar panel dimension: {dimensions[0]}mm x {dimensions[1]}mm\nNumber of Piezoelectric Transducers: {piezo_count} pcs'
        

# # Define header and paragraph components
# header = "Warriors Solar and Piezo Power Predictor App"
# paragraph = "Created by warriors group which are CpE students of Jose Rizal University.This app predicts the solar and piezo power output based on the input temperature and humidity. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs) "

# # Create interface
# input_panel = Panel(temperature, humidity, name="Solar and Piezo Power Predictor")
# output_panel = Panel(predict_power, predict_dimensions, power_output, name="Predicted Output")

# iface = gr.Interface(
#     [input_panel, power_output, output_panel],
#     Parallel("text", "text"),
#     title=header,
#     description=paragraph,
#     examples=[
#         [["65", "50"], "0.5"],
#         [["30", "60"], "1"],
#         [["35", "70"], "3"]
#     ]
# )

# # Launch interface
# iface.launch()

import gradio as gr

# Define input components
temperature = gr.inputs.Number(label="Temperature")
humidity = gr.inputs.Number(label="Humidity")

# Define prediction function
def predict_power(temperature, humidity):
    input_data = scaler.transform([[temperature, humidity]])
    predicted_power = linreg.predict(input_data)[0]
    predicted_power2 = linreg2.predict(input_data)[0]
    return f'Predicted solar power in watts: {predicted_power:.2f}\nPredicted Piezo power in watts: {predicted_power2:.2f}'

# Define header and paragraph components
header = "Warriors Solar and Piezo Power Predictor App"
paragraph = "Created by warriors group which are CpE students of Jose Rizal University.This app predicts the solar and piezo power output based on the input temperature and humidity. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs) "

# Create interface
iface = gr.Interface(
    predict_power, 
    [temperature, humidity], 
    "text",
    title=header,
    description=paragraph,
    layout="vertical",
    output_flag=None,
    examples=[
        ["65", "50"],
        ["30", "60"],
        ["35", "70"]
    ]
)

# Launch interface
iface.launch()

# import gradio as gr

# # Define input component
# power_output = gr.inputs.Number(label="Power Output Needed (in watts)")

# # Define prediction function
# def predict_dimensions(power_output):
#     if power_output == 0:
#         piezo_count = 0
#         dimensions = [0, 0]
#     elif power_output < 0.5:
#         piezo_count = round(power_output / 0.0417)
#         dimensions = [88, 142]
#     else:
#         dimensions = [88, 142]
#         piezo_count = 12
#         while (power_output > 2):
#             dimensions[0] *= 2
#             dimensions[1] *= 2
#             power_output /= 4
#             piezo_count *= 4
#         piezo_count += round(power_output / 0.5)
#     return f'Solar panel dimension: {dimensions[0]}mm x {dimensions[1]}mm\nNumber of Piezoelectric Transducers: {piezo_count} pcs'
        

# # Define header and paragraph components
# header = "Warriors Solar and Piezo Power Predictor App"
# paragraph = "Created by warriors group which are CpE students of Jose Rizal University. This app predicts the solar panel dimension and the number of piezoelectric transducers needed to generate a specific power output based on the input power output needed. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs)."

# # Create interface
# iface = gr.Interface(
#     predict_dimensions, 
#     power_output, 
#     "text",
#     title=header,
#     description=paragraph,
#     layout="vertical",
#     examples=[
#         ["0.2"],
#         ["1"],
#         ["4"],
#         ["0"]
#     ]
# )

# # Launch interface
# iface.launch()

import gradio as gr

# Define input components
temperature = gr.inputs.Number(label="Temperature")
humidity = gr.inputs.Number(label="Humidity")
power_output = gr.inputs.Number(label="Power Output Needed (in watts)")

# Define prediction functions
def predict_power(temperature, humidity):
    input_data = scaler.transform([[temperature, humidity]])
    predicted_power = linreg.predict(input_data)[0]
    predicted_power2 = linreg2.predict(input_data)[0]
    return f'Predicted solar power in watts: {predicted_power:.2f}\nPredicted Piezo power in watts: {predicted_power2:.2f}'

def predict_dimensions(power_output):
    if power_output == 0:
        piezo_count = 0
        dimensions = [0, 0]
    elif power_output < 0.5:
        piezo_count = round(power_output / 0.0417)
        dimensions = [88, 142]
    else:
        dimensions = [88, 142]
        piezo_count = 12
        while (power_output > 2):
            dimensions[0] *= 2
            dimensions[1] *= 2
            power_output /= 4
            piezo_count *= 4
        piezo_count += round(power_output / 0.5)
    return f'Solar panel dimension: {dimensions[0]}mm x {dimensions[1]}mm\nNumber of Piezoelectric Transducers: {piezo_count} pcs'

# Define header and paragraph components
header = "Warriors Solar and Piezo Power Predictor App"
paragraph = "Created by warriors group which are CpE students of Jose Rizal University. This app predicts the solar and piezo power output, as well as the solar panel dimension and the number of piezoelectric transducers needed to generate a specific power output based on the input temperature, humidity and power output needed. Dependent and applicable for the prototype's specifications: Solar Panel (polycrystalline, 88*142mm, 5V, 2W) and Piezo Electric transducer (35mm, 12 pcs)."

# Define output components
output1 = gr.outputs.Textbox(label="Power Prediction")
output2 = gr.outputs.Textbox(label="Dimension and Piezo Count Prediction")

# Define prediction function that calls both prediction functions
def predict_all(temperature, humidity, power_output, model):
    if model == "Solar and Piezo Power Prediction":
        power_prediction = predict_power(temperature, humidity)
        return power_prediction, ""
    elif model == "Solar Panel Dimension and Piezo Count Prediction":
        dimension_prediction = predict_dimensions(power_output)
        return "", dimension_prediction
    elif model == "Both":
        power_prediction = predict_power(temperature, humidity)
        dimension_prediction = predict_dimensions(power_output)
        return power_prediction, dimension_prediction

# Create interface with tabs
iface = gr.Interface(
    predict_all,
    [temperature, humidity, power_output, gr.inputs.Dropdown(["Solar and Piezo Power Prediction", "Solar Panel Dimension and Piezo Count Prediction", "Both"], label="Model", default="Both")],
    [output1, output2],
    title=header,
    description=paragraph,
    layout="vertical",
    examples=[
        [65, 50, 1, "Both"],
        [0, 0, 0, "Solar Panel Dimension and Piezo Count Prediction"]
    ]
)

# Launch interface
iface.launch()

