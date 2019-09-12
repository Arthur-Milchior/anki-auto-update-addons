from aqt.main import AnkiQt
from aqt.addons import AddonsDialog

old_sync = AnkiQt._sync
def _sync(self):
    old_sync(self)
    ad =AddonsDialog(self.addonManager)
    ad.onCheckForUpdates()
    ad.reject()
    
AnkiQt._sync = _sync
