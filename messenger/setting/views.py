from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from profileapp.models import UserProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
@login_required
def editprofile(request):
    if  request.method == "POST":
        if "image" in request.FILES:
            User = UserProfile.objects.get_or_create(user = request.user)
            User[0].avatar = request.FILES["image"]
            User[0].save()
            messages.info(request,"تصویر با موفقیت بارگزاری شد.")
        name = request.POST.get("name")
        password = request.POST.get("password")
        if(name != ""):
            request.user.first_name = name
            request.user.save()
            messages.info(request,"نام با موفقیت تغییر کرد.")
        if(password != ""):
            try:
                validate_password(password, user=None, password_validators=None)
            except Exception as pass_vaildators:
                for pass_vaildator in pass_vaildators:
                    if('short' in pass_vaildator):
                        messages.error(request,"رمز عبور وارد شده کوتاه است و حداقل باید دارای 8 حرف باشد.")
                    if('common' in pass_vaildator):
                        messages.error(request,"رمزعبور از عبارات قابل حدس استفاده کرده است.")
                    if('numeric' in pass_vaildator):
                        messages.error(request,"در رمز عبور فقط از اعداد استفاده شده است.") 
                    else:
                        messages.error(request,pass_vaildator)
                redirect("/")
            print(password)
            request.user.set_password(password)
            request.user.save()
            messages.info(request,"پسورد با موفقیت تغییر کرد.")
    return redirect("/")
