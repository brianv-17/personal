from django.contrib import admin
from spicyapp.models import User
from spicyapp.models import Comment
from spicyapp.models import Suggestion
from spicyapp.models import Videoone
from spicyapp.models import Videotwo
from spicyapp.models import Videothree

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Suggestion)
admin.site.register(Videoone)
admin.site.register(Videotwo)
admin.site.register(Videothree)

