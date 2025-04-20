import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare(package='rbot_modeling').find('rbot_modeling')
    model_name = 'robot2.urdf.xacro'
    def_model_path = os.path.join(pkg_share, 'urdf', model_name)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'RoboticArm', '-topic', 'robot_description'],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='model',
            default_value=def_model_path,
            description='Absolute path to the URDF file.'
        ),
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_robot
    ])
if __name__ == '__main__':
    generate_launch_description()