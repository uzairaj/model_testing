#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pickle
import json
import numpy as np


# In[13]:


#loading all required pickle files

loaded_label = pickle.load(open('mlabel.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
loaded_model = pickle.load(open('tag_suggestion_model.pkl', 'rb'))


# In[19]:


#this function will predict relevant tags based on article test

def pred_article_tags(test_article):

    vec = loaded_vectorizer.transform([test_article])
    r =loaded_model.predict(vec)
    labels = (r > 0.5).astype(np.int)
    labels=loaded_label.inverse_transform(labels)
    resp = json.dumps(labels[0])
    return resp


# In[20]:


if __name__ == "__main__":

    #input article    
    test_article='''The th day Russias military operation Ukraine entered Russia announced declared temporary ceasefire starting  Moscow time evacuation civilian  city Ukraine including capital Kyiv In statement made Defense Management Center Russian Ministry Defense stated humanitarian situation city Ukraine deteriorated Pointing importance ensuring safety civilian foreign citizen statement said Russia declares ceasefire March   Moscow time ready establish humanitarian corridor expression used In statement stated humanitarian aid corridor created evacuation Ukrainian city Kyiv Chernigiv Sumi Kharkiv Mariupol proposed Ukrainian side reach agreement determination working hour corridor  Moscow time What happened th day Donbass operation  Russian Foreign Minister Lavrov arrived Antalya Russian Foreign Minister Sergey Lavrov Antalya RussiaUkraineTurkey trilateral foreign minister meeting held Antalya tomorrow mediation Turkey came The private plane carrying Lavrov Russian delegation landed Antalya Airport The delegation moved star Regnum Carya Hotel Belek Tourism Center Serik district staying Ukrainian Foreign Minister Dmitriy Kuleba expected arrive city hour later The delegation stay separate hotel meet star Regnum Carya Hotel Belek Tourism Center meeting avuolu Lavrov Kuleba hold tripartite meeting tomorrow G Summit  hall world leader former United States President Barack Obama Russian President Vladimir Putin hosted  Russian Ministry Energy In joint statement Russian Ministry Energy Ministry Defense published Telegram channel Russia maximally interested fulfilling gas contract full full fulfillment Russias obligation gas contract full implementation delivery stated related The Russian side maximally concerned fully fulfilling obligation gas contract providing carrying delivery full statement said The statement also noted Gazprom received letter Ukraines GTS Operator Wednesday identifying risk gas transmission station located region Russias operation demilitarize Ukraine  Russian Ministry Defense Ukraine preparing provocation use toxic substance Russian Defense Ministry Spokesperson Igor Konashenkov stated Ukrainian radical nationalist may preparing provocation use toxic substance order accuse Russia using chemical weapon On night March   ton ammonia brought Zolochev settlement northwest Kharkov Ukrainian radical nationalist According account resident left Zolochev radical teach act correctly event chemical attack Konashenkov said  UN representative met representative Russian Ministry Defense Ministry Foreign Affairs Moscow United Nations UN Spokesperson Secretary General Stephane Dujarric Ukraine highlevel meeting UN staff Russian Ministry Foreign Affairs Ministry Defense Russia Moscow He stated discussing humanitarian cooperation Speaking reporter press conference Dujarric said Our colleague Moscow humanitarian aid held highlevel meeting Russian Ministry Foreign Affairs Russian Ministry Defense Participants agreed strengthen cooperation facilitate timely delivery humanitarian assistance people affected crisis Ukraine Dujarric also stated effort build existing coordination mechanism soldier civilian Ukraine since   Blinken Polands offer contains difficulty US Secretary State Antony Blinken stated decision country send weapon fighter jet Ukraine Polands offer place warplane disposal United States sent Ukraine stated difficulty Antony Blinken said country make decision sending weapon warplane Ukraine Commenting Polands statement ready send MiG fighter jet Ukraine US ready send Ramstein airbase Germany place plane USs command Blinken said Polands offer offer difficulty When come security assistance everything right said  Slutskiy We compromise single item meeting Ukraine Leonid Slutskiy member Russian delegation RussiaUkraine talk stated make concession single item Ukrainian side talk In statement Russian medium Slutskiy said The Russian delegation compromise single item talk Slutskiy added preferred talk le issue negotiation difficult  Stoltenberg The nofly zone Ukraine could lead largescale war Europe Speaking conference Canada via videoconference NATO Secretary General Jens Stoltenberg said alliance consider establishing nofly zone Ukraine despite Kievs call Stoltenberg said As nofly zone issue We must understand declaring nofly zone enforced In hostile situation saw Ukraine way massive attack Russian air defense system We cannot provide nofly zone condition Russias existing air defense system This also mean direct clash Russian aircraft This mean direct confrontation NATO Russian air force This lead significant escalation war Ukraine also create risk largescale war Europe participation NATO member said Stoltenberg also noted spread conflict Ukraine must prevented brought end  President Erdoan phone conversation President EU Commission Ursula von der Leyen President Recep Tayyio Erdoan Erdoan phone conversation President EU Commission Ursula von der Leyen During meeting situation Ukraine TurkeyEU relation discussed  World Economic Forum froze relation Russian organization It stated World Economic Forum DEF stopped cooperation people sanctioned due event Ukraine froze relation Russian organization We cooperating anyone sanction frozen relation Russian entities DEF Spokesperson Amanda Russo told Politico  Russian Ministry Defense Russian army evacuated  foreigner Ukraine Novorossiysk Head National Defense Control Center Russian Ministry Defense Mikhail Mizintsev told reporter  foreigner evacuated dangerous area Kherson Novorossiysk Tuesday  Blast attack Italian Embassy Belarus It stated result explosion took place territory Italian Embassy Belarus dead injured claw building broken object inner garden damaged Belarus Charge dAffaires Italy Vladimir Vasilkov said Two attempt made activate explosive device one failed There damage property belonging embassy No one killed injured explained Vasilkov noted evaluated incident terrorist attack due scale fact occurred night In statement made Ministry Foreign Affairs Belarus Italian law enforcement officer arrived scene described incident terrorist act preliminary investigation Experts done necessary research relevant study continuing The Italian authority declared readiness strengthen protection Belarusian Embassy  Russian Ministry Defense Extreme nationalist attacked facility power Chernobyl Nuclear Power Plant  Italian Prime Minister Draghi Sanctions Russia take long time Italian Prime Minister Mario Draghi stated Wests sanction Russia continue long time due escalating tension Ukraine economy ready Answering question parliamentarian Italian House Representatives Draghi said These sanction last long time must proportional possibility order permanent We intention withdrawing sanction policy agreed ally must also everything ensure line internal course Drawing attention fact Italian institution analyze result rising inflation slowing growth Draghi emphasized We ready take possible measure protect purchasing power family support company  The Constitutional Court Russia withdraws Conference European Constitutional Courts The Constitutional Court Russia announced withdrew Conference European Constitutional Courts CECC In statement made Constitutional Court Russia stated March  initiative several court member Conference European Constitutional Courts voting protocol sent member termination suspension membership Constitutional Court Russian Federation  EU expands sanction Russia Managers  company black list Names included EUs black list Sibur Holding Chairman Dmitriy Konov TMK Chairman Mihail Oseyevskiy Uralchem Group CEO Dmitriy Mazepin Fosagro CEO Andrey Guryev Rusagro Chairman Vadim Moshkovic Aeroflot CEO Mihail Poluboyarinov CEO VK Vladimir Kiriyenko President Rosnano Sergey Kulikov  Putin discussed situation Ukraine German Chancellor Scholz In statement made Kremlin reported Russian President Vladimir Putin telephone conversation German Chancellor Olaf Scholz situation Ukraine discussed meeting In statement stated The humanitarian aspect situation Ukraine Donbass republic especially emphasized meeting  Russia The claim Kiev one want leave humanitarian corridor false Stating Russia strictly complies regime silence  humanitarian corridor opened Ukraine Major General Mikhail Mizintsev Head National Center Defense Management Ministry Defense Russian Federation stated Kiev allowed leave humanitarian corridor He stressed claim one wanted go false Mizintsev said In face Ukrainian government claim one want go Russian territory humanitarian corridor openly declare false overt provocation Just past day database Russian Ministry Defense includes  thousand request evacuation Ukrainian foreign civilian Russia There  application said  US director Oliver Stones documentary Ukraine On Fire removed YouTube US director Oliver Stones documentary Ukraine On Fire examines Maydan event Ukraine  agenda recently removed YouTube  Bloomberg Germany prevents Sberbank removed SWIFT system Bloomberg agency referring diplomatic source close subject document possession stated Germanys attitude main obstacle disconnecting Sberbank Russias largest bank SWIFT system reported Berlin leading impetus oppose effort include Sberbank list Russian financial institution cut SWIFT report said According news Germany repeatedly expressed concern possible measure various diplomatic meeting recent day Berlin also concerned Russian proposal restrict access port measure could harm trade nonsanctioned product As quoted agency Germany like EU country opposes banning import Russian energy resource  Yuan deposit service launched Russia interest currency dollar euro increased In statement made Russian VTB bank stated Wednesday March  new deposit product offered customer From bank customer able open yuan time deposit account maximum interest  percent It noted lower limit opening account  yuan In order interest  percent account maturity   month must opened VTB bank previously offered interest rate  percent month deposit account ruble  percent shortterm dollar account  percent euro  German Chancellor Scholz No warplane sent Ukraine German Chancellor Olaf Scholz announced send warplane Ukraine German Chancellor Olaf Scholz said joint press conference meeting Canadian Prime Minister Justin Trudeau country providing financial aid year help Ukraines economy resilient Reminding provided weapon Ukraine addition humanitarian aid Scholz said We need think carefully else concretely This certainly include warplane  Former Bolivian President Morales The reason event Ukraine expansion NATO USA Former Bolivian President Evo Morales stated reason happened Ukraine NATOs enlargement policy led USA Commenting subject Morales told Sputnik This conflict worry whole world We believe military confrontation solution But time must see cause problem situation arises Russia Ukraine said Morales said Bolivia peaceful antiimperialist country according Constitution accept implementation policy expansion intervention institution NATO leadership United States military strategy problem Morales said  Abkhazia establishes diplomatic relation Donetsk Peoples Republic The Ministry Foreign Affairs Abkhazia announced diplomatic relation established Donetsk Peoples Republic today From March   Republic Abkhazia Donetsk Peoples Republic established diplomatic relation exchanging note statement said  Philip Morris stopped operation Russia The world largest tobacco product manufacturer Philip Morris International announced decided stop planned sanction Russia process introducing new product market Stating terminated investment trade innovation manufacturing activity company noted accelerated plan reduce production activity Russia due ongoing supply chain disruption changing legal framework  Companies exiting Russian market nationalized trustee appointed The ruling party United Russia announced government Draft Law Commission approved second economic support package envisages expropriation foreign company asset appointment trustee company According United Russia Partys statement second economic support package still draft law prepared response Western sanction envisages implementation one nationalization mechanism foreign company asset The bill pave way appointing outside management trustee company court decision activity company  percent belong foreign citizen hostile country terminated It stated provide opportunity prevent bankruptcy company continue employment employee company However owner company restarts operation sell share condition business employee continue way waive trustee If happen court appoint temporary management  month old company dissolved share new company put sale The person want buy new company undertake keep least  staff continue activity old company least  year  Russia We destroyed almost Ukraines antiaircraft system Russian Defense Ministry official press conference held regarding special military operation Ukraine said More  percent operational long mediumrange antiaircraft missile system belonging Ukrainian side destroyed  declared Russian official said Ukrainian warplane went Romania participate military operation  Ukrainian Minister Foreign Affairs requested ceasefire Chernobyl Ukrainian Foreign Minister Dmitry Kuleba called ceasefire stating repair made supply electricity Chernobyl Nuclear Power Plant Making statement Twitter Kuleba called international community demand Russia urgently cease attack allow repair team restore power supply adding The backup diesel generator hour capacity power Chernobyl Nuclear Power Plant After time cooling system storage facility spent nuclear fuel stop cause radiation leak  Ukrainian Armed Forces Russian army prepares new attempt seize Kiev The Armed Forces Ukraine announced Russian troop preparing seize capital Kiev According available information enemy preparing new attempt take Kiev press service Ukrainian Armed Forces said statement In statement also noted Russian troop tried start operation unsuccessful attack city Fastiv  Putin Egyptian leader Sisi met Ukraine In statement made Presidency Egypt noted President Abdel Fattah elSisi phone call Russian President Vladimir Putin discus development Ukraine  Donetsk Peoples Republic Kyiv preparing provocation humanitarian corridor In statement made Donetsk Peoples Republic DHC stated Kiev preparing new provocation humanitarian corridor Mariupol Volnovoha mine may laid exit city  British Defense Minister Wallace make speech Ukrainian parliament  Dutch Prime Minister Rutte Closure port Rotterdam Russian ship table yet Dutch Prime Minister Mark Rutte answered question whether closing country port Russian ship added expanded sanction Russia Rutte said The closure Rotterdam port Russian ship table yet seen European Union level  The fourth round RussiaUkraine negotiation fourth round RussiaUkraine peace talk take place LavrovKuleba meeting Turkey held meeting Russian Foreign Minister Sergey Lavrov Ukrainian counterpart Dmitry Kuleba held Turkey tomorrow Belarusian political scientist Yuri Voskresenskiy known close organizer RussiaUkraine peace talk told Rossiya television As far I know fourth round talk take place meeting foreign minister Russia Ukraine Turkey  Zelenskiy We preparing next round negotiation Ukrainian President Zelenskiy told Ukrainian delegation preparing next round negotiation Russia ensure peace According Russian medium outlet TASS Zelenskiy made statement Telegram account stated would listen report Ukrainian delegation met Russia Belarus returned night said We prepare next round negotiation behalf Ukraine name peace  Japan sent military equipment Ukraine Japan sent bulletproof vest helmet tent military equipment Ukraine tonight NHK TV reported Britain banned soldier traveling Ukraine According The Independent newspaper British Ministry Defense banned soldier traveling Ukraine It stated violate decision face disciplinary administrative penalty  USA sends Patriot system Poland US European Command EUCOM Spokesperson Captain Adam Miller announced Washington send  Patriot air defense system missile battery Poland threat USA NATO ally territory  SumiPoltava humanitarian corridor work  Sumi Regional Administration Head Dmitriy Jivitskiy said statement Telegram The negotiation group worked night duration SumiPoltava humanitarian corridor extended The corridor open today   CET According Jivitskiy also possible pas corridor private vehicle  Russia  people including  Turks evacuated Ukraine Crimea armored train The Russian Black Sea Fleet announced  people  Turks evacuated Ukraine Crimea armored train In statement fleet  foreign national  child brought Armyansk city Republic Crimea Kherson Region Ukraine soldier Southern Military District Russia The security transfer foreign citizen city Armyansk carried armored train crew Southern Military District provided In statement stated  Turks  Ukrainians citizen Egypt Azerbaijan Pakistan Sweden Italy Brazil Morocco India among evacuee  Finnish Prime Minister We support sanction including expansion SWIFT blockade Russian bank Finnish Prime Minister Sanna Marin stated support tough sanction targeting Moscow including step expand SWIFT blockade targeting Russian bank  Putin signed Real person Russia able buy gold bullion without VAT Russian President Vladimir Putin signed law foresees abolition  percent VAT sale gold bullion real person March   Earlier Russian Ministry Finance stated light unstable geopolitical situation investing gold ideal alternative investing dollar Russian citizen With law aimed direct individual investor gold bullion sufficient Russias reserve  EU permanent representative agreed expand sanction Russian business people family member In statement made Elysee Palace stated permanent representative European Union EU agreed expansion sanction Russian business people family member In statement also noted  Belarusian bank also agreed remove SWIFT system  Gazprom Gas transfer Ukraine continues usual Gazprom announced gas transfer Europe via Ukraine continue usual today  million cubic meter gas sent according buyer order In  Gazproms contractual obligation gas transfer Ukraine amount  million cubic meter per day total  billion cubic meter per year  Russian Foreign Affairs Lavrov leaf today tomorrow meeting Russian Foreign Ministry Spokesperson Mariya Zakharova said Foreign Minister Lavrov leave Moscow today go Turkey meet Ukrainian counterpart Kuleba tomorrow The meeting Lavrov Kuleba meet first time since Russia launched special military operation Ukraine take place mediation Foreign Minister Mevlt avuolu The meeting also highestlevel contact Russia Ukraine since start operation In peace talk held Russian Ukrainian delegation concrete result achieved far apart evacuation civilian Ukrainian city temporary ceasefire implemented evacuation Russian Foreign Ministry official previously noted meeting foreign minister Russia Ukraine Turkey held Antalya tomorrow held line agreement reached phone call Russian President Vladimir Putin President Erdogan Sunday  Greece EU take measure increase natural gas price Greek Prime Minister Kiryakos Mitsotakis asked EU take measure protect consumer rapidly increasing natural gas price Mitsotakis letter sent EU Commission President Ursula Von der Leyen stated EUs effort deal problem insufficient said The paradox neither production capacity natural gas supply chain affected current crisis This quantity It mean dont problem problem price said  A violent explosion occurred Lugansk Sputnik news agency correspondent reported violent explosion took place Lugansk It yet known caused explosion recorded center Lugansk facility targeted whether death injury result explosion  Russia found  weapon Zaporozhye Nuclear Power Plant The Russian National Guard Rosgvardiya announced  weapon Zaporozhye Nuclear Power Plant came control Russia It stated power unit power plant contain firearm also large amount ammunition A colonel Rosgvardiya said While power plant control large amount ammunition including heavy weapon found search operation These munition power unit station In word serious defensive war prepared said  China provide  million yuan worth humanitarian aid Ukraine In statement made Chinese Ministry Foreign Affairs Chinese Red Cross announced provide  million yuan worth humanitarian aid Ukraine consisting supply  EU Commission President von der Leyen We imported lot LNG dependent Russian gas end winter European Union EU Commission President Ursula von der Leyen said need natural gas imported Russia end winter highly liquefied He stated purchasing natural gas LNG   According Anadolu Agency Ukrainian Foreign Minister Kuleba said The meeting planned held March  held primarily thanks Turkish Foreign Minister Mevlt avuolu  Russia reduces use dollar foreign currency reserve foreign payment Dmitriy Birichevskiy Head Department Economic Cooperation Russian Ministry Foreign Affairs told Sputnik Due strengthening sanction Russia reducing use US dollar foreign currency reserve foreign payment moving nonWestern capital market said  US accept Polands offer The United States accept Polands offer send MiG fighter jet US airbase Germany sent Ukraine The Pentagon said statement sending combat aircraft NATO zone war zone raise serious concern entire NATO alliance However according written statement US European Command European Commander General Tod Wolters announced ordered two Patriot air defense battery sent Poland  New sanction UK Russian aviation industry The UK announced new sanction authorize detain Russian aircraft arriving country ban export good used aerospace industry Russia With new sanction considered crime Russian plane fly land UK The British Foreign Office said statement subject The ban include power seize aircraft owned operated leased person designated person entity associated Russia aircraft owned person affiliated Russia  Blinken discussed Ukraine crisis UAE Minister Foreign Affairs Antony Blinken US Minister Foreign Affairs discussed Ukraine crisis speaking United Arab Emirates UAE Foreign Minister Sheikh Abdullah bin Zayed alNahyan According WAM agency meeting importance reaching political consensus Ukraine emphasized  Zakharova The US biolaboratories Ukraine direct threat country Russian Ministry Foreign Affairs Spokesperson Mariya Zakharova interview Radio Sputnik regarding biolaboratories USA Ukraine This USAs Ukraine It completely change picture Turkeys involvement fate Turkey This mean influence deterrence tool direct threat country said Zaharova added activity organization stopped would spiraled control later  US European Command announces  Patriot battery sent Poland defensive purpose In statement reported two Patriot battery responsibility US European Command African Command deployed Poland upon invitation Poland instruction General Wolters The statement noted battery question purely defensive purpose pointed missile way intended attack  The evacuation approximately  thousand people Ukraine completed Ukrainian Presidential Office Deputy Kiril Tymoshenko stated evacuation approximately  thousand people Ukrainian city Sumi completed announced Turkish citizen among evacuated  Fitch downgrade Russias credit rating International credit rating agency Fitch Ratings downgraded Russias credit rating B C In statement stated said credit rating reflects view country default imminent stated development weakened Russias willingness pay public debt In statement noted escalation sanction proposal'''
    result = pred_article_tags(test_article)
    
    print(result)


# In[ ]:




