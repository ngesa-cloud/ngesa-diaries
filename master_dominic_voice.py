import asyncio
import os
import subprocess
import edge_tts

VOICE = "sw-KE-RafikiNeural"
RATE = "+8%"
PITCH = "+26Hz"

EPISODES_DOMINIC = [
    {
        "id": "ep001",
        "script": (
            "Kulikua na kisa kule Kisii na Homa Bay... watu wamelala fofofo saa nane za usiku, "
            "ghafla unaskia mchanga unamwagwa kwa bati! Twa twa twa! Na unadhani ni mwizi? "
            "La hasha! Ni Night Runner akikimbia uchi porini na kurusha cheche za moto! "
            "Wanakijiji wakiamka, mbwa hawabweki na hakuna hata unyayo! "
            "Wanapita vichakani kwa kasi ya ajabu bila kuchomwa na miiba. "
            "Wazee wanasema ni urithi wa damu kutoka vizazi vya kale. "
            "Maze, unadhani ni mchezo? Eeh, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 01: Night Runners wa Western Kenya. "
            "Uchunguzi wetu unathibitisha tabia hii si ya wizi bali ni compulsion ya kurithi. "
            "Hakuna madhara ya kimwili yanayoripotiwa lakini athari ya kisaikolojia kwa jamii ni kubwa sana. "
            "Kesi imefungwa chini ya hadhi ya Folkoric Anomalous Phenomenon. Eeh, hii ni mwecheche!"
        )
    },
    {
        "id": "ep002",
        "script": (
            "Maze skia hii story bana... Ngong Road saa tisa za usiku katikati ya msitu mnene wa Karen. "
            "Basi nyekundu ya zamani ya KBS namba 666 inatokea kwenye kona bila taa wala sauti ya injini! "
            "Dereva ametazama mbele haongei, makanga amesimama mlangoni hana uso, "
            "lakini ndani abiria wamejaa wametulia kimya kabisa. "
            "Na watu waka-board hiyo basi! Wanaingia lakini hakuna anayeshuka Nairobi mzima! "
            "Asubuhi ikifika, unakuta gari imeyeyuka kwenye ukungu wa msitu. "
            "Bana, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 02: Ghost Bus ya Ngong Road KBS 666. "
            "Rekodi za Kenya Bus Services za miaka ya tisini zinaonyesha basi hili lilipata ajali mbaya "
            "bila manusura. Tangu hapo mashahidi zaidi ya arobaini wameripoti kuiona "
            "katika maeneo yale yale saa tisa usiku. Tahadhari: Usijaribu kusimamisha gari hili."
        )
    },
    {
        "id": "ep003",
        "script": (
            "Imagine ukienda Menengai Crater Nakuru... mahali panaitwa Kirima kia Ngoma, kilima cha mashetani! "
            "Watu wakitembea jioni wanaskia ngoma zikilia chini ya ardhi na sauti zikiita majina yao. "
            "Mwaka wa 1854 maelfu ya mashujaa wa Maasai walisukumwa kwenye kreta hii wakati wa vita. "
            "Hadi leo watalii na wachungaji wanapotea bila viatu, "
            "na watu wakapiga picha... picha inatoka moshi na vivuli vya kutisha! "
            "Watu wa eneo hilo wanajua jioni ikifika, hutakiwi kutazama ndani ya shimo hilo. "
            "Eeh, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 03: Kirima kia Ngoma, Menengai Caldera. "
            "Shimo lenye kina cha mita mia tano na miamba ya volkano. "
            "Uchunguzi wa kijiolojia unaonyesha gesi ya sulfur inaweza kusababisha hallucinations, "
            "lakini haielezi kupotea kwa watu bila unyayo wala sauti za ngoma zinazosikika usiku."
        )
    },
    {
        "id": "ep004",
        "script": (
            "Mombasa raha, sivyo? Lakini tembea Mama Ngina Waterfront saa nane za usiku uone mambo! "
            "Upepo wa bahari unavuma kwa baridi, ghafla unatokeza mwanamume mtanashati mwenye sauti tamu, "
            "amevaa kanzu safi ya kizungu na kofia ya heshima. Anakusalimia kwa lugha ya staha. "
            "Lakini ukitazama chini kwa mchanga... miguu yake si ya binadamu! "
            "Ni kwato mbili za mbuzi zilizogawanyika! "
            "Na watu bado wakamsalimia kabla hawajagundua! "
            "Ukipiga kelele anayeyuka na kubaki harufu ya udi na ubani. "
            "Maze, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 04: The Cloven-Footed Jinn wa Mama Ngina. "
            "Visiwa vya Pwani vina rekodi ndefu za majini na viumbe vya baharini. "
            "Uthibitisho wa kimwili uliokusanywa ni alama za kwato za wanyama zisizo na mfuatano "
            "katika mchanga wa Mama Ngina Drive. Ushauri wa kiusalama: Usiongee na wageni usiku wa manane."
        )
    },
    {
        "id": "ep005",
        "script": (
            "Kila Mkenya aliyesoma boarding anajua hii story ya kutisha! "
            "Bweni la zamani la shule za Limuru na Meru lililojengwa juu ya makaburi ya enzi za ukoloni. "
            "Saa tisa za usiku wakati kila mtu amelala, kengele ya chuma inaanza kulia yenyewe! Ding! Dong! "
            "Kisha unaskia viatu virefu vya high heels vikitembea polepole kwa corridor tupu ya saruji! "
            "Clack! Clack! Clack! "
            "Milango inafunguka yenyewe, blanketi zinavutwa kutoka vitandani, "
            "na wasichana wakatoroka kupitia madirishani! "
            "Asubuhi wakichunguza, hakuna mtu yeyote aliyekuwemo! "
            "Eeh, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 05: Boarding School Crypt Hauntings. "
            "Historia ya miaka ya 1930 inaonyesha baadhi ya hosteli zilijengwa juu ya "
            "maeneo ya makaburi ya walowezi na wamisionari. "
            "Ripoti za acoustic anomalies na psychogenic mass incidents zimerekodiwa rasmi."
        )
    },
    {
        "id": "ep006",
        "script": (
            "Highway ya Nakuru kuelekea Eldoret pale Kikopey Flats... barabara iliyonyooka lakini giza ni totoro. "
            "Madereva wa malori ya masafa marefu wanasimulia kisa cha mwanamke aliyevaa gauni jeupe la harusi, "
            "amesimama kando ya lami akiinua mkono kuomba lifti kwenye baridi kali. "
            "Dereva mwenye huruma akasimamisha gari na kumkaribisha kwenye kiti cha mbele. "
            "Baada ya kilomita tano dereva akimtazama, kiti kiko wazi kabisa, "
            "lakini harufu ya maua ya makaburini imetanda garini na breki zinakata ghafla! "
            "Wengi wamepoteza maisha kwenye kona hiyo. "
            "Bana, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 06: The Vanishing Lady wa Kikopey. "
            "Eneo hili la highway lina historia ya ajali nyingi zisizoelezeka za magari. "
            "Ingawa wataalamu wanasema ni uchovu wa madereva, "
            "ushuhuda wa madereva zaidi ya thelathini una maelezo sawa ya mwanamke mweupe."
        )
    },
    {
        "id": "ep007",
        "script": (
            "Hii si hadithi ya kubuni, hii ni ukweli mzito na mchungu wa msitu wa Chakama kule Shakahola. "
            "Ekari mia nane za msitu wa miiba katika kaunti ya Kilifi, "
            "mahali ambapo mamia ya waumini walidanganywa kufunga chakula na maji hadi kufa "
            "ili wakutane na muumba wao kabla ya mwisho wa dunia. "
            "Wachunguzi walipoingia ndani ya msitu huo, walikuta makaburi ya halaiki yaliyofukiwa kwa siri. "
            "Hata baada ya miezi kadhaa, ukimya wa msitu huo unatia hofu moyoni. "
            "Ni ushahidi wa jinsi imani potovu inavyoweza kugeuka kuwa mauti ya kutisha. "
            "Giza hapa lina siri kubwa!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 07: Shakahola Cult Forensics. "
            "Uchunguzi wa kitabibu na kiintelijensia wa tukio baya zaidi la itikadi kali nchini Kenya. "
            "Miili zaidi ya mia nne na thelathini ilipatikana katika maeneo mbalimbali ya msitu. "
            "Kesi hii inabaki kuwa kumbukumbu ya hatari ya manipolyesheni ya kisaikolojia."
        )
    },
    {
        "id": "ep008",
        "script": (
            "Msitu mkubwa wa Kakamega na vilele vya vilima vya Nandi... "
            "wazee wa kabila la Nandi na Luhya wanamfahamu kiumbe anayeitwa Chemosit au Nandi Bear! "
            "Wanasema ni mnyama mkubwa nusu simba nusu mtu, mwenye manyoya mekundu, "
            "anayetembea kwa miguu miwili na kutoa kicheko kama binadamu gizani! "
            "Hakai chini bali anajificha juu ya matawi ya miti mirefu akingoja mtu apite peke yake, "
            "kisha anaruka na kumpiga kichwani ili ale ubongo tu na kuacha mwili mzima! "
            "Watafiti wa Kizungu walijaribu kumwinda miaka ya 1920 lakini wakaishia kukimbia! "
            "Maze, unadhani ni hekaya za watoto? Eeh, hii ni mwecheche!"
        ),
        "ai_script": (
            "Dossier Analysis ya Case 08: Chemosit Cryptid Investigation. "
            "Ripoti za kihistoria kutoka kwa maafisa wa kikoloni kama C.W. Hobley na Geoffrey Williams "
            "zilithibitisha kuwepo kwa mnyama asiyetambuliwa wa jamii ya hyena au dubu wa kale. "
            "Hadi leo msitu wa Kakamega una mafumbo ambayo sayansi haijapata majibu yake."
        )
    }
]

