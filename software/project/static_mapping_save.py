#!/usr/bin/env python3
"""Static-mapping helper for the Autonomic Lift Truck project.

The script launches TurtleBot3 gmapping for a configurable static acquisition period,
saves a ROS map with map_server, and then terminates the SLAM process.
"""
import argparse
import os
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=30.0,
                        help="Static mapping time in seconds (documentation describes at least 30 s).")
    parser.add_argument("--output", default="saved_map",
                        help="Output map basename; map_saver creates .pgm and .yaml files.")
    parser.add_argument("--model", default="waffle_pi", help="TurtleBot3 model.")
    args = parser.parse_args()

    env = os.environ.copy()
    env["TURTLEBOT3_MODEL"] = args.model
    process = subprocess.Popen([
        "roslaunch", "turtlebot3_slam", "turtlebot3_slam.launch", "slam_methods:=gmapping"
    ], env=env)
    try:
        time.sleep(args.duration)
        subprocess.check_call(["rosrun", "map_server", "map_saver", "-f", args.output], env=env)
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


if __name__ == "__main__":
    main()
