from django.contrib import admin

class PerwezAdminSite(admin.AdminSite):
    site_header = "🏢 Perwez Associate Admin Panel"
    site_title = "Perwez Admin"
    index_title = "Dashboard"

# Customize the default admin site
admin.site.site_header = "🏢 Perwez Associate Admin"
admin.site.site_title = "Perwez Admin"
admin.site.index_title = "Management Dashboard"

