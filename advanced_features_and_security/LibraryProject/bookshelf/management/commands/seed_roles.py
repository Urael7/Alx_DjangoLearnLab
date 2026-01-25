from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book


class Command(BaseCommand):
    help = "Create default groups (Viewers, Editors, Admins) and assign permissions for Book"

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Book)

        # Custom permissions defined on Book
        perms_codenames = {
            'can_view': 'Can view books',
            'can_create': 'Can create books',
            'can_edit': 'Can edit books',
            'can_delete': 'Can delete books',
        }

        # Ensure permissions exist (created by post_migrate normally)
        created_perms = {}
        for codename, name in perms_codenames.items():
            perm, _ = Permission.objects.get_or_create(
                content_type=content_type, codename=codename, defaults={'name': name}
            )
            created_perms[codename] = perm

        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        viewers.permissions.set([created_perms['can_view']])
        editors.permissions.set([
            created_perms['can_view'],
            created_perms['can_create'],
            created_perms['can_edit'],
        ])
        admins.permissions.set([
            created_perms['can_view'],
            created_perms['can_create'],
            created_perms['can_edit'],
            created_perms['can_delete'],
        ])

        self.stdout.write(self.style.SUCCESS('Seeded groups and permissions successfully.'))
