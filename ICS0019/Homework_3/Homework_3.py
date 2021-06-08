import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import pandas as pd


def main():
    fig = plt.figure(figsize=(20, 20))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([-20, 50, 30, 70], crs=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND)

    def plotLine(from_lon, from_lat, from_name, to_lon, to_lat, to_name, color):
        plt.plot([from_lon, to_lon], [from_lat, to_lat],
                 color=color, linewidth=2, marker='o',
                 transform=ccrs.Geodetic(),
                 )

        plt.text(from_lon - 1, from_lat - 1, from_name,
                 horizontalalignment='left',
                 transform=ccrs.Geodetic())

        plt.text(to_lon - 1, to_lat - 1, to_name,
                 horizontalalignment='left',
                 transform=ccrs.Geodetic())

    airports_before = pd.read_csv('otselennud.csv', sep=';')
    airports_after = pd.read_csv('flights21.csv', sep=';')
    airports_data = pd.read_csv('airports.dat', sep=',', na_filter=False, usecols=['IATA', 'Latitude', 'Longitude'])

    flights_before = airports_before.merge(airports_data, how="left")
    flights_after = airports_after.merge(airports_data, how="left")

    color_before = 'red'
    color_after = 'blue'

    tallinn_name = 'TLL'
    tallinn_lat = 59.4133
    tallinn_lon = 24.8328

    for index, row in flights_before.iterrows():
        if(row['IATA'] != 'TLL'):
            plotLine(tallinn_lon, tallinn_lat, tallinn_name, row['Longitude'], row['Latitude'], row['IATA'], color_before)

    for index, row in flights_after.iterrows():
        if (row['IATA'] != 'TLL'):
            plotLine(tallinn_lon, tallinn_lat, tallinn_name, row['Longitude'], row['Latitude'], row['IATA'], color_after)

    plt.annotate('Dachi Mshvidobadze', xy=(0.3, 1.1), xycoords='axes fraction', size=50)
    fig.savefig('airports_plot.jpg', bbox_inches='tight', dpi=150)

    plt.show()


if __name__ == '__main__':
    main()