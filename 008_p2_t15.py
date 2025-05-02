# Instalación de ROS (Ubuntu)
sudo apt install ros-noetic-desktop-full
source /opt/ros/noetic/setup.bash

# Nodo Python en ROS
roscore

# Nodo publisher
rostopic pub /led std_msgs/Bool "data: true"
