# Django Permisssion and Groups Setup

## Perrmissions:
'can_create' : Allows a user to create books.
'can_edit' : Allows a user to edit books.
'can_delete' : Allows a user to delete books.

## Groups:
**Viewers**: Can only view books.
**Editors**: Can edit books.
**Admins**: Can create, edit, and delete books.

## Setup Instructions:
1. Run migrations.
2. Assogn users to groups in Django Admin.
3. Test by logging in with different users.