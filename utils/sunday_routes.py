import pandas as pd


def get_routes_after_8pm_on_sundays(calendar_path, trips_path, stop_times_path):
    """
    Identify unique route IDs that operate after 8 PM on Sundays
    using GTFS calendar, trips, and stop_times data.

    Parameters:
        calendar_path (str): Path to the GTFS calendar.txt file
        trips_path (str): Path to the GTFS trips.txt file
        stop_times_path (str): Path to the GTFS stop_times.txt file

    Returns:
        List[int]: List of unique route IDs operating after 8 PM on Sundays
    """

    # Load GTFS data files
    calendar = pd.read_csv(calendar_path)
    trips = pd.read_csv(trips_path)
    stop_times = pd.read_csv(stop_times_path)

    # Step 1: Identify Sunday service IDs
    sunday_services = calendar[calendar['sunday'] == 1]['service_id']

    # Step 2: Find trips that operate on Sundays
    sunday_trip_ids = trips[trips['service_id'].isin(sunday_services)]['trip_id']

    # Step 3: Filter stop_times for trips with departure after 8 PM
    trips_after_8pm = stop_times[
        (stop_times['trip_id'].isin(sunday_trip_ids)) &
        (stop_times['departure_time'] > '20:00')
    ]

    # Step 4: Retrieve route_ids for these trips
    routes_after_8pm = trips[trips['trip_id'].isin(trips_after_8pm['trip_id'])]['route_id']

    # Step 5: Return unique route IDs as a list
    return routes_after_8pm.unique().tolist()
