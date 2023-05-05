# -*- coding: UTF-8 -*-
import csv
import bibtexparser
from rdflib import Graph


authormap={"L. Kröger":"http://data.archaeology.link/data/spphaefen/l_kroeger","M. Foucher":"http://data.archaeology.link/data/spphaefen/m_foucher"}
publicationmap={}
projectmap={"SPP-Im Netzwerk fluvialer Häfen":"https://gepris.dfg.de/gepris/projekt/198801704","Binnenhäfen/Inland harbours":"https://gepris.dfg.de/gepris/projekt/219647198"}
place_technique={"logboat":"http://www.wikidata.org/entity/Q596073","keelboat":"http://www.wikidata.org/entity/Q60520969","flat-bottomed vessel":"http://www.wikidata.org/entity/Q5457690","raft":"http://www.wikidata.org/entity/Q200433"}
countries={"Turkey":"http://www.wikidata.org/entity/Q43","Armenia":"http://www.wikidata.org/entity/Q399","Austria":"http://www.wikidata.org/entity/Q40","Bosnia and Herzegovina":"http://www.wikidata.org/entity/Q225","Britain, England":"http://www.wikidata.org/entity/Q21","Britain, Northern Ireland":"http://www.wikidata.org/entity/Q26","Britain, Scotland":"http://www.wikidata.org/entity/Q22","Britain, Wales":"http://www.wikidata.org/entity/Q25","Bulgaria":"http://www.wikidata.org/entity/Q219","Croatia":"http://www.wikidata.org/entity/Q224","Czech Republic":"http://www.wikidata.org/entity/Q213","Denmark":"http://www.wikidata.org/entity/Q35","Estonia":"http://www.wikidata.org/entity/Q191","Finland":"http://www.wikidata.org/entity/Q33","France":"http://www.wikidata.org/entity/Q142","Greece":"http://www.wikidata.org/entity/Q41","Hungary":"http://www.wikidata.org/entity/Q28","Italy":"http://www.wikidata.org/entity/Q38","Latvia":"http://www.wikidata.org/entity/Q211","Lithuania":"http://www.wikidata.org/entity/Q37","Netherlands":"http://www.wikidata.org/entity/Q55","Norway":"http://www.wikidata.org/entity/Q20","Poland":"http://www.wikidata.org/entity/Q36","Portugal":"http://www.wikidata.org/entity/Q45","Romania":"http://www.wikidata.org/entity/Q218","Serbia":"http://www.wikidata.org/entity/Q403","Russia":"http://www.wikidata.org/entity/Q159","Slovenia":"http://www.wikidata.org/entity/Q215","Spain":"http://www.wikidata.org/entity/Q29","Ireland":"http://www.wikidata.org/entity/Q27","Sweden":"http://www.wikidata.org/entity/Q34","Belgium":"http://www.wikidata.org/entity/Q31","Germany":"http://www.wikidata.org/entity/Q183","Ukraine":"http://www.wikidata.org/entity/Q212","Switzerland":"http://www.wikidata.org/entity/Q39"}
bodyofwater={"Ladoga":"http://www.wikidata.org/entity/Q15288","Barup Sø":"http://www.wikidata.org/entity/Q12302949","Moyola":"http://www.wikidata.org/entity/Q7337651","Carse Loch":"http://www.wikidata.org/entity/Q5046860","Kozjak":"http://www.wikidata.org/entity/Q12634812","Julsø":"http://www.wikidata.org/entity/Q12320531","Knudsø":"http://www.wikidata.org/entity/Q12322383","Vejle Å":"http://www.wikidata.org/entity/Q12340648","Kolmikulmalampi":"http://www.wikidata.org/entity/Q66586754","Sèvre Niortaise":"http://www.wikidata.org/entity/Q1225928","Etang de Thau":"http://www.wikidata.org/entity/Q288968","Adour":"http://www.wikidata.org/entity/Q207366","Lesum":"http://www.wikidata.org/entity/Q445963","Hohen Sprenzer See":"http://www.wikidata.org/entity/Q1623603","Kastorfer See":"http://www.wikidata.org/entity/Q1381520","Sude":"http://www.wikidata.org/entity/Q314552","Altmühl":"http://www.wikidata.org/entity/Q317060","Bederkesaer":"http://www.wikidata.org/entity/Q813840","Lac de Grand-Lieu":"http://www.wikidata.org/entity/Q3215452","Dordogne":"http://www.wikidata.org/entity/Q208174","Ognon":"http://www.wikidata.org/entity/Q286477","Witham":"http://www.wikidata.org/entity/Q917000","Ribble":"http://www.wikidata.org/entity/Q7337746","L'Arroux":"http://www.wikidata.org/entity/Q702925","Tissø":"http://www.wikidata.org/entity/Q11951950","Lac d'Annecy":"http://www.wikidata.org/entity/Q576704","Yonne":"http://www.wikidata.org/entity/Q213967","Doubs":"http://www.wikidata.org/entity/Q14372","Loch Urr":"http://www.wikidata.org/entity/Q24636549","Loch of Kinnordy":"http://www.wikidata.org/entity/Q65058560","Loch Ard":"http://www.wikidata.org/entity/Q952227","Lea Shun":"http://www.wikidata.org/entity/Q24640574","Jizera":"http://www.wikidata.org/entity/Q582675","Bednja":"http://www.wikidata.org/entity/Q1278490","Cesma":"http://www.wikidata.org/entity/Q340080","Una":"http://www.wikidata.org/entity/Q212927","Bosut":"http://www.wikidata.org/entity/Q2911647","Brežnica":"http://www.wikidata.org/entity/Q25300509","Jablanica":"http://www.wikidata.org/entity/Q1288026","Hamble":"http://www.wikidata.org/entity/Q7337483","Upper Lough Erne":"http://www.wikidata.org/entity/Q11878874","Jezioro Wigry":"http://www.wikidata.org/entity/Q1576094","Jezioro Wieleckie":"http://www.wikidata.org/entity/Q35715958","Jezioro Lazno":"http://www.wikidata.org/entity/Q9394207","Jezioro Mukrz":"http://www.wikidata.org/entity/Q11786542","Jeziora Morskie Oko":"http://www.wikidata.org/entity/Q163246","Majcz Wielki":"http://www.wikidata.org/entity/Q49305233","Lough Dargan":"http://www.wikidata.org/entity/Q33243866","Ballagh Lough":"http://www.wikidata.org/entity/Q33227853","Niers":"http://www.wikidata.org/entity/Q835333","Lough Carra":"http://www.wikidata.org/entity/Q1871364","Västra Älten":"http://www.wikidata.org/entity/Q17608577","Cetina":"http://www.wikidata.org/entity/Q522100","Taute":"http://www.wikidata.org/entity/Q1748366","Vitsø Nor":"http://www.wikidata.org/entity/Q12341189","Vestersø":"http://www.wikidata.org/entity/Q23732884","Slåensø":"http://www.wikidata.org/entity/Q23738207","Gudensø":"http://www.wikidata.org/entity/Q12314529","Fiskbæk":"http://www.wikidata.org/entity/Q23748287","River Forth":"http://www.wikidata.org/entity/Q2421","River Conon":"http://www.wikidata.org/entity/Q7337300","Dernaglar Loch":"http://www.wikidata.org/entity/Q24652268","River Sillees":"http://www.wikidata.org/entity/Q7515345","Quharity Burn":"http://www.wikidata.org/entity/Q24639160","Carlingwark Loch":"http://www.wikidata.org/entity/Q15207592","Craigston Burn":"http://www.wikidata.org/entity/Q112148685","Portmore Lough":"http://www.wikidata.org/entity/Q3777117","Larne Lough":"http://www.wikidata.org/entity/Q3756436","Swale":"http://www.wikidata.org/entity/Q3396347","Hutovo Blato":"http://www.wikidata.org/entity/Q21729484","Wallersee":"http://www.wikidata.org/entity/Q2542762","River Tyne":"http://www.wikidata.org/entity/Q216373","Lea":"http://www.wikidata.org/entity/Q511413","Tern":"http://www.wikidata.org/entity/Q2404982","Clyde":"http://www.wikidata.org/entity/Q19721","Allier":"http://www.wikidata.org/entity/Q2464","Garonne":"http://www.wikidata.org/entity/Q5077","Meurthe":"http://www.wikidata.org/entity/Q1160441","Arnon":"http://www.wikidata.org/entity/Q222884","Saone":"http://www.wikidata.org/entity/Q187834","Bolzsee":"http://www.wikidata.org/entity/Q31917557","Erdre":"http://www.wikidata.org/entity/Q1349493","Loiter Au":"http://www.wikidata.org/entity/Q5511767","Oberucker See":"http://www.wikidata.org/entity/Q826366","Havetofter See":"http://www.wikidata.org/entity/Q96610949","Werbelinsee":"http://www.wikidata.org/entity/Q2560025","Kesselsee":"http://www.wikidata.org/entity/Q1471239","Randow":"http://www.wikidata.org/entity/Q570235","Kleine Müritz":"http://www.wikidata.org/entity/Q829970","Uzunkul":"http://www.wikidata.org/entity/Q4469925","Geeste":"http://www.wikidata.org/entity/Q453203","Springsee":"http://www.wikidata.org/entity/Q1275495","Hunte":"http://www.wikidata.org/entity/Q708447","Leine":"http://www.wikidata.org/entity/Q161051","Dümmer":"http://www.wikidata.org/entity/Q688459","Dosse":"http://www.wikidata.org/entity/Q646005","Kleiner Zernsee":"http://www.wikidata.org/entity/Q32065809","Malchiner See":"http://www.wikidata.org/entity/Q315359","Ruhr":"http://www.wikidata.org/entity/Q1664","Düstersee":"http://www.wikidata.org/entity/Q1272437","Achterwasser":"http://www.wikidata.org/entity/Q340980","Balksee":"http://www.wikidata.org/entity/Q805098","Leine":"http://www.wikidata.org/entity/Q161051","Sorge":"http://www.wikidata.org/entity/Q320162","Medem":"http://www.wikidata.org/entity/Q896137","Pflegersee":"http://www.wikidata.org/entity/Q2084210","Enz":"http://www.wikidata.org/entity/Q14071","Faule Trave":"http://www.wikidata.org/entity/Q32751987","Scharsee":"http://www.wikidata.org/entity/Q369353","Alte Elde":"http://www.wikidata.org/entity/Q32213531","Ohre":"http://www.wikidata.org/entity/Q695628","Dumme":"http://www.wikidata.org/entity/Q32746929","Klenz-See":"http://www.wikidata.org/entity/Q1774117","River Finn":"http://www.wikidata.org/entity/Q1817926","Lough Annagh":"http://www.wikidata.org/entity/Q107092252","River Inny":"http://www.wikidata.org/entity/Q1410635","Monalty Lake":"http://www.wikidata.org/entity/Q33290147","Lago Viverone":"http://www.wikidata.org/entity/Q1800441","Plateliai-See":"http://www.wikidata.org/entity/Q2464737","Noord":"http://www.wikidata.org/entity/Q1899552","Ara":"http://www.wikidata.org/entity/Q3359300","Jezioro Charzykowskie":"http://www.wikidata.org/entity/Q4973783","Jezioro Radunskie":"http://www.wikidata.org/entity/Q4973619","Lednickie":"http://www.wikidata.org/entity/Q6512708","San":"http://www.wikidata.org/entity/Q216488","Somes":"http://www.wikidata.org/entity/Q217401","Teleajen":"http://www.wikidata.org/entity/Q3517273","Lough Ree":"http://www.wikidata.org/entity/Q608133","Lago di Varese":"http://www.wikidata.org/entity/Q542913","Diebel-See":"http://www.wikidata.org/entity/Q31953220","Nurzec":"http://www.wikidata.org/entity/Q1889871","Persante":"http://www.wikidata.org/entity/Q2071851","Lahn":"http://www.wikidata.org/entity/Q103148","Erft":"http://www.wikidata.org/entity/Q708840","Nidda":"http://www.wikidata.org/entity/Q706133","Mill Lough":"http://www.wikidata.org/entity/Q112633187","Llyn Llydaw":"http://www.wikidata.org/entity/Q3086201","Llyn Peris":"http://www.wikidata.org/entity/Q3401781","Schliersee":"http://www.wikidata.org/entity/Q834157","Treene":"http://www.wikidata.org/entity/Q20777","Steißlingersee":"http://www.wikidata.org/entity/Q57996126","Anfora Canal":"http://www.wikidata.org/entity/Q33179736","Tyasmin":"http://www.wikidata.org/entity/Q960750","Loch Awe":"http://www.wikidata.org/entity/Q1368230","Lac de Sanguinet":"http://www.wikidata.org/entity/Q3591682","River Blackwater":"http://www.wikidata.org/entity/Q2905610","Bistrita":"http://www.wikidata.org/entity/Q794131","Rhône":"http://www.wikidata.org/entity/Q602","March":"http://www.wikidata.org/entity/Q179251","Drava":"http://www.wikidata.org/entity/Q171009","River Roe":"http://www.wikidata.org/entity/Q2074865","Medway":"http://www.wikidata.org/entity/Q1434222","Mettmach":"http://www.wikidata.org/entity/Q21866043","River Spey":"http://www.wikidata.org/entity/Q19720","River Nith":"http://www.wikidata.org/entity/Q2557007","Schwinge":"http://www.wikidata.org/entity/Q317130","Müritz":"http://www.wikidata.org/entity/Q3369","Schweriner See":"http://www.wikidata.org/entity/Q311217","River Marron":"http://www.wikidata.org/entity/Q7337621","Dijle":"http://www.wikidata.org/entity/Q934226","Zwin":"http://www.wikidata.org/entity/Q36856","Finstertaler See":"http://www.wikidata.org/entity/Q104868183","Inn":"http://www.wikidata.org/entity/Q14369","Salzach":"http://www.wikidata.org/entity/Q152661","Pfrunger Ried":"http://www.wikidata.org/entity/Q1803391","Rößlerweiher":"http://www.wikidata.org/entity/Q110313254","Conventer See":"http://www.wikidata.org/entity/Q1129374","Saar":"http://www.wikidata.org/entity/Q153972","Peene":"http://www.wikidata.org/entity/Q1658","Vättern":"http://www.wikidata.org/entity/Q188195","Vänern":"http://www.wikidata.org/entity/Q173596","Zihl":"http://www.wikidata.org/entity/Q24792","Moossee":"http://www.wikidata.org/entity/Q664238","Kolindsund":"http://www.wikidata.org/entity/Q980101","Bølling Sø":"http://www.wikidata.org/entity/Q1020215","River Bann":"http://www.wikidata.org/entity/Q3072966","Ancholme":"http://www.wikidata.org/entity/Q7337082","Arun":"http://www.wikidata.org/entity/Q1111197","Schelde":"http://www.wikidata.org/entity/Q37620","Escaut":"http://www.wikidata.org/entity/Q37620","Alter See":"http://www.wikidata.org/entity/Q31877907","Theiß":"http://www.wikidata.org/entity/Q134350","Neiße":"http://www.wikidata.org/entity/Q5602","Boyle River":"http://www.wikidata.org/entity/Q13630268","Shannon":"http://www.wikidata.org/entity/Q192820","Lough Lene":"http://www.wikidata.org/entity/Q1633096","River Suck":"http://www.wikidata.org/entity/Q1719907","Lough Gowna":"http://www.wikidata.org/entity/Q3545409","River Clare":"http://www.wikidata.org/entity/Q614174","Jezioro Biale":"http://www.wikidata.org/entity/Q27704120","Brda":"http://www.wikidata.org/entity/Q772970","Jezioro Sominko":"http://www.wikidata.org/entity/Q9339450","Czarna":"http://www.wikidata.org/entity/Q1149245","Motlawa":"http://www.wikidata.org/entity/Q1950176","Zürich See":"http://www.wikidata.org/entity/Q14407","Oskol":"http://www.wikidata.org/entity/Q540067","Slovechna":"http://www.wikidata.org/entity/Q1848929","Dnepr":"http://www.wikidata.org/entity/Q40855","Derry River":"http://www.wikidata.org/entity/Q32728019","Atlantic":"http://www.wikidata.org/entity/Q97","Adria":"http://www.wikidata.org/entity/Q13924","Mastis":"http://www.wikidata.org/entity/Q12664718","Lage Vaart":"http://www.wikidata.org/entity/Q2091352","Swiniec":"http://www.wikidata.org/entity/Q8082246","Protva":"http://www.wikidata.org/entity/Q1467086","Geistsee":"http://www.wikidata.org/entity/Q166359","Eider":"http://www.wikidata.org/entity/Q3314","Vechte":"http://www.wikidata.org/entity/Q168904","Teufelsmoor":"http://www.wikidata.org/entity/Q897333","Saale":"http://www.wikidata.org/entity/Q1678","Tauchowsee":"http://www.wikidata.org/entity/Q32750658","Langbürgner See":"http://www.wikidata.org/entity/Q1569749","Arlau":"http://www.wikidata.org/entity/Q315952","Müggelsee":"http://www.wikidata.org/entity/Q694789","Briesener See":"http://www.wikidata.org/entity/Q21041917","Kudensee":"http://www.wikidata.org/entity/Q1791011","Severn":"http://www.wikidata.org/entity/Q19682","Wear":"http://www.wikidata.org/entity/Q1433715","Uecker":"http://www.wikidata.org/entity/Q704775","Werse":"http://www.wikidata.org/entity/Q2452","Granziner See":"http://www.wikidata.org/entity/Q1543300","Isar":"http://www.wikidata.org/entity/Q106588","Degersee":"http://www.wikidata.org/entity/Q1182865","Schlavenkensee":"http://www.wikidata.org/entity/Q32285343","Glienicker See":"http://www.wikidata.org/entity/Q882857","Bocholter Aa":"http://www.wikidata.org/entity/Q572262","Lower Lough Erne":"http://www.wikidata.org/entity/Q6875872","Colne":"http://www.wikidata.org/entity/Q629755","Tyne":"http://www.wikidata.org/entity/Q216373","Thames":"http://www.wikidata.org/entity/Q19686","Trent":"http://www.wikidata.org/entity/Q19714","Grünwaldsee":"http://www.wikidata.org/entity/Q21871441","Wadag":"http://www.wikidata.org/entity/Q2090677","Narew":"http://www.wikidata.org/entity/Q60055","Ialomita":"http://www.wikidata.org/entity/Q726693","Mura":"http://www.wikidata.org/entity/Q204040","Stettiner Haff":"http://www.wikidata.org/entity/Q161385","Skrovlingen":"http://www.wikidata.org/entity/Q18188209","Dommel":"http://www.wikidata.org/entity/Q1238549","River Shannon":"http://www.wikidata.org/entity/Q192820","Lago Maggiore":"http://www.wikidata.org/entity/Q14379","Clonlea Lough":"http://www.wikidata.org/entity/Q33239831","River Avoca":"http://www.wikidata.org/entity/Q2390594","Lago di Bertignano":"http://www.wikidata.org/entity/Q3825905","Po":"http://www.wikidata.org/entity/Q643","Gardasee":"http://www.wikidata.org/entity/Q6414","Bolsena":"http://www.wikidata.org/entity/Q208180","Ledrosee":"http://www.wikidata.org/entity/Q1407745","Kromme Rijn":"http://www.wikidata.org/entity/Q338833","Piave":"http://www.wikidata.org/entity/Q213462","Oglio":"http://www.wikidata.org/entity/Q848670","Niemen":"http://www.wikidata.org/entity/Q5622","Nisser":"http://www.wikidata.org/entity/Q1633266","Vistula":"http://www.wikidata.org/entity/Q548","Rospuda":"http://www.wikidata.org/entity/Q576707","Bibersee":"http://www.wikidata.org/entity/Q22691357","Kvillebäcken":"http://www.wikidata.org/entity/Q32272449","Sempachersee":"http://www.wikidata.org/entity/Q14459","Wörther See":"http://www.wikidata.org/entity/Q2596539","Klopeiner See":"http://www.wikidata.org/entity/Q687150","Obertrumer See":"http://www.wikidata.org/entity/Q1727088","River Arun":"http://www.wikidata.org/entity/Q261603","Great Ouse":"http://www.wikidata.org/entity/Q19716","Barmsee":"http://www.wikidata.org/entity/Q808393","Kilnamar Lough":"http://www.wikidata.org/entity/Q33266843","River Glyde":"http://www.wikidata.org/entity/Q7337463","Schluchsee":"http://www.wikidata.org/entity/Q835671","Sandrach":"http://www.wikidata.org/entity/Q833033","Zierker See":"http://www.wikidata.org/entity/Q199102","Tollense":"http://www.wikidata.org/entity/Q678026","Fulda":"http://www.wikidata.org/entity/Q6434","Lac de Paladru":"http://www.wikidata.org/entity/Q3215502","Lake of Annecy":"http://www.wikidata.org/entity/Q18564755","Barhapple Loch":"http://www.wikidata.org/entity/Q24656403","Aller":"http://www.wikidata.org/entity/Q1967803","Emscher":"http://www.wikidata.org/entity/Q504922","Falkenseebach":"http://www.wikidata.org/entity/Q1394272","Breiter Luzin":"http://www.wikidata.org/entity/Q826491","Großer Fürstenseer See":"http://www.wikidata.org/entity/Q1548683","Hemmelsdorfer See":"http://www.wikidata.org/entity/Q765875","Großer Schierensee":"http://www.wikidata.org/entity/Q1548950","Schwennenzer See":"http://www.wikidata.org/entity/Q1670059","Broklandsau":"http://www.wikidata.org/entity/Q925970","Kummerower See":"http://www.wikidata.org/entity/Q688154","Uchter Moor":"http://www.wikidata.org/entity/Q1549190","Glambecksee":"http://www.wikidata.org/entity/Q32033070","Windebyer Noor":"http://www.wikidata.org/entity/Q896807","Kilnamar Lough":"http://www.wikidata.org/entity/Q33266843","River Slaney":"http://www.wikidata.org/entity/Q1122203","Lough Scur":"http://www.wikidata.org/entity/Q24196364","River Feale":"http://www.wikidata.org/entity/Q1413986","River Suir":"http://www.wikidata.org/entity/Q1128134","Lough Gill":"http://www.wikidata.org/entity/Q1010499","River Boyne":"http://www.wikidata.org/entity/Q896037","Lough Corrib":"http://www.wikidata.org/entity/Q848917","Lago di Comabbio":"http://www.wikidata.org/entity/Q1094718","Guadalquivir":"http://www.wikidata.org/entity/Q14309","Wauwilermoos":"http://www.wikidata.org/entity/Q2552836","Dittligsee":"http://www.wikidata.org/entity/Q461874","Vierwaldstätter See":"http://www.wikidata.org/entity/Q14381","River Moyola":"http://www.wikidata.org/entity/Q7337651","Kupa":"http://www.wikidata.org/entity/Q211046","Birksø":"http://www.wikidata.org/entity/Q12303550","Arendsee":"http://www.wikidata.org/entity/Q641949","Bornhöveder See":"http://www.wikidata.org/entity/Q893993","Dornach-Ried":"http://www.wikidata.org/entity/Q31971497","Haddebyer Noor":"http://www.wikidata.org/entity/Q896799","Königseggsee":"http://www.wikidata.org/entity/Q22692643","Alster":"http://www.wikidata.org/entity/Q1219","Werra":"http://www.wikidata.org/entity/Q6424","Waupacksee":"http://www.wikidata.org/entity/Q2552837","Walchensee":"http://www.wikidata.org/entity/Q174645","Cloonacolly Lough":"http://www.wikidata.org/entity/Q33239874","Lough O'Flynn":"http://www.wikidata.org/entity/Q24196551","Lough Croan":"http://www.wikidata.org/entity/Q33282560","Levallinree Lough":"http://www.wikidata.org/entity/Q33272988","River Barrow":"http://www.wikidata.org/entity/Q936301","River Erne":"http://www.wikidata.org/entity/Q122766","Nieuwe Maas":"http://www.wikidata.org/entity/Q1362309","Glatzer Neiße":"http://www.wikidata.org/entity/Q1455991","Baldeggersee":"http://www.wikidata.org/entity/Q14509","Zihlkanal":"http://www.wikidata.org/entity/Q202788","Inkwilersee":"http://www.wikidata.org/entity/Q458858","Hüttwilersee":"http://www.wikidata.org/entity/Q689321","Somme":"http://www.wikidata.org/entity/Q37646", "Moselle":"http://www.wikidata.org/entity/Q1667","Havel":"http://www.wikidata.org/entity/Q1682","Pfäffikersee":"http://www.wikidata.org/entity/Q14514","Lago di Nemi":"http://www.wikidata.org/entity/Q33285225","Lough Rahavarrig":"http://www.wikidata.org/entity/Q33285225","Neuburger See":"http://www.wikidata.org/entity/Q1871350","Lough Arrow":"http://www.wikidata.org/entity/Q1871350","Ems":"http://www.wikidata.org/entity/Q1648","Lough Owel":"http://www.wikidata.org/entity/Q2702889","River Quoile":"http://www.wikidata.org/entity/Q3332405","Lac de Chalain":"http://www.wikidata.org/entity/Q1799622","Saône":"http://www.wikidata.org/entity/Q187834","Kilbirnie Loch":"http://www.wikidata.org/entity/Q6406556","Loch Arthur":"http://www.wikidata.org/entity/Q24657046","River Tay":"http://www.wikidata.org/entity/Q19719", "Mosel":"http://www.wikidata.org/entity/Q1667","Lago Trasimeno":"http://www.wikidata.org/entity/Q188487","Bacchiglione":"http://www.wikidata.org/entity/Q1242186","Jezioro Mausz":"http://www.wikidata.org/entity/Q4745402","Jezioro Lednickie":"http://www.wikidata.org/entity/Q6512708","Wolchow":"http://www.wikidata.org/entity/Q15243","Loch Kinord":"http://www.wikidata.org/entity/Q6664930", "Loch Laggan":"http://www.wikidata.org/entity/Q6664933", "Neckar":"http://www.wikidata.org/entity/Q1673", "Chiemsee":"http://www.wikidata.org/entity/Q4138", "Charente":"http://www.wikidata.org/entity/Q123362", "Lippe":"http://www.wikidata.org/entity/Q153945", "Starnberger See":"http://www.wikidata.org/entity/Q131615", "Steinhuder Meer":"http://www.wikidata.org/entity/Q165782", "River Moy":"http://www.wikidata.org/entity/Q1149711", "Lago di Bientina":"http://www.wikidata.org/entity/Q3825910", "Lago di Monate":"http://www.wikidata.org/entity/Q2259119", "Mersey":"http://www.wikidata.org/entity/Q19724","Lough Oughter":"http://www.wikidata.org/entity/Q3756406", "Ziese":"http://www.wikidata.org/entity/Q199218", "Lough Derravaragh":"http://www.wikidata.org/entity/Q1586768", "Zugersee":"http://www.wikidata.org/entity/Q14436", "Ägerisee":"http://www.wikidata.org/entity/Q14507", "Federsee":"http://www.wikidata.org/entity/Q248234", "Haine":"http://www.wikidata.org/entity/Q1569447", "Vorskla":"http://www.wikidata.org/entity/Q844041","River Foyle":"http://www.wikidata.org/entity/Q958530", "River Trent":"http://www.wikidata.org/entity/Q19714", "Seine":"http://www.wikidata.org/entity/Q1471","Brivet":"http://www.wikidata.org/entity/Q178081", "River Clyde":"http://www.wikidata.org/entity/Q19721", "River Thames":"http://www.wikidata.org/entity/Q19686", "Ljubljanica":"http://www.wikidata.org/entity/Q339990","Mlosina":"http://www.wikidata.org/entity/Q11142243", "Amstel":"http://www.wikidata.org/entity/Q185405", "Elblag":"http://www.wikidata.org/entity/Q32750600", "North Sea":"http://www.wikidata.org/entity/Q1693", "Ijssel":"http://www.wikidata.org/entity/Q217818", "Dnjepr":"http://www.wikidata.org/entity/Q40855","Elbe":"http://www.wikidata.org/entity/Q1644", "Styr":"http://www.wikidata.org/entity/Q1136609", "Strupino":"http://www.wikidata.org/entity/Q9347030", "Warta":"http://www.wikidata.org/entity/Q201823", "Omulew":"http://www.wikidata.org/entity/Q2023557","Oder":"http://www.wikidata.org/entity/Q552", "Arve":"http://www.wikidata.org/entity/Q633819", "Lake Constance":"http://www.wikidata.org/entity/Q4127", "Bieler See":"http://www.wikidata.org/entity/Q14429", "Lough Neagh":"http://www.wikidata.org/entity/Q206942", "Lough Gara":"http://www.wikidata.org/entity/Q6686123", "Desna":"http://www.wikidata.org/entity/Q202796", "Oka":"http://www.wikidata.org/entity/Q172089", "Main":"http://www.wikidata.org/entity/Q1670", "Lough Allen":"http://www.wikidata.org/entity/Q1366974", "Lough Cullin":"http://www.wikidata.org/entity/Q3776431", "Waal":"http://www.wikidata.org/entity/Q216171", "Baltic Sea":"http://www.wikidata.org/entity/Q545", "Loch Doon":"http://www.wikidata.org/entity/Q1547670", "Lough Ennell":"http://www.wikidata.org/entity/Q2639357","Loire":"http://www.wikidata.org/entity/Q1469","Lough Gara":"http://www.wikidata.org/entity/Q6686123", "Breedogue River":"http://www.wikidata.org/entity/Q32535533","Loch Glashan":"http://www.wikidata.org/entity/Q3776179", "Lough Beg":"http://www.wikidata.org/entity/Q24196547", "Lough Rea":"http://www.wikidata.org/entity/Q24196547", "Weser":"http://www.wikidata.org/entity/Q1650","Spree":"http://www.wikidata.org/entity/Q1684","Mediterranean Sea":"http://www.wikidata.org/entity/Q4918","Brenta":"http://www.wikidata.org/entity/Q214551","Nidelva":"http://www.wikidata.org/entity/Q499668","Oude Rijn":"http://www.wikidata.org/entity/Q1345836", "Adda":"http://www.wikidata.org/entity/Q63109","Arno":"http://www.wikidata.org/entity/Q115457","Lago di Fimon":"http://www.wikidata.org/entity/Q3825951","Ijsselmeer":"http://www.wikidata.org/entity/Q4121", "Rotte":"http://www.wikidata.org/entity/Q674294","Maas":"http://www.wikidata.org/entity/Q41986", "Rhine":"http://www.wikidata.org/entity/Q584", "Vecht":"http://www.wikidata.org/entity/Q168904","Weichsel":"http://www.wikidata.org/entity/Q548","Derwitzer See":"http://www.wikidata.org/entity/Q317486", "Genfer See":"http://www.wikidata.org/entity/Q6403","Murtensee":"http://www.wikidata.org/entity/Q14448","Danube":"http://www.wikidata.org/entity/Q1653","Don":"http://www.wikidata.org/entity/Q1229"}


