SELECT name, battery_level, version_name, device_id, `timestamp`
FROM app_processes INNER JOIN samples 
ON samples.id = app_processes.sample_id
WHERE ( NOT battery_state='Charging') AND importance='Foreground app'
AND ( name='com.dts.freefireth' OR name='com.slippy.linerusher' 
OR name='com.innersloth.spacemafia' OR name='com.playgendary.tom'
OR name='com.kiloo.subwaysurf' OR name='com.cassette.aquapark'
/* OR name='com.roblox.client'*/ OR name='com.dpspace.rocketsky'
OR name='com.crazylabs.lady.bug' OR name='com.tencent.iglite'
OR name='com.tapped.flipdunk' OR name='com.youmusic.magictiles'
/* OR name= 'me.pou.app' */ OR name='com.water.balls'
/* OR name='com.outfit7.mytalkingtom' */ OR name='com.mojang.minecrafttrialpe'
OR name='com.mgc.runnergame' OR name='com.amanotes.beathopper'
OR name='com.miniclip.eightballpool' OR name='com.rovio.baba'
OR name='com.supercell.brawlstars' )
ORDER BY name, device_id, `timestamp`

/* it is important that the phone is not charging because I will analyze its discharge*/

/* Importance can be : Background process, Foreground app, Service
 so I chose the option where the user will be effectively using the app */

 /*
I will not use the application_label, because when I tested some appeared NULL
 */

/*
Top jogos Gratuitos
{https://play.google.com/store/apps/top/category/GAME?hl=pt_BR}
    Garena Free Fire: com.dts.freefireth
    Fun Race 3D: com.slippy.linerusher
    Among Us: com.innersloth.spacemafia
    Tomb of the Mask: com.playgendary.tom
    Subway Surfers: com.kiloo.subwaysurf
    aquapark.io: com.cassette.aquapark
    * ROBLOX: com.roblox.client
    Rocket Sky!: com.dpspace.rocketsky
    Miraculous: Ladybug & Gato Noir Jogo Oficial: com.crazylabs.lady.bug
    PUBG MOBILE LITE: com.tencent.iglite
    Flip Dunk: com.tapped.flipdunk
    Magic Tiles 3: com.youmusic.magictiles
    *Pou : me.pou.app
    Sand Balls: com.water.balls
    *Meu Talking Tom 2: com.outfit7.mytalkingtom
    Teste do Minecraft: com.mojang.minecrafttrialpe
    Run Race - Corrida 3D: com.mgc.runnergame
    Tiles Hop: Forever Dancing Ball: com.amanotes.beathopper
    8 Ball Pool: com.miniclip.eightballpool
    Angry Birds 2: com.rovio.baba
    ---
    Brawl Stars: com.supercell.brawlstars

    these games with * have no well-defined genre 
*/
