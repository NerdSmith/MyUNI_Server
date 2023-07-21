def set_all_model_perms_4_group(group, model):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType

    ct = ContentType.objects.get_for_model(model)

    perms_4_model = Permission.objects.filter(content_type=ct)

    for permission in perms_4_model.all():
        group.permissions.add(permission)


def make_faculty_admin():
    from django.contrib.auth.models import Group

    from maps_api.models import Building, Map
    from wvs_api.models import WV
    from publications_api.models import PubTag, PubGroup, Publication, PubPicture

    group, created = Group.objects.get_or_create(name="faculty_admin")

    # maps_api
    set_all_model_perms_4_group(group, Building)
    set_all_model_perms_4_group(group, Map)
    # maps_api end

    # wvs_api
    set_all_model_perms_4_group(group, WV)
    # wvs_api end

    # publications_api
    set_all_model_perms_4_group(group, PubTag)
    set_all_model_perms_4_group(group, PubGroup)
    set_all_model_perms_4_group(group, Publication)
    set_all_model_perms_4_group(group, PubPicture)
    # publications_api end


def make_direction_admin():
    from django.contrib.auth.models import Group
    from manual_api.models import Subject, InfoPost

    group, created = Group.objects.get_or_create(name="direction_admin")

    # manual_api
    set_all_model_perms_4_group(group, Subject)
    set_all_model_perms_4_group(group, InfoPost)
    # manual_api end


def make_course_group_admin():
    from django.contrib.auth.models import Group

    group, created = Group.objects.get_or_create(name="course_group_admin")

    # core_api
    from core_api.models import CourseGroup
    set_all_model_perms_4_group(group, CourseGroup)
    # core_api end

    # event_api
    from event_api.models import Event
    set_all_model_perms_4_group(group, Event)
    # event_api end

    # schedule_api
    from schedule_api.models import Schedule
    set_all_model_perms_4_group(group, Schedule)
    # schedule_api end


def populate_groups(sender, **kwargs):
    make_faculty_admin()
    make_direction_admin()
    make_course_group_admin()
