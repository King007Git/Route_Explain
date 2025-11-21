DATA=[
  {
    "date": "2025-11-22",
    "routes": [
      {
        "route_id": "R1",
        "vehicle": {
          "id": "V1",
          "type": "Medium Van",
          "capacity_kg": 1200
        },
        "driver": {
          "id": "D1",
          "name": "Alex",
          "max_work_minutes": 480,
          "performance": {
            "speed_factor": 0.95,
            "max_continuous_drive_min": 150,
            "break_duration_min": 15
          }
        },
        "summary": {
          "total_distance_km": 76.3,
          "total_travel_time_min": 142,
          "total_service_time_min": 70,
          "total_break_time_min": 15,
          "total_stops": 6
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "address": "12 Warehouse Road, Central Industrial Area",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T08:00:00+05:30",
            "planned_departure": "2025-11-22T08:15:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 15,
            "load_change_kg": 900,
            "load_after_stop_kg": 900,
            "time_window": { "start": "08:00", "end": "09:00" }
          },
          {
            "sequence": 2,
            "stop_id": "S1",
            "type": "delivery",
            "name": "Green Mart - Indiranagar",
            "address": "21 100 Ft Road, Indiranagar",
            "lat": 12.9784,
            "lng": 77.6408,
            "planned_arrival": "2025-11-22T08:35:00+05:30",
            "planned_departure": "2025-11-22T08:45:00+05:30",
            "distance_from_previous_km": 7.2,
            "travel_time_from_previous_min": 20,
            "service_time_min": 10,
            "load_change_kg": -250,
            "load_after_stop_kg": 650,
            "time_window": { "start": "08:30", "end": "09:30" }
          },
          {
            "sequence": 3,
            "stop_id": "S2",
            "type": "delivery",
            "name": "Fresh Basket - Whitefield",
            "address": "55 ITPL Main Road, Whitefield",
            "lat": 12.9698,
            "lng": 77.7499,
            "planned_arrival": "2025-11-22T09:20:00+05:30",
            "planned_departure": "2025-11-22T09:35:00+05:30",
            "distance_from_previous_km": 16.5,
            "travel_time_from_previous_min": 35,
            "service_time_min": 15,
            "load_change_kg": -300,
            "load_after_stop_kg": 350,
            "time_window": { "start": "09:00", "end": "10:00" }
          },
          {
            "sequence": 4,
            "stop_id": "B1",
            "type": "break",
            "name": "Driver Break - Highway Lay-by",
            "address": "Near Outer Ring Road Junction",
            "lat": 12.96,
            "lng": 77.72,
            "planned_arrival": "2025-11-22T09:40:00+05:30",
            "planned_departure": "2025-11-22T09:55:00+05:30",
            "distance_from_previous_km": 3.0,
            "travel_time_from_previous_min": 5,
            "service_time_min": 15,
            "load_change_kg": 0,
            "load_after_stop_kg": 350,
            "time_window": None
          },
          {
            "sequence": 5,
            "stop_id": "S3",
            "type": "pickup",
            "name": "Return Center - Marathahalli",
            "address": "3 Service Lane, Marathahalli",
            "lat": 12.9550,
            "lng": 77.7010,
            "planned_arrival": "2025-11-22T10:10:00+05:30",
            "planned_departure": "2025-11-22T10:20:00+05:30",
            "distance_from_previous_km": 8.1,
            "travel_time_from_previous_min": 15,
            "service_time_min": 10,
            "load_change_kg": 100,
            "load_after_stop_kg": 450,
            "time_window": { "start": "10:00", "end": "11:00" }
          },
          {
            "sequence": 6,
            "stop_id": "S4",
            "type": "depot",
            "name": "Main City Depot",
            "address": "12 Warehouse Road, Central Industrial Area",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T11:02:00+05:30",
            "planned_departure": "2025-11-22T11:10:00+05:30",
            "distance_from_previous_km": 41.5,
            "travel_time_from_previous_min": 47,
            "service_time_min": 8,
            "load_change_kg": -450,
            "load_after_stop_kg": 0,
            "time_window": { "start": "10:30", "end": "12:30" }
          }
        ]
      },
      {
        "route_id": "R2",
        "vehicle": {
          "id": "V2",
          "type": "Small Van",
          "capacity_kg": 800
        },
        "driver": {
          "id": "D2",
          "name": "Sarah",
          "max_work_minutes": 420,
          "performance": {
            "speed_factor": 1.0,
            "max_continuous_drive_min": 120,
            "break_duration_min": 20
          }
        },
        "summary": {
          "total_distance_km": 45.2,
          "total_travel_time_min": 110,
          "total_service_time_min": 45,
          "total_break_time_min": 0,
          "total_stops": 4
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T09:00:00+05:30",
            "planned_departure": "2025-11-22T09:15:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 15,
            "load_change_kg": 500,
            "load_after_stop_kg": 500,
            "time_window": { "start": "09:00", "end": "10:00" }
          },
          {
            "sequence": 2,
            "stop_id": "S5",
            "type": "delivery",
            "name": "Koramangala Tech Park",
            "lat": 12.9352,
            "lng": 77.6245,
            "planned_arrival": "2025-11-22T09:45:00+05:30",
            "planned_departure": "2025-11-22T10:05:00+05:30",
            "distance_from_previous_km": 8.5,
            "travel_time_from_previous_min": 30,
            "service_time_min": 20,
            "load_change_kg": -200,
            "load_after_stop_kg": 300,
            "time_window": { "start": "09:30", "end": "10:30" }
          },
          {
            "sequence": 3,
            "stop_id": "S6",
            "type": "delivery",
            "name": "Jayanagar 4th Block",
            "lat": 12.9250,
            "lng": 77.5938,
            "planned_arrival": "2025-11-22T10:25:00+05:30",
            "planned_departure": "2025-11-22T10:35:00+05:30",
            "distance_from_previous_km": 5.2,
            "travel_time_from_previous_min": 20,
            "service_time_min": 10,
            "load_change_kg": -300,
            "load_after_stop_kg": 0,
            "time_window": { "start": "10:00", "end": "11:00" }
          },
          {
            "sequence": 4,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T11:15:00+05:30",
            "planned_departure": "2025-11-22T11:25:00+05:30",
            "distance_from_previous_km": 7.5,
            "travel_time_from_previous_min": 40,
            "service_time_min": 10,
            "load_change_kg": 0,
            "load_after_stop_kg": 0,
            "time_window": { "start": "11:00", "end": "12:00" }
          }
        ]
      },
      {
        "route_id": "R3",
        "vehicle": {
          "id": "V3",
          "type": "Truck",
          "capacity_kg": 5000
        },
        "driver": {
          "id": "D3",
          "name": "Mike",
          "max_work_minutes": 540,
          "performance": {
            "speed_factor": 0.8,
            "max_continuous_drive_min": 180,
            "break_duration_min": 30
          }
        },
        "summary": {
          "total_distance_km": 32.0,
          "total_travel_time_min": 90,
          "total_service_time_min": 60,
          "total_break_time_min": 0,
          "total_stops": 3
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T07:00:00+05:30",
            "planned_departure": "2025-11-22T07:30:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 30,
            "load_change_kg": 4000,
            "load_after_stop_kg": 4000,
            "time_window": { "start": "07:00", "end": "08:00" }
          },
          {
            "sequence": 2,
            "stop_id": "S7",
            "type": "delivery",
            "name": "Peenya Industrial Estate",
            "lat": 13.0285,
            "lng": 77.5197,
            "planned_arrival": "2025-11-22T08:15:00+05:30",
            "planned_departure": "2025-11-22T08:45:00+05:30",
            "distance_from_previous_km": 16.0,
            "travel_time_from_previous_min": 45,
            "service_time_min": 30,
            "load_change_kg": -4000,
            "load_after_stop_kg": 0,
            "time_window": { "start": "08:00", "end": "12:00" }
          },
          {
            "sequence": 3,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T09:30:00+05:30",
            "planned_departure": "2025-11-22T09:40:00+05:30",
            "distance_from_previous_km": 16.0,
            "travel_time_from_previous_min": 45,
            "service_time_min": 10,
            "load_change_kg": 0,
            "load_after_stop_kg": 0,
            "time_window": { "start": "09:00", "end": "10:00" }
          }
        ]
      },
      {
        "route_id": "R4",
        "vehicle": {
          "id": "V4",
          "type": "Scooter",
          "capacity_kg": 50
        },
        "driver": {
          "id": "D4",
          "name": "Raj",
          "max_work_minutes": 300,
          "performance": {
            "speed_factor": 1.1,
            "max_continuous_drive_min": 90,
            "break_duration_min": 10
          }
        },
        "summary": {
          "total_distance_km": 12.0,
          "total_travel_time_min": 40,
          "total_service_time_min": 15,
          "total_break_time_min": 0,
          "total_stops": 3
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T10:00:00+05:30",
            "planned_departure": "2025-11-22T10:05:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 5,
            "load_change_kg": 10,
            "load_after_stop_kg": 10,
            "time_window": { "start": "10:00", "end": "10:15" }
          },
          {
            "sequence": 2,
            "stop_id": "S8",
            "type": "delivery",
            "name": "Residency Road Office",
            "lat": 12.9740,
            "lng": 77.6090,
            "planned_arrival": "2025-11-22T10:20:00+05:30",
            "planned_departure": "2025-11-22T10:25:00+05:30",
            "distance_from_previous_km": 3.0,
            "travel_time_from_previous_min": 15,
            "service_time_min": 5,
            "load_change_kg": -10,
            "load_after_stop_kg": 0,
            "time_window": { "start": "10:15", "end": "10:45" }
          },
          {
            "sequence": 3,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-22T10:50:00+05:30",
            "planned_departure": "2025-11-22T10:55:00+05:30",
            "distance_from_previous_km": 3.0,
            "travel_time_from_previous_min": 25,
            "service_time_min": 5,
            "load_change_kg": 0,
            "load_after_stop_kg": 0,
            "time_window": { "start": "10:30", "end": "11:00" }
          }
        ]
      }
    ]
  },
  {
    "date": "2025-11-21",
    "routes": [
      {
        "route_id": "R5",
        "vehicle": {
          "id": "V1",
          "type": "Medium Van",
          "capacity_kg": 1200
        },
        "driver": {
          "id": "D1",
          "name": "Alex",
          "max_work_minutes": 480,
          "performance": {
            "speed_factor": 0.95,
            "max_continuous_drive_min": 150,
            "break_duration_min": 15
          }
        },
        "summary": {
          "total_distance_km": 60.0,
          "total_travel_time_min": 120,
          "total_service_time_min": 50,
          "total_break_time_min": 0,
          "total_stops": 3
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-21T08:00:00+05:30",
            "planned_departure": "2025-11-21T08:15:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 15,
            "load_change_kg": 800,
            "load_after_stop_kg": 800,
            "time_window": { "start": "08:00", "end": "09:00" }
          },
          {
            "sequence": 2,
            "stop_id": "S9",
            "type": "delivery",
            "name": "Electronic City Phase 1",
            "lat": 12.8452,
            "lng": 77.6602,
            "planned_arrival": "2025-11-21T09:15:00+05:30",
            "planned_departure": "2025-11-21T09:35:00+05:30",
            "distance_from_previous_km": 20.0,
            "travel_time_from_previous_min": 60,
            "service_time_min": 20,
            "load_change_kg": -800,
            "load_after_stop_kg": 0,
            "time_window": { "start": "09:00", "end": "10:00" }
          },
          {
            "sequence": 3,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-21T10:35:00+05:30",
            "planned_departure": "2025-11-21T10:45:00+05:30",
            "distance_from_previous_km": 20.0,
            "travel_time_from_previous_min": 60,
            "service_time_min": 10,
            "load_change_kg": 0,
            "load_after_stop_kg": 0,
            "time_window": { "start": "10:00", "end": "11:00" }
          }
        ]
      }
    ]
  },
  {
    "date": "2025-11-20",
    "routes": [
      {
        "route_id": "R6",
        "vehicle": {
          "id": "V2",
          "type": "Small Van",
          "capacity_kg": 800
        },
        "driver": {
          "id": "D2",
          "name": "Sarah",
          "max_work_minutes": 420,
          "performance": {
            "speed_factor": 1.0,
            "max_continuous_drive_min": 120,
            "break_duration_min": 20
          }
        },
        "summary": {
          "total_distance_km": 18.0,
          "total_travel_time_min": 50,
          "total_service_time_min": 30,
          "total_break_time_min": 0,
          "total_stops": 3
        },
        "stops": [
          {
            "sequence": 1,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-20T08:30:00+05:30",
            "planned_departure": "2025-11-20T08:45:00+05:30",
            "distance_from_previous_km": 0,
            "travel_time_from_previous_min": 0,
            "service_time_min": 15,
            "load_change_kg": 300,
            "load_after_stop_kg": 300,
            "time_window": { "start": "08:30", "end": "09:30" }
          },
          {
            "sequence": 2,
            "stop_id": "S10",
            "type": "delivery",
            "name": "Malleshwaram Market",
            "lat": 13.0055,
            "lng": 77.5692,
            "planned_arrival": "2025-11-20T09:10:00+05:30",
            "planned_departure": "2025-11-20T09:20:00+05:30",
            "distance_from_previous_km": 6.0,
            "travel_time_from_previous_min": 25,
            "service_time_min": 10,
            "load_change_kg": -300,
            "load_after_stop_kg": 0,
            "time_window": { "start": "09:00", "end": "10:00" }
          },
          {
            "sequence": 3,
            "stop_id": "S0",
            "type": "depot",
            "name": "Main City Depot",
            "lat": 12.9716,
            "lng": 77.5946,
            "planned_arrival": "2025-11-20T09:45:00+05:30",
            "planned_departure": "2025-11-20T09:50:00+05:30",
            "distance_from_previous_km": 6.0,
            "travel_time_from_previous_min": 25,
            "service_time_min": 5,
            "load_change_kg": 0,
            "load_after_stop_kg": 0,
            "time_window": { "start": "09:30", "end": "10:30" }
          }
        ]
      }
    ]
  }
]