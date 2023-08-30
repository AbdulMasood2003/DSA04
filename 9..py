import pandas as pd
data = {
    'location': ['Location_A', 'Location_B', 'Location_A', 'Location_C', 'Location_B', 'Location_C', 'Location_A'],
    'listing_price': [20000, 30000, 40000, 50000, 60000, 75000, 90000],
    'bedrooms': [2, 4, 5, 6, 5, 4, 3],
    'area': [1000, 1200, 1300, 1400, 1500, 1600, 1700]
}
property_data = pd.DataFrame(data)

def main():
    average_listing_price = property_data.groupby('location')['listing_price'].mean()
    print("Average Listing Price of Properties in Each Location:")
    print(average_listing_price)
    print()
    properties_with_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4]
    number_of_properties_with_more_than_four_bedrooms = properties_with_more_than_four_bedrooms.shape[0]
    print("Number of Properties with More Than Four Bedrooms:", number_of_properties_with_more_than_four_bedrooms)
    print()
    property_with_largest_area = property_data.loc[property_data['area'].idxmax()]
    print("Property with the Largest Area:")
    print(property_with_largest_area)
if __name__ == "__main__":
    main()
