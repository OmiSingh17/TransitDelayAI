from utils.sunday_routes import get_routes_after_8pm_on_sundays

routes = get_routes_after_8pm_on_sundays(
    'data/calendar.txt',
    'data/trips.txt',
    'data/stop_times.txt'
)

print("✅ Routes operating after 8 PM on Sundays:")
print(routes)
