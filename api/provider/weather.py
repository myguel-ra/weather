# Mock weather service


class service:
    @staticmethod
    def get_temperature(city: str, days: int) -> float:
        if city.lower() == "lisbon":
            return 25.5
        else:
            raise ValueError("The selected city is not available as an option.")

    @staticmethod
    def will_rain(city: str, days: int) -> bool:
        if city.lower() == "lisbon":
            return True
        else:
            raise ValueError("The selected city is not available as an option.")
