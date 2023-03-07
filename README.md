# ROS_application_survey

## General Idea
1. Obtain the target repositories of the ROS applications. Prepare for both ROS and ROS2. 
2. Crawl the data from github through the Github API. The interested APIs are the issues and correpsonding commit fixes.
3. Analyze the data to understand the current ROS ecosystem.


## Development Progress
- [x] Integration of PyGithub library to query Github Repos and Issues.
- [x] Link PRs to corresponding issues. 
- [ ] Explore the details of the issues, and link it to the corresponding commits. (In Progress)
- [ ] Find ways to categorize the issues.


## Survey Progress
- [x] Manually label the projects into categories. 
  - [x] Develop a tool for easier labeling (`easy_labeling.py`)
- [ ] Once the development work is completed, we will start to crawl the data from the target repositories. 
  - [ ] The first study target is MoveIt: https://https://github.com/ros-planning/moveit (In Progress)
    - [ ] Issues categorization
    - [ ] Root cause analysis
- [ ] Consider making a tool for easier categorization (similar to `easy_labeling.py`)


## Bug Categorization
- General Bug: Bugs related to coding.
- Robot Specific Bug
  - Cross System Compatibility: Robot Operating System (ROS) has different versions, and the APIs have minor differences.

