class service:
    """Mock weather service for temperature and rainfall predictions."""

    @staticmethod
    def get_temperature(city: str, days: int) -> float:
        """
        Get the predicted temperature for a city after a specified number of days.

        Args:
            city (str): The name of the city for which the temperature is predicted.
            days (int): The number of days into the future for the temperature prediction.

        Returns:
            float: The predicted temperature.

        Raises:
            ValueError: If the selected city is not available as an option.
        """
        if city.lower() == "lisbon":
            return 25.5
        raise ValueError("The selected city is not available as an option.")

    @staticmethod
    def will_rain(city: str, days: int) -> bool:
        """Check if it is predicted to rain in a city after a specified number of days."""
        if city.lower() == "lisbon":
            return True
        raise ValueError("The selected city is not available as an option.")
