test_items = [
    #NOTE all test items taken from https://www.einbuergerungstest-online.de/einbuergerungstest test for Berlin. (may be item number discrepancies between this and other sources)
    #NOTE 321-330 are for Berlin only.
    #NOTE this is a 0.1 master list, to be converted into a library as per lib_data_entry.py
    #NOTE: code at bottom used to convert list to dictionary (items_lib.json) on 19.06.2023

    (179, "Was gab es während der Zeit des Nationalsozialismus in Deutschland?", ["das Verbot von Parteien ", "das Recht zur freien Entfaltung der Persönlichkeit ", "Pressefreiheit ", "den Schutz der Menschenwürde "], 0),
    (90, "Die deutschen Bundesländer wirken an der Gesetzgebung des Bundes mit durch …", ["den Bundestag. ", "den Bundesrat. ", "die Bundesregierung.", "die Bundesversammlung. "], 1),
    (126, "Was bekommen wahlberechtigte Bürger und Bürgerinnen in Deutschland vor einer Wahl?", ["eine Wahlerlaubnis vom Bundespräsidenten / von der Bundespräsidentin", "eine Benachrichtigung vom Pfarramt", "eine Benachrichtigung von der Bundesversammlung ", "eine Wahlbenachrichtigung von der Gemeinde"], 3),
    (37, "Wie werden die Regierungschefs / Regierungschefinnen der meisten Bundesländer in Deutschland genannt?", ["Ministerpräsident / Ministerpräsidentin", "Senator / Senatorin ", "Erster Minister / Erste Ministerin", "Premierminister / Premierministerin"], 0),
    (60, "In Deutschland gehören der Bundestag und der Bundesrat zur …", ["Judikative.", "Exekutive. ", "Legislative.", "Direktive."], 2),
    (119, "Wahlen in Deutschland sind frei. Was bedeutet das?", ["Jede Person kann ohne Zwang entscheiden, ob sie wählen möchte und wen sie wählen möchte.", "Alle verurteilten Straftäter / Straftäterinnen dürfen nicht wählen.", "Wenn ich wählen gehen möchte, muss mein Arbeitgeber / meine Arbeitgeberin mir frei geben.", "Ich kann frei entscheiden, wo ich wählen gehen möchte. "], 0),
    (183, "Wann war in der Bundesrepublik Deutschland das „Wirtschaftswunder“?", ["40er Jahre ", "50er Jahre", "70er Jahre", "80er Jahre"], 1),
    (142, "Was ist die Hauptaufgabe eines Richters / einer Richterin in Deutschland? Ein Richter / eine Richterin …", ["arbeitet an einem Gericht und spricht Urteile.", "vertritt Bürger und Bürgerinnen vor einem Gericht.", "betreut Jugendliche vor Gericht.", "ändert Gesetze."], 0),
    (148, "Was ist eine Aufgabe der Polizei in Deutschland?", ["die Einhaltung von Gesetzen zu überwachen", "die Bürgerinnen und Bürger abzuhören", "die Gesetze zu beschließen", "das Land zu verteidigen"], 0),
    (298, "In der DDR lebten vor allem Migranten aus …", ["Frankreich, Rumänien, Somalia.", "Nordkorea, Mexiko, Ägypten.", "Chile, Ungarn, Simbabwe.", "Vietnam, Polen, Mosambik."], 3),
    (79, "Was bedeutet die Abkürzung FDP in Deutschland?", ["Führende Demokratische Partei", "Freie Demokratische Partei", "Freie Deutschland Partei", "Friedliche Demonstrative Partei"], 1),
    (249, "Wer ist in Deutschland hauptsächlich verantwortlich für die Kindererziehung?", ["der Staat", "die Schulen", "die Eltern", "die Verwandten"], 2),
    (101, "Gewerkschaften sind Interessenverbände der …", ["Rentner und Rentnerinnen.", "Arbeitgeber und Arbeitgeberinnen.", "Arbeitnehmer und Arbeitnehmerinnen.", "Jugendlichen."], 2),
    (258, "Was darf das Jugendamt in Deutschland?", ["Es kontrolliert, ob das Kind einen Kindergarten besucht.", "Es bezahlt das Kindergeld an die Eltern.", "Es entscheidet, welche Schule das Kind besucht", "Es kann ein Kind, das geschlagen wird oder hungern muss, aus der Familie nehmen."], 3),  
    (140, "Was macht ein Schöffe / eine Schöffin in Deutschland? Er / Sie …", ["stellt Urkunden aus.", "gibt Bürgern / Bürgerinnen rechtlichen Rat.", "entscheidet mit Richtern / Richterinnen über Schuld und Strafe.", "verteidigt den Angeklagten / die Angeklagte."], 2),
    (282, "Welches Ehrenamt müssen deutsche Staatsbürger / Staatsbürgerinnen übernehmen, wenn sie dazu aufgefordert werden?", ["Wahlhelfer / Wahlhelferin", "Bibliotheksaufsicht", "Vereinstrainer / Vereinstrainerin", "Lehrer / Lehrerin"], 0),
    (72, "Wie heißt der jetzige Bundeskanzler / die jetzige Bundeskanzlerin von Deutschland?", ["Gerhard Schröder", "Franziska Giffey", "Angela Merkel", "Olaf Scholz"], 3),
    (203, "Wie hieß das Wirtschaftssystem der DDR?", ["Angebot und Nachfrage", "Marktwirtschaft", "Kapitalismus", "Planwirtschaft"], 3), 
    (10, "Was ist mit dem deutschen Grundgesetz vereinbar?", ["die Todesstrafe", "die Prügelstrafe", "die Folter", "die Geldstrafe"], 3),
    (71, "Wo hält sich der deutsche Bundeskanzler / die deutsche Bundeskanzlerin am häufigsten auf? Am häufigsten ist er / sie …", ["in Bonn, weil sich dort das Bundeskanzleramt und der Bundestag befinden.", "auf Schloss Bellevue, dem Amtssitz des Bundespräsidenten / der Bundespräsidentin, um Staatsgäste zu empfangen.", "in Berlin, weil sich dort das Bundeskanzleramt und der Bundestag befinden", "auf Schloss Meseberg, dem Gästehaus der Bundesregierung, um Staatsgäste zu empfangen."], 2),
    (52, "Was bedeutet „Volkssouveränität“? Alle Staatsgewalt geht vom …", ["Volke aus.", "Bundestag aus.", "Bundesverfassungsgericht aus.", "preußischen König aus."], 0),
    (195, "Welches heutige deutsche Bundesland gehörte früher zum Gebiet der DDR?", ["Hessen", "Sachsen-Anhalt", "Nordrhein-Westfalen", "Saarland"], 1),
    (206, "Was bedeutete im Jahr 1989 in Deutschland das Wort „Montagsdemonstration“?", ["Montags waren Demonstrationen gegen das DDR-Regime.", "Montags demonstrierte man in der DDR gegen den Westen.", "In der Bundesrepublik waren Demonstrationen nur am Montag erlaubt.", "Am ersten Montag im Monat trafen sich in der Bundesrepublik Deutschland Demonstranten."], 0),
    (276, "Was sollten Sie tun, wenn Sie von Ihrem Ansprechpartner / Ihrer Ansprechpartnerin in einer deutschen Behörde schlecht behandelt werden?", ["Ich drohe der Person", "Ich kann nichts tun.", "Ich kann mich beim Behördenleiter / bei der Behördenleiterin beschweren. ", "Ich muss mir diese Behandlung gefallen lassen."], 2),
    (295, "Welche Religion hat die europäische und deutsche Kultur geprägt?", ["der Islam ", "der Hinduismus", "das Christentum", "der Buddhismus"], 2), 
    (243, "Maik und Sybille wollen mit Freunden an ihrem deutschen Wohnort eine Demonstration auf der Straße abhalten. Was müssen sie vorher tun?", ["Sie müssen die Demonstration anmelden.", "Sie müssen nichts tun. Man darf in Deutschland jederzeit überall demonstrieren.", "Sie können gar nichts tun, denn Demonstrationen sind in Deutschland grundsätzlich verboten.", "Maik und Sybille müssen einen neuen Verein gründen, weil nur Vereine demonstrieren dürfen."], 0),    
    (223, "Welches Land ist ein Nachbarland von Deutschland?", ["Polen ", "Rumänien", "Bulgarien", "Griechenland"], 0),
    (159, "Was gab es in Deutschland nicht während der Zeit des Nationalsozialismus?", ["Pressezensur", "Verfolgung der Juden", "freie Wahlen", "willkürliche Verhaftungen"], 2), 
    (158, "Das „Dritte Reich“ war eine …", ["Demokratie.", "Räterepublik", "Monarchie.", "Diktatur."], 3),
    (239, "Durch welche Verträge schloss sich die Bundesrepublik Deutschland mit anderen Staaten zur Europäischen Wirtschaftsgemeinschaft zusammen?", ["durch die „Londoner Verträge“", "durch die „Pariser Verträge“", "durch die „Hamburger Verträge“", "durch die „Römischen Verträge“"], 3),    
    (323, "Für wie viele Jahre wird das Landesparlament in Berlin gewählt?", ["3", "4", "5", "6"], 2),
    (329, "Wie nennt man den Regierungschef / die Regierungschefin des Stadtstaates Berlin?", ["Oberbürgermeister / Oberbürgermeisterin", "Regierender Bürgermeister / Regierende Bürgermeisterin", "Ministerpräsident / Ministerpräsidentin", "Präsident / Präsidentin des Senats"], 1),
    (330, "Welchen Senator / welche Senatorin hat Berlin nicht?", ["Finanzsenator / Finanzsenatorin", "Senator / Senatorin für Außenbeziehungen", "Justizsenator / Justizsenatorin", "Innensenator / Innensenatorin"], 1),
    
    (35, "Womit finanziert der deutsche Staat die Sozialversicherung?", ["Sozialabgaben", "Kirchensteuern ", "Vereinsbeiträgen ", "Spendengeldern "], 0),    
    (63, "Was gehört in Deutschland nicht zur Exekutive?", ["die Ministerien ", "das Finanzamt ", "die Polizei ", "die Gerichte"], 3),
    (227, "Welches Land ist ein Nachbarland von Deutschland?", ["Finnland ", "Schweden ", "Dänemark", "Norwegen "], 2),
    (68, "Warum kontrolliert der Staat in Deutschland das Schulwesen?", ["weil es nach dem Grundgesetz seine Aufgabe ist ", "weil es in Deutschland nur staatliche Schulen gibt", "weil es in den Bundesländern verschiedene Schulen gibt ", "weil alle Schüler und Schülerinnen einen Schulabschluss haben müssen"], 0),
    (41, "Warum gibt es in einer Demokratie mehr als eine Partei?", ["weil dadurch die unterschiedlichen Meinungen der Bürger und Bürgerinnen vertreten werden", "um wirtschaftlichen Wettbewerb anzuregen ", "um politische Demonstrationen zu verhindern ", "damit Bestechung in der Politik begrenzt wird "], 0),
    (106, "In Deutschland helfen ehrenamtliche Wahlhelfer und Wahlhelferinnen bei den Wahlen. Was ist eine Aufgabe von Wahlhelfern / Wahlhelferinnen?", ["Sie helfen Kindern und alten Menschen beim Wählen. ", "Sie zählen die Stimmen nach dem Ende der Wahl. ", "Sie geben Zwischenergebnisse an Journalisten weiter. ", "Sie schreiben Karten und Briefe mit der Angabe des Wahllokals. "], 1),
    (213, "Wie viele Einwohner hat Deutschland?", ["70 Millionen ", "78 Millionen", "83 Millionen", "90 Millionen "], 1),
    (240, "Seit wann bezahlt man in Deutschland mit dem Euro in bar?", ["1995 ", "1998", "2005 ", "2002"], 3),    
    (110, "Für wie viele Jahre wird der Bundestag in Deutschland gewählt?", ["4 Jahre ", "5 Jahre", "2 Jahre ", "3 Jahre "], 0),
    (114,  "An demokratischen Wahlen in Deutschland teilzunehmen ist …", ["eine Last. ", "ein Zwang. ", "ein Recht. ", "eine Pflicht. "], 2),
    (151, "Wer baute die Mauer in Berlin?", ["Großbritannien ", "die DDR ", "die Bundesrepublik Deutschland ", "die USA"], 1),
    (279, "In den meisten Mietshäusern in Deutschland gibt es eine „Hausordnung“. Was steht in einer solchen „Hausordnung“? Sie nennt …", ["alle Mieter und Mieterinnen im Haus. ", "die Adresse des nächsten Ordnungsamtes.", "Regeln, an die sich alle Bewohner und Bewohnerinnen halten müssen.", "Regeln für die Benutzung öffentlicher Verkehrsmittel. "], 2),    
    (8, "Was steht nicht im Grundgesetz von Deutschland?", ["Die Würde des Menschen ist unantastbar. ", "Jeder Mensch darf seine Meinung sagen. ", "Alle sollen gleich viel Geld haben. ", "Alle sind vor dem Gesetz gleich. "], 2),
    (149, "Wer kann Gerichtsschöffe / Gerichtsschöffin in Deutschland werden?", ["nur Personen mit einem abgeschlossenen Jurastudium ", "alle Personen, die seit mindestens 5 Jahren in Deutschland leben ", "alle deutschen Staatsangehörigen älter als 24 und jünger als 70 Jahre ", "alle in Deutschland geborenen Einwohner / Einwohnerinnen über 18 Jahre "], 2),
    (132, "Viele Menschen in Deutschland arbeiten in ihrer Freizeit ehrenamtlich. Was bedeutet das?", ["Sie arbeiten als Soldaten / Soldatinnen.", "Sie arbeiten in der Bundesregierung.", "Sie arbeiten freiwillig und unbezahlt in Vereinen und Verbänden.", "Sie arbeiten in einem Krankenhaus und verdienen dabei Geld. "], 2),
    (234, "Wo ist der Sitz des Europäischen Parlaments?", ["Straßburg ", "London ", "Paris", "Berlin "], 0),    
    (23, "In Deutschland sind die meisten Erwerbstätigen …", ["in kleinen Familienunternehmen beschäftigt. ", "ehrenamtlich für ein Bundesland tätig. ", "bei einer Firma oder Behörde beschäftigt. ", "selbständig mit einer eigenen Firma tätig."], 2),
    (137,  "Welches Gericht ist in Deutschland bei Konflikten in der Arbeitswelt zuständig?", ["das Amtsgericht ", "das Familiengericht", "das Strafgericht ", "das Arbeitsgericht "], 3),
    (266, "Wann beginnt die gesetzliche Nachtruhe in Deutschland?", ["wenn die Sonne untergeht ", "wenn die Nachbarn schlafen gehen", "um 0 Uhr, Mitternacht ", "um 22 Uhr "], 3),
    (169, "Wann wurde die Bundesrepublik Deutschland gegründet?", ["1939 ", "1945 ", "1949 ", "1951 "], 2),    
    (163, "In welchem Jahr zerstörten die Nationalsozialisten Synagogen und jüdische Geschäfte in Deutschland?", ["1945 ", "1925 ", "1930 ", "1938"], 3),
    (86, "Wer wählt in Deutschland den Bundespräsidenten / die Bundespräsidentin?", ["der Bundesrat ", "das Bundesverfassungsgericht ", "die Bundesversammlung", "das Bundesparlament "], 2),
    (219, "Die Bundesrepublik Deutschland hat die Grenzen von heute seit …", ["1990. ", "1933. ", "1971. ", "1949. "], 0),
    (51, "Zu einem demokratischen Rechtsstaat gehört es nicht, dass …", ["Menschen sich kritisch über die Regierung äußern können. ", "Menschen von einer Privatpolizei ohne Grund verhaftet werden.", "jemand ein Verbrechen begeht und deshalb verhaftet wird.", "Bürger friedlich demonstrieren gehen dürfen. "], 1),    
    (283, "Was tun Sie, wenn Sie eine falsche Rechnung von einer deutschen Behörde bekommen?", ["Ich gehe mit der Rechnung zum Finanzamt. ", "Ich schicke die Rechnung an die Behörde zurück. ", "Ich lasse die Rechnung liegen. ", "Ich lege Widerspruch bei der Behörde ein. "], 3),
    (278, "Ein Mann im Rollstuhl hat sich auf eine Stelle als Buchhalter beworben. Was ist ein Beispiel für Diskriminierung? Er bekommt die Stelle nur deshalb nicht, weil er …", ["im Rollstuhl sitzt. ", "keine Erfahrung hat. ", "kein Englisch spricht. ", "zu hohe Gehaltsvorstellungen hat. "], 0),
    (221, "Deutschland ist Mitglied des Schengener Abkommens. Was bedeutet das?", ["Deutsche können ohne Passkontrolle in jedes Land reisen. ", "Deutsche können in viele Länder Europas ohne Passkontrolle reisen.", "Alle Menschen können ohne Personenkontrolle in Deutschland einreisen. ", "Deutsche können in jedem Land mit dem Euro bezahlen. "], 1),
    (325, "Welche Farben hat die Landesflagge von Berlin?", ["schwarz-gold", "blau-weiß-rot", "grün-weiß-rot ", "weiß-rot "], 3),    
    (327, "Welches Bundesland ist ein Stadtstaat?", ["Hessen ", "Brandenburg ", "Saarland ", "Berlin"], 1),
    (27, "Deutschland ist …", ["ein sozialistischer Staat.", "eine Diktatur. ", "ein Bundesstaat. ", "eine Monarchie. "], 2),
    (129, "Vom Volk gewählt wird in Deutschland …", ["der Ministerpräsident / die Ministerpräsidentin eines Bundeslandes. ", "der Bundestag. ", "der Bundespräsident / die Bundespräsidentin. ", "der Bundeskanzler / die Bundeskanzlerin. "], 1),
    (84, "Welche Hauptaufgabe hat der deutsche Bundespräsident / die deutsche Bundespräsidentin? Er / Sie …", ["repräsentiert das Land. ", "überwacht die Einhaltung der Gesetze. ", "entwirft die Gesetze. ", "regiert das Land. "], 0),    
    (120, "Das Wahlsystem in Deutschland ist ein …", ["allgemeines Männerwahlrecht. ", "Mehrheits- und Verhältniswahlrecht. ", "Dreiklassenwahlrecht. ", "Zensuswahlrecht. "], 1),
]

items = {}
for item in test_items:
    number = int(item[0])
    question = item[1]
    options = item[2]
    correct_response = item[3]

    new_entry = {
        'question': question,
        'options': options, 
        'correct_response': correct_response
    }

    items[number] = new_entry

import json
def save_library(items, items_lib):
    with open(items_lib, 'w') as file:
        json.dump(items, file)

save_library(items, 'items_lib.json')

print(items)