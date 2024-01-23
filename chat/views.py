from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from gtts import gTTS

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


@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomDetailView(DetailView):
    model = RolePlayingRoom

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
    
role_playing_room_detail = RolePlayingRoomDetailView.as_view()


@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomDeleteView(DeleteView):
    model = RolePlayingRoom
    success_url = reverse_lazy("role_playing_room_list")

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
    
    def form_vaild(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "채팅방을 삭제했습니다.")
        return response
    
role_playing_room_delete = RolePlayingRoomDeleteView.as_view()


@staff_member_required
def make_voice(request: HttpRequest) -> HttpResponse:
    lang = request.GET.get("lang", "en")

    message = request.GET.get("message")

    response = HttpResponse()

    gTTS(message, lang=lang).write_to_fp(response)

    response["content-Type"] = "audio/mpeg"

    return response