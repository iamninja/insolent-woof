import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Goodbye World!"
line2 = "And welcome back"
line3 = "My own Add-On"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)