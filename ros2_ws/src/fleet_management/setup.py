from setuptools import find_packages, setup

package_name = 'fleet_management'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yevgeniy',
    maintainer_email='risimon@mail.ru',
    description='Fleet Management System in CLI',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = fleet_management.fleet_management_server_cli:main',
            'client = fleet_management.fleet_management_client_cli:main',
            'cli = fleet_management.fleet_management_cli:main'
        ],
    },
)
