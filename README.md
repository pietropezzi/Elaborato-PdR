# Elaborato Programmazione di Reti
Questo repository contiene la mia soluzione alla **Traccia 1** dell'Elaborato di Programmazione di Reti.
Per una breve guida su come eseguire il codice, leggere il punto **2.Istruzioni esecuzione** della
[Relazione](https://github.com/pietropezzi/Elaborato-PdR/blob/main/Relazione.pdf).

# Traccia
Si immagini di avere uno scenario di Smart Meter IoT che rilevando la temperatura e umidità del
terreno in cui sono posizionati.
Questi dispositivi si collegano 1 volta al giorno con una connessione UDP verso il Gateway.
Tramite questa connessione i dispositivi inviano le misure che hanno raccolto durante le 24 ore
precendenti. Le misure consistono di un file che contiene l'ora della misura e il dato di
temperatura e umidità.

Una volta che i pacchetti di tutti i dispositivi sono arrivati al Gateway, il gateway instaura una 
connessione TCP verso un server centrale dove i valori vengono visualizzati sulla console del
server nel seguente modo

**Ip_address_device_1 - ora_misura - valore_temperatura - valore_umidità**

*I 4 Dispositivi IoT hanno un indirizzamento appartenente ad una rete di Classe C del tipo
192.168.1.0/24, Il Gateway ha due interfacce di rete: quella verso i dispositivi il cui IP address
appartiene alla stessa network dei dispositivi mentre l'interfaccia che parla con il server ha indirizzo ip
appartenente alla classe 10.10.10.10.0/24, classe a cui appartiene anche l'IP address del server
centrale.*

*Si realizzi un emulatore Python che sfruttando il concetto di socket visti in laboratorio consenta
di simulare, utilizzando l'interfaccia di loopback del propio PC, il comportamento di questo sistema.
Si devono simulare le connessioni UDP dei device verso il Gateway e la connessione TCP del
Gateway verso il Server mostrando sulla Console del server la lista dei messaggi ricevuti nel
formato indicato sopra. Inoltre indicare la dimensione dei buffer utilizzati su ciascun canale 
trasmissivo, il tempo impiegato per trasmettere il pacchetto UDP ed il tempo impiegato per
trasmettere il pacchetto TCP.*
