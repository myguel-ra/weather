# Mock weather service


class service:
    @staticmethod
    def get_temperature(city: str, days: int) -> float:
        if city.lower() == "lisbon":
            return 25.5
        else:
            raise ValueError(f"Temperature data not available for {city}")

    @staticmethod
    def will_rain(city: str, days: int) -> bool:
        if city.lower() == "lisbon":
            return True
        else:
            raise ValueError(f"Rain data not available for {city}")
