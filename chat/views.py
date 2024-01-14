from typing import Any
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from django.utils.decorators import method_decorator
from .models import RolePlayingRoom
from .forms import RolePlayingRoomForm


@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomCreateView(CreateView):
    model = RolePlayingRoom
    form_class = RolePlayingRoomForm

    def form_vaild(self, form):
        role_playing_room = form.save()
        role_playing_room.user = self.request.user
        return super().form_valid(form)
    

role_playing_room_new = RolePlayingRoomCreateView.as_view()


@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomUpdateView(UpdateView):
    model = RolePlayingRoom
    form_class = RolePlayingRoomForm

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


role_playing_room_edit = RolePlayingRoomUpdateView.as_view()


@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomListView(ListView):
    model = RolePlayingRoom

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

role_playing_room_list = RolePlayingRoomListView.as_view()