async def master_all():
    os.makedirs("audio", exist_ok=True)
    
    for ep in EPISODES_DOMINIC:
        ep_id = ep["id"]
        print(f"\n==========================================")
        print(f"🎙️ Generating Episode: {ep_id} in Dominic Narration Style")
        print(f"==========================================")
        
        # 1. Synthesize Episode Audio
        raw_ep_file = f"audio/{ep_id}_raw.mp3"
        master_ep_file = f"audio/{ep_id}.mp3"
        
        comm = edge_tts.Communicate(ep["script"], voice=VOICE, rate=RATE, pitch=PITCH)
        await comm.save(raw_ep_file)
        
        # 2. Master Episode with Dominic Presence EQ and EBU R128 (-16.4 LUFS)
        subprocess.run([
            "ffmpeg", "-y", "-i", raw_ep_file,
            "-af", "equalizer=f=3200:t=q:w=1.5:g=3.5,equalizer=f=250:t=q:w=1.0:g=1.5,loudnorm=I=-16:TP=-1.5:LRA=9",
            "-b:a", "192k", master_ep_file
        ], check=True)
        os.remove(raw_ep_file)
        print(f"✔ Mastered Episode: {master_ep_file}")
        
        # 3. Synthesize AI Debrief Audio
        ep_num = ep_id.replace("ep00", "").replace("ep0", "")
        ai_raw_file = f"audio/ai_case0{ep_num}_raw.mp3"
        ai_master_file = f"audio/ai_case0{ep_num}.mp3"
        
        comm_ai = edge_tts.Communicate(ep["ai_script"], voice=VOICE, rate=RATE, pitch=PITCH)
        await comm_ai.save(ai_raw_file)
        
        # 4. Master AI Debrief
        subprocess.run([
            "ffmpeg", "-y", "-i", ai_raw_file,
            "-af", "equalizer=f=3200:t=q:w=1.5:g=3.5,equalizer=f=250:t=q:w=1.0:g=1.5,loudnorm=I=-16:TP=-1.5:LRA=9",
            "-b:a", "192k", ai_master_file
        ], check=True)
        os.remove(ai_raw_file)
        print(f"✔ Mastered AI Debrief: {ai_master_file}")

if __name__ == "__main__":
    asyncio.run(master_all())
