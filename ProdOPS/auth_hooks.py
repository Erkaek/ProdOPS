"""Hook into Alliance Auth"""

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# ProdOPS
# AA ProdOPS App
from ProdOPS import urls


class ProdOPSMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("ProdOPS App"),
            "fas fa-cube fa-fw",
            "ProdOPS:index",
            navactive=["ProdOPS:"],
        )

    def render(self, request):
        """Render the menu item"""

        if request.user.has_perm("ProdOPS.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return ProdOPSMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(urls, "ProdOPS", r"^ProdOPS/")
