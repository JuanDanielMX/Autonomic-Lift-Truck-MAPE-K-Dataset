#!/usr/bin/env python3

import rospy
import subprocess
import time

def start_slam_and_save_map():
    # Initialize the ROS node
    rospy.init_node('turtlebot3_slam_and_save', anonymous=True)
    
    # Set the TurtleBot3 model parameter
    rospy.set_param("TURTLEBOT3_MODEL", "waffle_pi")
    
    # Path to save the map
    map_filename = "/home/user/Downloads/saved_map"
    
    # Start the gmapping slam process
    try:
        slam_process = subprocess.Popen(["roslaunch", "turtlebot3_slam", "turtlebot3_slam.launch", "slam_methods:=gmapping"])
        
        # Allow SLAM to run for a specified duration (e.g., 300 seconds or 5 minutes)
        duration = 15
        time.sleep(duration)

        # Save the generated map in the specified directory
        subprocess.call(["rosrun", "map_server", "map_saver", "-f", map_filename])

        # Terminate the SLAM process
        slam_process.terminate()

    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    start_slam_and_save_map()

