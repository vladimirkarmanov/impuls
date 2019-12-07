from django.contrib import admin

from .models import Event, EventOrganizer, EventDate, PressRelease


class EventDateInline(admin.TabularInline):
    model = EventDate


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (EventDateInline,)
    list_display = ('name', 'organizer', 'get_start_dates')
    list_display_links = ('name',)
    list_filter = ('dates__start_date',)
    search_fields = ('name',)

    def get_start_dates(self, obj) -> str:
        return ' | '.join(str(date.start_date) for date in obj.dates.all())

    get_start_dates.short_description = 'Даты начала'
    get_start_dates.admin_order_field = 'dates__start_date'

    class Meta:
        model = Event


@admin.register(EventOrganizer)
class EventOrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'get_events')
    list_display_links = ('name',)
    list_filter = ('events__dates__start_date',)
    search_fields = ('name',)

    def get_events(self, obj) -> str:
        return ' | '.join(str(event.name) for event in obj.events.all())

    get_events.short_description = 'Мероприятия'

    class Meta:
        model = EventOrganizer


@admin.register(EventDate)
class EventDateAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'event')
    list_display_links = ('start_date',)
    list_filter = ('start_date',)
    search_fields = ('start_date', 'end_date')

    class Meta:
        model = EventDate


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('file', 'event_date')
    list_display_links = ('event_date',)
    search_fields = ('file',)

    class Meta:
        model = PressRelease
