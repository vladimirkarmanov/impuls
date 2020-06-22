from django.urls import path

from .views import DialogsView, MessagesView, CreateDialogView

urlpatterns = [
    path('', DialogsView.as_view(), name='dialogs'),
    path('<int:chat_id>/', MessagesView.as_view(), name='messages'),
    path('create/<int:user_id>/', CreateDialogView.as_view(), name='create_dialog'),
]
