from dataclasses import dataclass


@dataclass
class Observation:
    plate_num : str
    date : str
    car_type : str
    speed : float
    seatbelt_status : bool