import urllib.request
from urllib.request import urlopen, Request
import json
import requests
import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class Handler():


    def onSubmit(self, button):

        entry = builder.get_object("entry")

        output = builder.get_object("output")
        urlinput = entry.get_text()


        #finalurl = get_url(urlinput)

        link = get_url(urlinput)



        print(link)


        output.set_text(link)

        copy_text(link);

def get_url(url2):
    url2 = url2 + ".json"

    #url = "https://www.reddit.com/r/WhatsWrongWithYourDog/comments/cnefqf/yyou_good_bruh/.json"

    url = url2

    hdr = {'User-Agent' : 'reddit posts to vreddit links!'}

    json_obj = req = requests.get(url, headers=hdr)
    json = json_obj.json()
    link = json[0]["data"]["children"][0]['data']['url']

    return link




builder = Gtk.Builder()
builder.add_from_file("ui.glade")

window = builder.get_object("window1")


builder.connect_signals(Handler())

window.show_all();

Gtk.main()
