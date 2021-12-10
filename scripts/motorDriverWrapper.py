import rospy
from driver_scripts.drives import Drives
from std_msgs.msg import Int32
from four_wheel_drive.msg import Drives_command
from std_srvs.srv import Trigger

class MotorDriver:
    def __init__(self) -> None:
        self.drives = Drives
        rospy.Service("stop_motor", Trigger, self.callback_stop)
        


    def callback_stop(self, req):
        self.drives.stop()
        return {"success": True, "message": "Motors have been stopped"}

    def stop(self):
        self.drives.stop()
