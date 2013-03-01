import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmcaddon, os
from time import strftime
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.thegeekgroup')
__language__ = __settings__.getLocalizedString

def CATEGORIES():
    # List all the shows.
    shows = {}

    # TGG live stream
    addLink(
        name = __language__(30000),
        url = 'rtsp://thegeekgroup.videocdn.scaleengine.net/thegeekgroup-live/play/thegeekgroup.stream',
        date = '',
        iconimage = os.path.join(__settings__.getAddonInfo('path'), 'resources', 'media', 'tgg.png'),
        info = {
            'title': __language__(30000),
            'plot': __language__(30200),
            'genre': 'Science & Technology',
            'count': 1
        }
    )

# Info takes Plot, date, size
def addLink(name, url, date, iconimage, info):
        ok=True
        liz=xbmcgui.ListItem(name, date, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="video", infoLabels=info )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

CATEGORIES()

xbmcplugin.endOfDirectory(int(sys.argv[1]))



# below is some code i found to play the video by calling the youtube plugin to play it

# needs to be made into proper def
# video_id = 'youtube_video_id'
#playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
#item = xbmcgui.ListItem(path=playback_url)
#xbmcplugin.setResolvedUrl(plugin_handle, True, item)