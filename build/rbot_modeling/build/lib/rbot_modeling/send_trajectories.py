#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time

class TrajectorySender(Node):
    def __init__(self):
        super().__init__('trajectory_sender')
        self.publisher = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        time.sleep(2)  # Let everything initialize

        self.send_poses()

    def send_poses(self):
        poses = [
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, -0.5, 1.0, -1.0, 0.5],
            [-0.7, 0.4, -1.2, 0.8, -0.6],
            [1.2, -1.2, 0.3, -0.5, 1.0]
        ]

        for idx, pose in enumerate(poses):
            traj_msg = JointTrajectory()
            traj_msg.joint_names = ['J_0', 'J_1', 'J_2', 'J_3', 'J_4']
            point = JointTrajectoryPoint()
            point.positions = pose
            point.time_from_start.sec = 3
            traj_msg.points = [point]

            self.get_logger().info(f'Sending pose {idx + 1}: {pose}')
            self.publisher.publish(traj_msg)
            time.sleep(5)  # Wait before next pose

        self.get_logger().info('All poses sent.')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = TrajectorySender()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
