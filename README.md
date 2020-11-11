Begleiten Sie Alman Achim auf seiner Reise durch ein furchterregendes extraterrestrisches Kartoffelfeld im Erstlingswerk des Entwicklerstudios Team_All-Mann!
Wenn Sie das Spiel spielen wollen, so müssen Sie zunächst ein, zwei Vorbereitungen treffen. Dieser Text fungiert als eine Art Tutorial, das Ihnen dabei unter
die Arme greifen soll. Schritt für Schritt wird Ihnen im Folgenden erklärt, was Sie tun müssen.


1. Um das Spiel starten zu können, müssen Sie zunächst sicherstellen, dass Sie die aktuelle Version von Python (3.9 Stand Nov_2020) installiert haben: https://www.python.org/downloads/

2. Ist das erledigt, müssen Sie das Spiel aus unserem GIT Repository auf Ihrem PC speichern. Befinden Sie sich in der Übersicht des Reiters "<>Code", 
in der Sie die Einträge LICENCE, README.md & Asteroids.py sehen, müssten Sie rechts über der Liste einen grünen Button sehen, der mit Code betitelt ist.
Klicken Sie auf den Button und kopieren Sie den Link, der in dem gerade erschienenen Fenster angezeigt wird.

3. Nun zeigen wir Ihnen, wie Sie die Kommandozeile ihres Computers öffnen. Besitzen Sie einen Mac, dann öffnen Sie das Terminal indem Sie cmd + Leertaste
drücken und nach "Terminal" suchen. Starten Sie das Terminal mit einem Doppelklick. Besitzen Sie einen Windows PC, dann öffnen Sie die 
Kommandozeile, indem Sie die Windows-Taste drücken, anschließend cmd eintippen und Enter drücken. Keine Ahnung, wie das bei Linux ist lol,
wenn Sie Linux haben, wünsche ich Ihnen alles gute.

4. Haben Sie die die Kommandozeile vor sich? Großartig! Sie haben es fast geschafft! Bevor wir weitermachen, gedenken wir jedoch kurz jenen, die es nicht
bis zu diesem Schritt der Anleitung geschafft haben

...

In Ordnung machen wir weiter!

5. Im Folgenden werden Sie einige Befehle benötigen, die am Ende der Readme Datei noch einmal konzentriert aufgelistet werden. Denken Sie daran jeden Befehl
mit der Entertaste zu bestätigen. Zunächst müssen Sie sich darüber Gedanken machen, in welchem Ordner Sie das Spiel speichern wollen. Indem Sie den Befehl 
pwd eingeben und Enter drücken, können Sie sehen, in welchem Order Sie sich gerade befinden. Es bietet sich an, dass Sie für das Spiel einen neuen Ordner anlegen. 
Um einen neuen Ordner zu erstellen, tippen Sie den Befehl Mkdir ein, gefolgt von einem Leerzeichen und dem Namen den Sie dem Ordner geben wollen.
Wenn Sie den Ordner erstellt haben, können Sie erneut Mkdir eingeben, um zu überprüfen, ob Ihr Ordner zu sehen ist.

6. Nun gehen Sie in den Ordner, indem Sie Ls [Ihr Ordnername] eingeben.

7. Wir hoffen, dass Sie immer noch den Link in Ihrer Zwischenablage kopiert haben, denn nun ist es so weit, dass Sie das Repository klonen. Geben Sie "Git Clone [Link]" ein
und fügen Sie anstatt [Link] ihren Github Link ein.

8. Das Spiel nutzt ein System namens Arcade, dass Sie ebenfalls auf ihrem Computer installieren müssen, indem Sie Pip3 install arcade im Terminal eingeben.

9. Zuletzt müssen Sie noch Python starten, indem Sie einfach Python eingeben und Enter drücken.

10. Haben Sie diese Schritte richtig befolgt, sollte alles bereit zum Spielen sein. Geben Sie python asteroids.py ein und drücken Sie enter. Das Spiel sollte nun starten.
Wir wünschen Ihnen viel Spaß mit Almann Achims Abenteuer im Weltall!



Hier noch einmal die wichtigsten Befehle für die Kommandozeile:

1. Python    - Python starten
2. Strg-d    - Python beenden
3. Git clone - Git einfügen
4. Mkdir     - Neuen Ordner erstellen
5. Ls        - Ordnerinhalt listen
6. Pwd       - Zeigt an, in welchem Ordner Sie sich befinden
7. Cd ..     - Eine Ebene höher springen
8. Clone     - Zum ersten Mal runterladen
9. Pip3      - Arcade installieren
10. Push      - Hochladen
11. Fetch     - Runterladen aber noch nicht anwenden
12. Pull      - Herunterladen und anwenden
13. python asteroids.py - Spiel starten



Steuerung des Spiels:

1. Weichen Sie den Kartoffeln aus, indem Sie die Pfeiltasten benutzen.
2. Sie haben drei Leben. Kollidieren Sie mit einer Kartoffel, verlieren Sie ein Leben.
3. Sind Ihre Leben aufgebraucht, endet das Spiel.
4. Schießen Sie auf Kartoffeln, indem Sie die Leertaste drücken.
5. Für jede frittierte Kartoffel erhalten Sie X Punkte.
6. Ziel ist es einen möglichst hohen Score zu erreichen, bevor das Spiel endet.



Wir hoffen, dass diese Readme File all Ihre Fragen beantworten konnte und dass Ihnen das Spiel gefällt :)
