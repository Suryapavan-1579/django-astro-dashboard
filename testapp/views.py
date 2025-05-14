from django.shortcuts import render
import datetime, random

# Create your views here.
def astro_view(request):
    msg_list = [
        "The stars are aligning in your favor—trust the timing of your life.",
        "This is your reminder: you are exactly where you're meant to be.",
        "A shift in energy is coming—stay open to unexpected blessings.",
        "The universe is guiding you—listen to your intuition.",
        "Big changes are ahead, but you're more than ready.",
        "You’re shedding old layers—transformation is never comfortable, but always necessary.",
        "Let go of what no longer serves you. Space must be made for the new.",
        "Your personal evolution is accelerating—embrace it fully.",
        "Growth comes when you stop doubting yourself and start trusting your journey.",
        "Love is on the horizon—open your heart to receive.",
        "A new connection is forming—be clear about what you truly desire.",
        "You’re attracting the kind of love that reflects your self-worth.",
        "Old wounds may resurface—heal them to move forward in love.",
        "Opportunities are opening up—don’t hesitate to step into your power.",
        "Your hard work is about to pay off—stay focused and grounded.",
        "You’re being called to align your work with your purpose.",
        "This is a powerful time to set intentions for your career path."
        ]
    

    # names = ["Surya","Pavan","Kumar","Lakshman","Sriram"]

    time = datetime.datetime.now()

    h = int(time.strftime("%H"))

    if h<=12:
        s = "Good Morning"
    elif h<=16:
        s = "Good Afternoon"
    elif h<=21:
        s= "Good Evening"
    else:
        s = "Good Night"

    msg = random.choice(msg_list)
    
    if request.method == "POST":
        name = request.POST.get("username")
       
        my_dict = {"time": time, "name": name, "msg": msg, "wish": s}
        return render(request, "testapp/astrohome.html", my_dict)
    else:
        return render(request, "testapp/astrohome.html")
    


    # name = random.choice(names)

    # msg = random.choice(msg_list)

    # my_dict = {"time":time ,"name":name,"msg":msg , "wish":s}

    # return render(request,"testapp/astrohome.html", my_dict)