import roslib
roslib.load_manifest('baxter_states')
import rospy
import smach
import smach_ros
from simple_script_server import *  # import script
sss = simple_script_server()

from cob_srvs.srv import Trigger

class MoveArm(smach.State):
	def __init__(self):
		smach.State.__init__(self, 
			outcomes=['succeeded','preempted','aborted'],
			input_keys=['component', 'state'])

	def execute(self, userdata):
		
		sss.move(userdata.component,userdata.state)
		
		
		return 'succeeded'

