# -*- coding: utf-8 -*-

import compatible_uwsc as UWSC

VAL1 = UWSC.INPUT('Please Input Word','Sample...',0)
UWSC.MSGBOX(VAL1,'BTN_OK')

UWSC.SAVEIMAGE('screenshot.png',1,1,1920,1080)

UWSC.MMV(10,15,1000)
UWSC.MMV(100,150,1000)
UWSC.MMV(10,150,1000)
UWSC.MMV(100,15,1000)
UWSC.MMV(50,150,1000)

UWSC.BTN('LEFT',0,100,100,1000)
UWSC.BTN('RIGHT',0,100,100,1000)

UWSC.KBD('ctrl',1,1000)
UWSC.KBD('a',0,1000)
UWSC.KBD('c',0,1000)
UWSC.KBD('ctrl',2,1000)