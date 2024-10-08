"""
Clock Angle:
Given two times in HH:MM format, calculate the angle between the hour and minute hands of a clock
"""

class ClockAngle:
    def calculate_angle(self, hour: int, minute: int) -> float:
        """
        Calculate the angle between hour and minute hands of a clock.
        
        :param hour: Hour (0-23)
        :param minute: Minute (0-59)
        :return: Angle in degrees (0-180)
        """
        # Validate input
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError("Invalid input. Hour should be 0-23, minute should be 0-59.")
        
        # Convert 24-hour format to 12-hour format
        hour = hour % 12
        
        # Calculate angles
        # Hour hand moves 360° in 12 hours, or 0.5° per minute
        hour_angle = (hour * 60 + minute) * 0.5
        
        # Minute hand moves 360° in 60 minutes, or 6° per minute
        minute_angle = minute * 6
        
        # Calculate the absolute difference between angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle (acute angle)
        return min(angle, 360 - angle)

# Example usage
clock = ClockAngle()
print(f"Angle at 3:30: {clock.calculate_angle(3, 30):.2f} degrees")
print(f"Angle at 12:00: {clock.calculate_angle(0, 0):.2f} degrees")
print(f"Angle at 6:00: {clock.calculate_angle(6, 0):.2f} degrees")
print(f"Angle at 11:59: {clock.calculate_angle(11, 59):.2f} degrees")

# Time Complexity: O(1) - constant time operations
# Space Complexity: O(1) - only uses a fixed amount of extra space