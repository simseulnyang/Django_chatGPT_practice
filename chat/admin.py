from django.contrib import admin

from .forms import RolePlayingRoomForm
from .models import RolePlayingRoom


@admin.register(RolePlayingRoom)
class RolePlayingRoomAdmin(admin.ModelAdmin):
    form = RolePlayingRoomForm

    # save request.user if form is valid
    def save_model(self, request, obj, form, change):
        # 신규 생성에서만 reqeust.user를 할당
        if change is False and form.is_valid():
            obj.user = request.user

        super().save_model(request, obj, form, change)