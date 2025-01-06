def add_package(shipments, tracking_number, details):
    shipments[tracking_number] = details

def update_package_status(shipments, tracking_number, status):
    if tracking_number in shipments:
        shipments[tracking_number]['status'] = status
    else:
        print(f"Tracking number {tracking_number} not found")

def get_package_details(shipments, tracking_number):
    return shipments[tracking_number]

def print_shipments(shipments):
    for tracking_number, details in shipments.items():
        print(f"Tracking Number: {tracking_number}, Status: {details['status']}, Destination: {details['destination']}")

shipments = {}
add_package(shipments, "ABC123", {'status': 'In Transit', 'destination': 'New York'})
add_package(shipments, "XYZ789", {'status': 'Delivered', 'destination': 'Los Angeles'})
update_package_status(shipments, "XYZ789", "Returned")
print_shipments(shipments)
print("Details for 'DEF456':", get_package_details(shipments, "DEF456"))