def bibtexToRDF(triples,entries,ns,nsont):
    typeToURI={"article":"http://purl.org/ontology/bibo/Article","book":"http://purl.org/ontology/bibo/Book"}
    bibmap={}
    for entry in entries:
        bibmap[str(entry["ID"])[0:str(entry["ID"]).rfind("_")]]=ns+"bib_"+str(entry["ID"])
        triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <"+str(typeToURI[entry["ENTRYTYPE"]])+"> .\n")
        triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(entry["title"])+"\"@en .\n")
        triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://purl.org/dc/elements/1.1/title> \""+str(entry["title"])+"\"@en .\n")
        if "and" in entry["author"]:
            for author in entry["author"].split("and"):
                if "," in author:
                    authoruri=str(author).replace(","," ")
                    authoruri=authoruri.replace(" ","_")
                    authoruri=authoruri.replace("__","_")
                    authoruri=authoruri.strip()
                    triples.add("<"+ns+"author_"+str(authoruri)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .\n")
                    triples.add("<"+ns+"author_"+str(authoruri)+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(author)+"\"@en .\n")
                    triples.add("<"+ns+"author_"+str(authoruri)+"> <http://xmlns.com/foaf/0.1/family_Name> \""+str(author)[0:str(author).rfind(',')]+"\"@en .\n")
                    triples.add("<"+ns+"author_"+str(authoruri)+"> <http://xmlns.com/foaf/0.1/firstName> \""+str(author)[str(author).rfind(',')+1:].strip()+"\"@en .\n")
                    triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://purl.org/dc/elements/1.1/creator> <"+ns+"author_"+str(authoruri)+"> .\n")
        else:
            authoruri=str(entry["author"]).replace(","," ")
            authoruri=authoruri.replace(" ","_")
            authoruri=authoruri.replace("__","_")
            authoruri=authoruri.strip()
            triples.add("<"+ns+"author_"+str(authoruri)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .\n")
            triples.add("<"+ns+"author_"+str(authoruri)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#label> \""+str(entry["author"])+"\"@en .\n")
            triples.add("<"+ns+"author_"+str(authoruri)+"> <http://xmlns.com/foaf/0.1/family_Name> \""+str(entry["author"])[0:str(entry["author"]).rfind(',')]+"\"@en .\n")
            triples.add("<"+ns+"author_"+str(authoruri)+"> <http://xmlns.com/foaf/0.1/firstName> \""+str(entry["author"])[str(entry["author"]).rfind(',')+1:].strip()+"\"@en .\n")
            triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://purl.org/dc/elements/1.1/creator> <"+ns+"author_"+str(authoruri)+"> .\n")
        triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://purl.org/dc/elements/1.1/created> \""+str(entry["year"])+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        if "doi" in entry:
            triples.add("<"+ns+"bib_"+str(entry["ID"])+"> <http://purl.org/ontology/bibo/doi> \""+str(entry["doi"])+"\"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n")
    return {"triples":triples,"bibmap":bibmap}


with open('source/spp.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
print(bib_database.entries)

ns="http://data.archaeology.link/data/spphaefen/"
nsont="http://www.spp-haefen.de/ont#"
triples=set()
bibres=bibtexToRDF(triples,bib_database.entries,ns,nsont)
triples=bibres["triples"]
bibmap=bibres["bibmap"]
triples.add("<http://www.opengis.net/ont/geosparql#Feature> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#Geometry> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#hasGeometry> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#asWKT> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#DatatypeProperty> .\n")
triples.add("<http://www.opengis.net/ont/sf#Point> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Geometry> .\n")
triples.add("<"+str(nsont)+"Harbour> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Feature> .\n")
triples.add("<http://www.wikidata.org/prop/direct/P206> <http://www.w3.org/2000/01/rdf-schema#label> \"located in or next to body of water\"@en .\n")
triples.add("<http://www.wikidata.org/prop/direct/P17> <http://www.w3.org/2000/01/rdf-schema#label> \"country\"@en .\n")
with open('source/HarbourDataRepository_001_Kroeger_2018.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        cururi=ns+row["ID_place"]
        #print(cururi)
        triples.add("<"+str(cururi)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <"+str(nsont)+"Harbour> .\n")
        triples.add("<"+str(cururi)+"> <http://www.opengis.net/ont/geosparql#hasGeometry> <"+str(cururi)+"_geom> .\n")
        if row["Author"] in authormap:
            triples.add("<"+str(cururi)+"> <http://purl.org/dc/elements/1.1/creator> <"+str(authormap[row["Author"]])+"> .\n")
            triples.add("<"+str(authormap[row["Author"]])+"><http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Author"])+"\"@en  .\n")
        else:
            triples.add("<"+str(cururi)+"> <http://purl.org/dc/elements/1.1/creator> \""+str(row["Author"])+"\" .\n")
        triples.add("<"+str(cururi)+"> <http://purl.org/dc/elements/1.1/created> \""+str(row["Year"]).replace("\"","'")+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        triples.add("<"+str(cururi)+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Name_mod"]).replace("\"","'")+"\"@en .\n")
        if row["Hydro_name_mod"] in bodyofwater:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P206> <"+bodyofwater[str(row["Hydro_name_mod"])]+"> .\n <"+bodyofwater[str(row["Hydro_name_mod"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Hydro_name_mod"])+"\"@en .\n")
        else:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P206> \""+str(row["Hydro_name_mod"]).replace("\"","'")+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
            if str(row["Hydro_name_mod"])!="Unknown":
                print(str(row["Hydro_name_mod"]))
        triples.add("<"+str(cururi)+"> <"+str(nsont)+"locationSecure> \""+str(row["Locat_secure"]).replace("\"","'")+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if row["Project"] in projectmap:
           triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> <"+projectmap[str(row["Project"])]+"> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/cerif/frapo/Project> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Project"])+"\"@en .\n")
        else:
           triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> \""+str(row["Project"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if row["Country"] in countries:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P17> <"+countries[str(row["Country"])]+"> .\n <"+countries[str(row["Country"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Country"])+"\"@en .\n")
        else:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P17> \""+str(row["Country"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if "Date_min" in row and row["Date_min"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_min> \""+str(row["Date_min"])+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        if "Date_max" in row and row["Date_max"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_max> \""+str(row["Date_max"])+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        if "Place_technique" in row and row["Place_technique"].strip()!="":
            if row["Place_technique"] in place_technique:
                triples.add("<"+str(cururi)+"> <"+str(nsont)+"place_technique> <"+str(place_technique[row["Place_technique"]])+"> .\n")
                triples.add("<"+str(place_technique[row["Place_technique"]])+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Place_technique"])+"\"@en .\n")
            else:
                triples.add("<"+str(cururi)+"> <"+str(nsont)+"place_technique> \""+str(row["Place_technique"])+"\" .\n")
        if "Locat_precision" in row and row["Locat_precision"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"precision> <"+str(nsont)+str(row["Locat_precision"])+"> .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.opengis.net/ont/geosparql#asWKT> \"POINT("+row["Longitude"]+" "+row["Latitude"]+")\"^^<http://www.opengis.net/ont/geosparql#wktLiteral> .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.w3.org/2000/01/rdf-schema#label> \"\"\""+str(row["Name_mod"]).replace("\"","'")+" Geometry\"\"\"@en .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/ont/sf#Point> .\n")
        if "Comments" in row and row["Comments"]!="":
            triples.add("<"+str(cururi)+"> <http://www.w3.org/2000/01/rdf-schema#comment> \"\"\""+row["Comments"].replace("\"","'")+"\"\"\"@en .\n")
        if "Ref_mod" in row and row["Ref_mod"]!="":
            refs= row["Ref_mod"].split(";")
            for ref in refs:
                if ref in bibmap:
                    triples.add("<"+str(cururi)+"> <http://purl.org/dc/terms/isReferencedBy> "+str(bibmap[ref])+" . \n")
            triples.add("<"+str(cururi)+"> <http://www.w3.org/2004/02/skos/core#note> \"\"\""+row["Ref_mod"]+"\"\"\" .\n")

with open("spp_result.ttl","w",encoding="utf-8") as resfile:
    resfile.write("".join(triples))
    resfile.close()

#g=Graph()
#g.parse("spp_result.ttl")
#g.serialize("spp_result.ttl")
