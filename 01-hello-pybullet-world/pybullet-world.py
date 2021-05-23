import pybullet as p
import time
import pybullet_data

# PyBullet is designed a client-server driven API.
# Client send commands to server, and server returns the status

# [DIRECT]
# The DIRECT connection sends the commands directly to the physics engine, 
# without using any transport layer and no graphics visualization window, 
# and directly returns the status after executing the command.

# [GUI]
# The GUI connection will create a new graphical user interface (GUI) 
# with 3D OpenGL rendering, within the same process space as PyBullet. 
# On Linux and Windows this GUI runs in a separate thread, while on OSX it runs in 
# the same thread due to operating system limitations. 
# On Mac OSX you may see a spinning wheel in the OpenGL Window, until you run a 'stepSimulation' 
# or other PyBullet command.

physicsClient = p.connect(p.GUI) # or p.DIRECT for non-graphical version

# optionally. If you have your own data files, you should set path through this
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)  # X, Y, Z # Default: No Gravity
p.configureDebugVisualizer(p.COV_ENABLE_GUI, False)
p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, True)
p.resetDebugVisualizerCamera(cameraDistance=1.400, cameraYaw=58.000, cameraPitch=-42.200, cameraTargetPosition=(0.0, 0.0, 0.0))

planeId = p.loadURDF("plane.urdf")
base_pos = [0, 0, 0]
base_orientation = p.getQuaternionFromEuler([0,0,0])
ur5 = p.loadURDF('../ur_description/urdf/ur5_robot.urdf', basePosition=base_pos, baseOrientation=base_orientation, useFixedBase=True)
p.resetBasePositionAndOrientation(ur5, base_pos, base_orientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(ur5)
print(f"End position and orientation: {cubePos} / {cubeOrn}")
p.disconnect()
