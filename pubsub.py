import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64

class TurtleDistancePublisher(Node):
    def __init__(self):
        super().__init__('turtle_distance_publisher')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Float64, 'turtle1/distance_from_origin', 10)
        self.get_logger().info('Turtle Distance Publisher Node Started')

    def listener_callback(self, msg):
        # Extract x and y positions
        x = msg.x
        y = msg.y
        
        # Compute distance from origin
        distance = (x**2 + y**2)**0.5
        
        # Create and publish Float64 message
        distance_msg = Float64()
        distance_msg.data = distance
        self.publisher.publish(distance_msg)
        self.get_logger().info(f'Publishing distance: {distance}\n')

def main(args=None):
    rclpy.init(args=args)
    turtle_distance_publisher = TurtleDistancePublisher()
    try:
        rclpy.spin(turtle_distance_publisher)
    except KeyboardInterrupt:
        turtle_distance_publisher.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        turtle_distance_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
