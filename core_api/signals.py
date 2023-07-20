def make_faculty_admin():
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    from maps_api.models import Building, Map

    group, created = Group.objects.get_or_create(name="faculty_admin")

    ct_building = ContentType.objects.get_for_model(Building)
    ct_map = ContentType.objects.get_for_model(Map)

    perms_4_building = Permission.objects.filter(content_type=ct_building)
    perms_4_map = Permission.objects.filter(content_type=ct_map)

    for permission in perms_4_building.all():
        group.permissions.add(permission)

    for permission in perms_4_map.all():
        group.permissions.add(permission)


def populate_groups(sender, **kwargs):
    make_faculty_admin()
