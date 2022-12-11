from app.models import User

userarray = User.objects.all()
lat = []
lng = []
for user in userarray:
    if user.is_student and user.lat:
        lat.append(user.lat)
        lng.append(user.lng)
locations = zip(lat, lng)
