from user import User
from privileges import Privileges
from admin import Admin

my_admin = Admin('igor', 'dias', 32323232, 26)
my_admin.privilege.show_privileges()