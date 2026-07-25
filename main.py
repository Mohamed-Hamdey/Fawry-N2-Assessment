from rules.Speed_Limit import Speed_Limit
from rules.Seatbelt import Seatbelt_Rule
from models.observation import Observation
from quant_radar import Qu_Radar

class Main:

    @staticmethod
    def run() -> None:
        radar = Qu_Radar()

        # Register rules. Adding/removing rules never touches QuRadar itself.
        radar.add_rule(Seatbelt_Rule(fee=100))
        radar.add_rule(Speed_Limit("Truck", 60, fee=300))
        radar.add_rule(Speed_Limit("Private", 80, fee=300))
        radar.add_rule(Speed_Limit("Bus", 70, fee=300))

        observations = [
            Observation("ABC1234", "2026-07-25", "Private", 94, False),
            Observation("XYZ987", "2026-07-25", "Truck", 55, True),
            Observation("BUS111", "2026-07-25", "Bus", 85, True),
            Observation("CLN555", "2026-07-25", "Private", 60, True),
        ]

        for obs in observations:
            fine = radar.process(obs)
            if fine:
                fine.print_fine()
                print()

        print("== getAllPossibleFines ==")
        for entry in radar.getAllPossibleFines():
            print(f"{entry['plate_number']}: {int(entry['total_amount'])} EGP")

        print("\n== Violated rules (count) ==")
        for rule_name, count in radar.get_all_violated_rules().items():
            print(f"{rule_name}: {count}")


if __name__ == "__main__":
    Main.run()