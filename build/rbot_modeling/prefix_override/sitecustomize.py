import sys
if sys.prefix == '/home/kwamboka/anaconda3':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kwamboka/embodiedIntelligence/ros2_ws2/src/rbot_modeling/install/rbot_modeling'
