import click
from your_package_name.fleet_management_client_cli import FleetManagementClient

@click.command()
@click.option('--fleet-size', type=int, required=True, help='Specify the fleet size for allocation and routing.')
def allocate_and_route(fleet_size):
    """Allocate and route vehicles for a fleet management task."""
    client = FleetManagementClient()

    # Validate the fleet size (you can add more validation as needed)
    if fleet_size <= 0:
        click.echo("Fleet size must be a positive integer.")
        return

    # Send the request to the Action Server using the Action Client
    client.send_request(fleet_size)

if __name__ == '__main__':
    allocate_and_route()

