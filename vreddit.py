import urllib.request
from urllib.request import urlopen, Request
import json
import requests
import gi

import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk



class Handler():

    shareLink = ""

    def onSubmit(self, button):

        entry = builder.get_object("entry")

        output = builder.get_object("output")
        urlinput = entry.get_text()

        copy = builder.get_object("copy")



        #finalurl = get_url(urlinput)

        link = get_url(urlinput)



        print(link)
        copy.show()
        global shareLink
        shareLink = link
        output.set_text(link)

    def onCopy(self, button):
        global shareLink
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(shareLink, -1)
        print(shareLink)



def get_url(url2):
    url2 = url2 + ".json"

    #url = "https://www.reddit.com/r/WhatsWrongWithYourDog/comments/cnefqf/yyou_good_bruh/.json"

    url = url2

    hdr = {'User-Agent' : 'reddit posts to vreddit links!'}

    json_obj = req = requests.get(url, headers=hdr)
    json = json_obj.json()
    link = json[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']

    return link




builder = Gtk.Builder()
builder.add_from_file("ui.glade")

window = builder.get_object("window1")


builder.connect_signals(Handler())

window.connect("destroy", Gtk.main_quit)

window.show_all();



Gtk.main()
