Progress Update
- 07/03/2022: Complete the initial auditing of MoveIt issue page 1.
- 

---- Below are the valid contents ----

All_Labels: 
- Inconsistency, 
- Assertion, 
- Compatibility, 
  - ROS Version
  - 
- Compile Error,
- GUI accessibility,

1. [cannot compile from source](https://github.com/ros-planning/moveit/issues/3310)
   - KeyIssue: moveit cmake configs that might only trigger on Ubuntu 22.04 / devel workspaces with ruckig included
   - Label: Compatibility - ROS Version, Compile Error
   - Remark: 
   - VersionDependency: true
   - Version: Noetic, Ubuntu_22.04
2. [The MoveIt Planning Scene Interface confuses me](https://github.com/ros-planning/moveit/issues/3291)
   - KeyIssue: inconsistencies with moveit_commander when importing and exporting .scene files
   - Label: Inconsistency, 
   - Remark:
   - VersionDependency: false
   - Version: Noetic, Ubuntu_20.04
3. [Collision of newly attached object not taken into account for first plan](https://github.com/ros-planning/moveit/issues/3207)
   - KeyIssue: Inconsistency between planning and execution when attaching objects
   - Label: Inconsistency,
   - Remark:
   - VersionDependency: false
   - Version: Melodic, Ubuntu_18.04
4. [Calling `moveit_commander` function `set_joint_value_target` crashes without warnings if `len(position) < len(name)`]
   - KeyIssue: missing assertion.
   - Label: Assertion,
   - Remark:
   - VersionDependency: false
   - Version: Noetic, Ubuntu_20.04
5. [Getting a warning when attaching a box: "Empty quaternion found in pose message"](https://github.com/ros-planning/moveit/issues/3174)
   - KeyIssue: A warning that should not be there.
   - Label: Inconsistency,
   - Remark: this is a very minor issue.
   - VersionDependency: false
   - Version: Noetic, Ubuntu_20.04
6. [Different planning results between c++ and python interface](https://github.com/ros-planning/moveit/issues/3159)
   - KeyIssue: Rviz works but the python interface does not.
   - Label: Version Compatibility,
   - Remark:
   - VersionDependency: true
   - Version: Noetic, Ubuntu_20.04
7. [CHOMP planner segmentation fault in noetic-devel](https://github.com/ros-planning/moveit/issues/3154)
   - KeyIssue: A field is not initialized. 
   - Label: Initialization,
   - Remark:
   - VersionDependency: true
   - Version: Noetic, Ubuntu_20.04
8. [The issue of moveit_setup_assistant gui in defining the robot pose- joint label, joint value and slide bar is too small](https://github.com/ros-planning/moveit/issues/3118)
   - KeyIssue: The GUI is not user-friendly.
   - Label: GUI accessibility,
   - Remark: not functional. The problem happens when using 4K screen (with high resolution).
   - VersionDependency: false
   - Version: Noetic, Ubuntu_20.04
9. [bug in move_group.py](https://github.com/ros-planning/moveit/issues/3061)
   -  KeyIssue: The except catch is not correct.
   -  Label: Exception Handling, Compatibility - ROS Version,
   -  Remark: Happen only in Noetic because Melodic has a different exception handle
   -  VersionDependency: true
   -  Version: Noetic, Ubuntu_20.04
10. [`moveit_ros_benchmarks` in MoveIt 1.1.7 segmentation fault](https://github.com/ros-planning/moveit/issues/3037)
   -  KeyIssue: launch file is not correct due to incompatibility between config and parser
   -  Label: 