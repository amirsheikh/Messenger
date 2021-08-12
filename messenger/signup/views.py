from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from profileapp.models import UserProfile
from django.contrib.auth.password_validation import validate_password
import phonenumbers
# Create your views here.
def signup(request):
    if  request.method == "POST" and User.objects.filter(username = request.POST.get('username')).exists():
        messages.error(request,"این اکانت قبلا ثبت شده است.")
        return redirect('/')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
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
            return redirect('/')
        
        try:
            phonenumber = phonenumbers.parse(username,'IR')
            if(not phonenumbers.is_valid_number(phonenumber)):
                messages.error(request,'شماره وارد شده نادرست است.')
                return redirect('/')
        except:
            messages.error(request,'شما باید شماره تلفن خود را وارد کنید.')
            return redirect('/')
        saveUser = User.objects.create_user(username, 
        password = password,
        first_name = request.POST.get('name'))
        Userpro = UserProfile(user = saveUser)
        Userpro.save()
        messages.info(request,"اکانت شما با موفقیت ساخته شد.") 
        return redirect('/')