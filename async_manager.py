from .communication_module import AirTrafficControlServer

async def main_loop():
    server = AirTrafficControlServer(host, port)
    air_traffic_controller = AirTrafficController(airspace, landing_queue, runway_manager)
    radar = RadarDisplay(..)


    await asyncio.gather(
        server.start_server(),
        air_traffic_controler.coordinate_aircrafts(),
        radar.update_loop()
    )