from aqt.main import AnkiQt
from aqt.addons import AddonsDialog

old_sync = AnkiQt._sync
def _sync(self):
    old_sync(self)
    ad =AddonsDialog(self.addonManager)
    if hasattr(ad, "onCheckForUpdates"):
        #version at most 19
        ad.onCheckForUpdates()
    else:
        #version at least 20
        ad.check_for_updates()
    ad.reject()
    
AnkiQt._sync = _sync
