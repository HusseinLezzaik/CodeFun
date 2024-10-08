"""
Longest Time Span from Date Intervals:
Given a set of date intervals represented by StartDate and EndDate, efficiently calculate the longest timespan covered by them
"""

from typing import List, Tuple
from datetime import datetime, timedelta

def longest_timespan(intervals: List[Tuple[str, str]]) -> int:
    events = []
    for start, end in intervals:
        events.append((datetime.strptime(start, "%Y-%m-%d"), 1))  # 1 for start event
        events.append((datetime.strptime(end, "%Y-%m-%d"), -1))   # -1 for end event
    
    events.sort()  # Sort all events by date
    
    active_intervals = 0
    longest_span = timedelta()
    last_change = None
    
    for date, event_type in events:
        if active_intervals == 0 and event_type == 1:
            last_change = date
        elif active_intervals == 1 and event_type == -1:
            span = date - last_change
            longest_span = max(longest_span, span)
        
        active_intervals += event_type
    
    return longest_span.days

# Example usage
intervals = [
    ("2023-01-01", "2023-03-15"),
    ("2023-02-10", "2023-04-20"),
    ("2023-06-01", "2023-08-15"),
]

result = longest_timespan(intervals)
print(f"The longest timespan is {result} days.")