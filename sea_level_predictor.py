import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6, label='Data Points')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Predict sea level rise in future years (e.g., from 1880 to 2050)
    future_years = range(1880, 2051)
    future_predictions = slope * future_years + intercept
    
    # Plot the line of best fit
    plt.plot(future_years, future_predictions, color='red', label='Line of Best Fit')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()