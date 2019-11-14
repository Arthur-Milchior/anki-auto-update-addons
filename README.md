# Update add-ons at start
## Rationale
I don't want to have to think about updating my add-ons. So this
add-on synchronizes add-ons when the collection is synchronized.

It uses the same process for updating as Anki. That is, it updates
only add-ons installed using the add-on manager. And you can decide to
update all or none of the add-ons.

## Warning
This add-on uses Anki's default update method, and so has the same limitation:
it only updates all or none of the add-ons.

## Version 2.0
None

## Internal
It modifies:
* `aqt.main.AnkiQt._sync` by calling the previous version of this
  function and then asking addonDialog for update

## TODO
* Being able to synchronize only some add-ons.

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-auto-update-addons
Addon number| [1847544206](https://ankiweb.net/shared/info/1847544206)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
