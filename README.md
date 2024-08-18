# Forest Project: IoT-based Forest Preservation and Conservation System

## Overview
ForestWatch is an IoT-based project designed to help preserve and conserve forests by detecting and alerting relevant authorities about potential forest fires and illegal deforestation activities. <br>
This project was built using a combination of Node-RED for IoT simulation, Flask for database management, and various APIs for automated communication and notifications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features
1. **Simulated IoT System for Fire and Deforestation Detection** <br>
I have implemented a simulated IoT system using Node-RED to monitor forest conditions. The system detects abnormal temperature levels and acoustic signals indicative of fire or illegal logging activities.
   #### Fire Detection System
   ![Screenshot 2024-08-18 at 14 22 34](https://github.com/user-attachments/assets/1cd9b04f-5f19-4122-8bdf-f4263502b18e)

   #### Deforestation Detection System
   ![Screenshot 2024-08-18 at 14 24 17](https://github.com/user-attachments/assets/2ce4dd8e-99e6-4af1-9603-b40513ec6b58)

   
2. **Flask-Based Database (events.db)** <br>
The project uses a Flask application to manage an SQLite database (events.db). The database stores critical data such as event types, timestamps, sensor values, latitude and longitude coordinates, and additional details.
![Screenshot 2024-08-18 at 14 25 39](https://github.com/user-attachments/assets/830517d8-eac3-4f18-b530-44a583fd651d)

3. **Automated Email Notifications** <br>
**Contact Retrieval**: The system uses the **Nylas API** to retrieve contact information for the relevant authorities. <br>
**Email Sending**: Once an incident is detected, the system automatically sends an email notification to the authorities using the **Nylas API**.
   #### Forest Fire Detected
   ![Screenshot 2024-08-18 at 14 51 17](https://github.com/user-attachments/assets/2406b5f0-b08c-49c1-9963-0e751b0ebda6)

   #### Deforestation Detected
   ![Screenshot 2024-08-18 at 14 51 36](https://github.com/user-attachments/assets/2debcb15-4165-48e0-af11-d9961c7e7051)

4. **Push Notifications** <br>
Push notifications are sent to the user’s mobile device using Remote-RED, ensuring timely alerts on forest-related incidents.
   #### Forest Fire Detected
   ![IMG_4396_11zon](https://github.com/user-attachments/assets/240701ec-445e-40c3-8d3f-0ae10779e915)

   #### Deforestation Detected
   ![IMG_4397_11zon](https://github.com/user-attachments/assets/c1958c6c-8ce1-423d-a390-00ecd7d68ddd)

   
5. **SMS Notifications** <br>
Twilio is integrated into the system to send text message notifications to relevant authorities when an incident is detected.
6. **Calendar Integration** <br>
The system automatically implements the **Nylas API** to mark events related to forest illegalities on a calendar, providing a historical record of incidents.

   #### Illegal Forest Event(s) Added to Calendar
   ![Screenshot 2024-08-18 at 14 50 56](https://github.com/user-attachments/assets/34102219-3a88-4270-a79b-8ba49bc3310c)


7. **Simple Dashboard** <br>
A dashboard is available to visualize and analyze the data from the events.db database, providing insights into forest activities and trends.

   #### Simple Dashboard
   ![Screenshot 2024-08-18 at 15 01 41](https://github.com/user-attachments/assets/2b0047f8-a928-439a-9d03-86b4d0851afb)

8. **API Endpoints** <br>
Several API endpoints are built into the Flask application to facilitate data fetching and interaction with the system.
9. **Mobile Compatibility** <br>
The user interface is accessible via mobile devices, thanks to the integration with Remote-RED, allowing for real-time monitoring on the go.

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- `pip` (Python package installer).
- SQLite
- Node-RED
- Flask
- Nylas API Account
- Twilio Account
- Remote-RED

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ForestWatch.git
   cd ForestWatch
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

   The application will be running at `http://127.0.0.1:5000/`.

### Testing the Endpoints

- **Home Page:**

  Visit the home page by navigating to `http://127.0.0.1:5000/dashboard` in your web browser. You should see the dashboard.

## Project Structure

```
├── README.md
├── LICENSE
├── app.py                   # Flask application, API endpoints, and routes
├── .env
├── scripts/                 # Nylas API interaction scripts
├── instance/events.db       # SQLite database
├── assets/                  # images
├── templates/               # HTML templates
└── node-red/                # Node-RED flow configurations 
```

## Endpoints
The routes and endpoints used during the implementation of this project are found in app.py file

## Acoustic Sensors Simulation
![alt text](assets/Images/Acoustic_Sensors.png)

## Temperature Sensors Simulation
![alt text](assets/Images/Temperature_Sensors.png)

## Future Enhancements

- [x] **Integrate with Nylas API:** Add functionality to send detailed email notifications using the Nylas API.
- [x] **Add Real Event Detection:** Implement real-time detection of logging and fire events using IoT devices or external APIs.
- [ ] **Deploy to Cloud:** Host the Flask application on a cloud platform like Heroku or AWS.
- [ ] OAuth 2.0 using Nylas API
- [ ] Integration of AI(LLM) into the system

## Usage
- Real-Time Monitoring: Monitor forest activities in real-time via the dashboard
- Notifications: Receive automated alerts via email, SMS, and push notifications
- Data Storage: Storage and management of historical data

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
