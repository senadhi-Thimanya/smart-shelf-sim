# 🛍️ Smart Shelf Sim - Edge + Microservices Project

This is a sample project that simulates a smart shelf monitoring system using edge computing and microservices. It uses Python and Flask to demonstrate communication between simulated edge devices and a cloud API. (Uses docker)

## 🧱 Components

- `shelf_vision_service`: randomly simulates shelf image analysis
- `shelf_status_service`: detects changes in stock status
- `event_publisher_service`: sends updates to the cloud
- `cloud_api`: receives and logs updates

## 🚀 How to Run

1. Clone the repo
2. Open each script in VS Code
3. Run `cloud/cloud_api.py` first
4. Run the edge services and observe the output

## 💡 Future Additions
- Docker containers
- Dashboard UI
- Real image detection logic
