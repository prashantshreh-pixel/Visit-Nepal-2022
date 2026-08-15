from hotel_management_system.models import Booking


def check_availability(room, check_in, check_out):
    overlapping_bookings = Booking.objects.filter(
        room=room,
        check_in__lt=check_out,
        check_out__gt=check_in
    )
    return not overlapping_bookings.exists()

