# ROS_application_survey

## General Idea
1. Obtain the target repositories of the ROS applications. Prepare for both ROS and ROS2. 
2. Crawl the data from github through the Github API. The interested APIs are the issues and correpsonding commit fixes.
3. Analyze the data to understand the current ROS ecosystem.


## Development Progress
- [x] Integration of PyGithub library to query Github Repos and Issues.
- [ ] Explore the details of the issues, and link it to the corresponding commits.


## Survey Progress
- [ ] Manually label the projects into categories. 
- [ ] Once the development work is completed, we will start to crawl the data from the target repositories. 
  - [ ] The first study target is MoveIt: https://https://github.com/ros-planning/moveit
    - [ ] Issues categorization
    - [ ] Root cause analysis
