from django.contrib import admin
#from application.models import Company,Organization,Post,Category,Student #import model
from application.models import *

admin.site.register(Post)
admin.site.register(Category)


admin.site.register(Publisher)

admin.site.register(Author)


admin.site.register(City)
admin.site.register(State)

admin.site.register(Post2)



#admin.site.register(Book)

   #title = models.CharField(max_length=100)
    #authors = models.ManyToManyField(Author)

class BookAdmin(admin.ModelAdmin):
    list_display=['title',]
    search_fields=['title',]
    list_filter =['title']
    list_per_page =4  # Add Pagination
admin.site.register(Book,BookAdmin)




class RegistrationAdmin(admin.ModelAdmin):
    list_display=['username','useremail','userpass',]
    search_fields=['username',]
    list_filter =['username']
    list_per_page =4  # Add Pagination
admin.site.register(UserRegistration,RegistrationAdmin)




class PersonAdmin(admin.ModelAdmin):
    list_display=['per_name','father_name','gender','mobile',]
    search_fields=['per_name','father_name','gender','mobile',]
    list_filter =['per_name']
admin.site.register(Person,PersonAdmin)
 


class StudentAdmin(admin.ModelAdmin):
    #list_display=['stu_name','father_name','stu_address','stu_gender','stu_mobile','admin_photo']
    list_display=['stu_name','father_name','stu_address','stu_gender','stu_mobile','admin_thumbnail','stu_status']
    search_fields=['stu_name']
    list_filter =['stu_name']
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):
        pass
    export_as_csv.short_description = "Export Selected"
    
admin.site.register(Student,StudentAdmin)


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=['comp_name','comp_email','comp_code','comp_mobile','comp_address']
    search_fields=['comp_name']
    list_filter =['comp_name']
admin.site.register(Company,CompanyAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display=['orgName','orgEmail','orgContact'] # Add Colums
    list_per_page =4  # Add Pagination
    list_filter =['orgName']
    search_fields=['orgName','orgEmail']
admin.site.register(Organization,OrganizationAdmin)    

# Register your models here.
