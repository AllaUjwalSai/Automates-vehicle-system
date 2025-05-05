# Autonomous Vehicle Simulation: Pedestrian Detection & Lane Following

![Gazebo Simulation Screenshot](docs/images/gazebo_screenshot.png)  
*Example of the rover navigating a curved lane with obstacle detection.*

## 📌 Overview
This ROS-based project simulates an autonomous vehicle in Gazebo, featuring:
- **Pedestrian Detection**: HOG + SVM for real-time human detection.
- **Lane Following**: Edge-based vector calculation for road boundary tracking.
- **Terrain Adaptation**: LiDAR-driven speed control for inclines/obstacles.

Built on the NXO AIM 2024 stack for modular autonomy development.

## 🛠️ Key Components
| Module                  | Description                                                                 | ROS Topics                          |
|-------------------------|-----------------------------------------------------------------------------|-------------------------------------|
| `edge_vectors_publisher` | Processes camera images to detect lane edges.                              | `/edge_vectors`, `/debug_images/*`  |
| `line_follower`         | Implements steering logic and publishes `/joy` commands.                   | `/joy`, `/scan`, `/edge_vectors`    |
| `object_recognizer`     | (Optional) Pedestrian detection using HOG/SVM.                             | `/traffic_status`                   |

## 🚀 Quick Start
### Prerequisites
- Ubuntu 22.04 + ROS 2 Humble
- Gazebo Fortress
- OpenCV 4.x, NumPy

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/autonomous-rover-simulation.git
cd autonomous-rover-simulation

# Build with colcon
colcon build --symlink-install
source install/setup.bash
