from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    ld = LaunchDescription()

    urdf_tutorial_path = FindPackageShare('rbot_modeling')
    default_model_path = PathJoinSubstitution(['urdf', 'robotarm1.urdf'])
    default_rviz_config_path = PathJoinSubstitution([urdf_tutorial_path, 'rviz', 'urdf.rviz'])
    gui_arg = DeclareLaunchArgument(
        name = 'gui',
        default_value='true',
        choices=['true', 'false'],
        description='Flag to enable joint_state_publisher_gui',
    )
    ld.add_action(gui_arg)
    rviz_arg = DeclareLaunchArgument(
        name='rviz_config',
        default_value=default_rviz_config_path,
        description='Absolute path to rviz config file',
    )
    ld.add_action(rviz_arg)
    ld.add_action(DeclareLaunchArgument(
        name = 'model',
        default_value=default_model_path,
        description='Path to robot urdf file relative to urdf_tutorial package',
    ))
    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'rbot_modeling',
            'urdf_package_path': LaunchConfiguration('model'),
            'jsp_gui': LaunchConfiguration('gui'),
            'rviz_config': LaunchConfiguration('rviz_config')
        }.items()
    ))

    return ld
