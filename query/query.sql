SELECT name, battery_level, version_name, device_id, `timestamp`
FROM app_processes INNER JOIN samples 
ON samples.id = app_processes.sample_id
WHERE `timestamp` >= '01-01-2018 00:00:00'
AND ( NOT battery_state='Charging') AND importance='Foreground app'
AND ( name='com.dts.freefireth' 
OR name='com.supercell.clashroyale' 
OR name='com.nianticlabs.pokemongo' 
OR name='com.igg.android.lordsmobile'
OR name='com.supercell.brawlstars' 
OR name='com.supercell.clashofclans'
OR name='com.king.candycrushsaga' 
OR name='com.mobile.legends'
OR name='com.tencent.ig'
OR name='com.playrix.gardenscapes'
OR name='com.miniclip.eightballpool' 
OR name='com.playrix.township'
OR name='jp.konami.duellinks' 
OR name='com.king.candycrushsodasaga'
OR name='com.kabam.marvelbattle'
OR name='com.hcg.cok.gp'
OR name='com.king.farmheroessaga'
OR name='com.youmusic.magictiles'
OR name='com.kiloo.subwaysurf' 
OR name='com.imangi.templerun2' )
ORDER BY name, device_id, `timestamp`

/* it is important that the phone is not charging because I will analyze its discharge*/

/* Importance can be : Background process, Foreground app, Service
 so I chose the option where the user will be effectively using the app */

 /*
I will not use the application_label, because when I tested some appeared NULL
 */

/*
TOP JOGOS GRATUITOS NO jogos.txt */