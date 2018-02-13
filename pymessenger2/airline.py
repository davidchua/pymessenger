import attr


@attr.s
class AirlineItinerary(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template
    """
    intro_message = attr.ib(convert=str)
    pnr_number = attr.ib(convert=str)
    passenger_info = attr.ib()
    flight_info = attr.ib()
    passenger_segment_info = attr.ib()
    total_price = attr.ib(convert=int)
    currency = attr.ib(convert=str)
    locale = attr.ib(default='en_US')
    price_info = attr.ib(default=None)
    base_price = attr.ib(default=None)
    tax = attr.ib(default=None)
    theme_color = attr.ib(default=None)
    template_type = attr.ib(default='airline_itinerary')


@attr.s
class PassengerInfo(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#passenger_info
    """
    passenger_id = attr.ib(convert=str)
    name = attr.ib(convert=str)
    ticket_number = attr.ib(default=None)


@attr.s
class FlightInfo(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#flight_info
    """
    connection_id = attr.ib(convert=str)
    segment_id = attr.ib(convert=str)
    flight_number = attr.ib(convert=str)
    departure_airport = attr.ib()
    arrival_airport = attr.ib()
    flight_schedule = attr.ib()
    travel_class = attr.ib(convert=str)
    aircraft_type = attr.ib(default=None)


@attr.s
class FlightSchedule(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#flight_schedule

    Times have to be given in yyyy-mm-ddThh:mm
    """
    departure_time = attr.ib(convert=str)
    arrival_time = attr.ib(convert=str)
    boarding_time = attr.ib(default=None)


@attr.s
class Airport(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#airport
    """
    airport_code = attr.ib(convert=str)
    city = attr.ib(convert=str)
    terminal = attr.ib(default=None)
    gate = attr.ib(default=None)


@attr.s
class PassengerSegmentInfo(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#passenger_segment_info
    """
    segment_id = attr.ib(convert=str)
    passenger_id = attr.ib(convert=str)
    seat = attr.ib(convert=str)
    seat_type = attr.ib(convert=str)
    product_info = attr.ib(default=None)


@attr.s
class PriceInfo(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template#price_info
    """
    title = attr.ib(convert=str)
    amount = attr.ib(convert=int)
    currency = attr.ib(default=None)
