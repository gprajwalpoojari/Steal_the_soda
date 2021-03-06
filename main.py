from world import *
from can import *
from RRT import *

fig = plt.figure("Environment")
ax = fig.add_subplot(projection='3d')
ax.set_xlim(0, 2000)
ax.set(xlabel = 'X Axis', ylabel = 'Y Axis', zlabel = 'Z Axis')
world = World(fig, ax)
world.create_world()
world_equations = world.get_world_equations()
window_params = world.get_window_params()
can = Can(fig, ax)
can.update_pose((200, 500, 26), 90, 0, 0)
can.update_can_points()
can.spawn_can()
planner = RRT(fig, ax, world_equations, window_params, start=(200, 500, 26), goal=(1500, 500, 200))

status = planner.build_RRT()
print(status)
# if status == True:
#     planner.trace_path(can)
# plt.show()
# can.update_pose()
# can.spawn_can()
# plt.pause(2)
# can.clear_can()
# can.update_pose((750,500,800), 0, 90, 0)
# can.update_can_points()
# can.spawn_can()
# plt.pause(2)
# can.clear_can()
# value = can.check_collision(world_equations, window_params)
# print(value)
plt.show()