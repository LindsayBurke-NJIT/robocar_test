#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class myNode(Node):
    def __init__(self):
        super().__init__("my_first_node")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("hello")

def main():
    rclpy.init()

    #node 1
    node = myNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()