import pytz
from datetime import datetime
import jdatetime


class HelpersForDate:
    def extend_date(self, date_string):
        """
        Extends a date string to the full datetime string if it is only a date.

        Args:
            date_string (str): a date string in "YYYY-MM-DD" format

        Returns:
            str: the full datetime string in "YYYY-MM-DD HH:MM:SS" format
        """
        if len(date_string) == 10:  # YYYY-MM-DD
            return f"{date_string} 00:00:00"
        return date_string

    def date_to_unix_timestamp(self, date_string, format="%Y-%m-%d %H:%M:%S", timezone="UTC"):
        """
        Converts a date string to its Unix timestamp in milliseconds.

        Args:
            date_string (str): a date string in the given format
            format (str): the format of the date string (default: "%Y-%m-%d %H:%M:%S")
            timezone (str): the timezone of the date string (default: "UTC")

        Returns:
            int: the Unix timestamp of the date string in milliseconds
        """
        ff = self.extend_date(date_string)
        dt = datetime.strptime(ff, format)
        tz = pytz.timezone(timezone)
        dt = tz.localize(dt)
        dt_utc = dt.astimezone(pytz.UTC)
        timestamp_milliseconds = int(dt_utc.timestamp() * 1000)
        return timestamp_milliseconds

    def get_day_range(self, date_string, timezone="UTC"):
        """
        Returns a tuple of two integers representing the start and end Unix timestamps
        of a given date string in the given timezone.

        Args:
            date_string (str): a date string in "YYYY-MM-DD" format
            timezone (str): the timezone of the date string (default: "UTC")

        Returns:
            tuple: a tuple of two integers representing the start and end timestamps
                   of a given date string in the given timezone
        """
        start_date = f"{date_string} 00:00:00"
        end_date = f"{date_string} 23:59:59"
        start_timestamp = self.date_to_unix_timestamp(start_date, timezone=timezone)
        end_timestamp = self.date_to_unix_timestamp(end_date, timezone=timezone) + 1000  # Add 1 second in milliseconds
        return start_timestamp, end_timestamp

    @classmethod
    def convert_gregorian_to_shamsi(cls, date_str):
        # Convert the date string to a datetime object
        """
        Converts a Gregorian date string to a Shamsi date string.

        Args:
            date_str (str): a date string in "YYYY-MM-DD" format

        Returns:
            str: the Shamsi date string in "YYYY-MM-DD" format
        """
        gregorian_date = datetime.strptime(date_str, '%Y-%m-%d')
        # Convert Gregorian datetime to Shamsi datetime
        shamsi_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
        # Return the Shamsi date formatted as yyyy-mm-dd
        return shamsi_date.strftime('%Y-%m-%d')