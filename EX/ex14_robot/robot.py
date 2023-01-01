"""
EX14 - Robot.

This program creates a line following robot using FollowerBot package.

Available functions:
test_run(robot: FollowerBot); Moves the robot compared to its starting position.
drive_to_line(robot: FollowerBot);

"""


from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move.

    Assignment requirements: It does not matter how much the robot moves,
    just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(10)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 15-30cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    # Move until two of the first sensors detect colour change to black.
    while True:
        # With these settings the robot should move about 3px during the cycle (100 * 0.03) which is
        # less than the line width (5px).
        robot.set_wheels_speed(100)
        robot.sleep(0.03)

        # Line sensor value 0 represents black and 1024 represents white.
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            # Move the robot about 20px.
            robot.set_wheels_speed(100)
            robot.sleep(0.2)
            # Then stop and break the cycle.
            robot.set_wheels_speed(0)
            robot.done()
            break


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == "__main__":
    robot = FollowerBot()
    # test_run(robot)
    drive_to_line(robot)
