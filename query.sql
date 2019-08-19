SELECT distinct device_id
FROM app_processes INNER JOIN samples 
ON samples.id = app_processes.sample_id
WHERE name='com.kiloo.subwaysurf' AND ( NOT battery_state='Charging')
ORDER BY device_id 


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
*/