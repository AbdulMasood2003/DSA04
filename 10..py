import pandas as pd
import matplotlib.pyplot as plt
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [1000, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 1800, 1900, 1700]
}
monthly_sales_data = pd.DataFrame(data)
def plot_line_chart():
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales_data['month'], monthly_sales_data['sales'], marker='o', linestyle='-', color='b')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    plot_line_chart()
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [1000, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 1800, 1900, 1700]
}
monthly_sales_data = pd.DataFrame(data)
def plot_bar_chart():
    
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_sales_data['month'], monthly_sales_data['sales'], color='b')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(axis='y')
    plt.show()
if __name__ == "__main__":
    plot_bar_chart()
