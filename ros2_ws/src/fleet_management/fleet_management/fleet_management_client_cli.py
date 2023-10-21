import rclpy
from rclpy.action import ActionClient
from your_package_name.msg import FleetManagement

class FleetManagementClient:
    def __init__(self):
        self.node = rclpy.create_node('fleet_management_client')
        self.action_client = ActionClient(self.node, FleetManagement, 'fleet_management')
        self.logger = self.node.get_logger()

    def send_request(self, fleet_size):
        goal_msg = FleetManagement.Goal()
        goal_msg.fleet_size = fleet_size

        self.logger.info(f'Sending fleet management request for {fleet_size} vehicles...')

        future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        rclpy.spin_until_future_complete(self.node, future)

        if future.result() is not None:
            result = future.result().result()
            self.display_routes(result.vehicle_routes)
            self.logger.info('Fleet management task completed successfully.')
        else:
            self.logger.error('Fleet management task failed.')

    def feedback_callback(self, feedback_msg):
        # Update progress or show feedback to the user if needed
        pass

    def display_routes(self, routes):
        self.logger.info('Vehicle Routes:')
        for i, route in enumerate(routes, start=1):
            self.logger.info(f'Vehicle {i}: {route}')

def main(args=None):
    rclpy.init(args=args)
    fleet_management_client = FleetManagementClient()
    
    # Get the fleet size from the user or a command line argument
    fleet_size = 5  # Replace with user input or command line argument
    
    fleet_management_client.send_request(fleet_size)
    
    rclpy.spin(fleet_management_client.node)
    fleet_management_client.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

