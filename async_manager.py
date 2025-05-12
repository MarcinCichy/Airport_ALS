import asyncio
from communication.communication_module import AirTrafficControlServer
from controller.controller_module import AirTrafficController

async def main_loop(host=None, port=None):
    server = AirTrafficControlServer(host, port)
    air_traffic_controller = AirTrafficController(airspace, landing_queue, runway_manager)
    # radar = RadarDisplay(..)


    await asyncio.gather(
        server.start_server(),
        #air_traffic_controller.coordinate_aircrafts(),
        # radar.update_loop()
    )