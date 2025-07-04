public class SingleTon {
    // Die Instanz - zunachst noch nicht vorhanden
    private static SingleTon singleton;

    // der private Konstruktor
    private SingleTon() {}

    // die Clientmethode instance()
    public static synchronized SingleTon instance() {
        // Instanz erzeugen, falls noch keine existiert
        if (singleton == null) {
            singleton = new SingleTon();
        }
        // Instanz auf jeden Fall zuruckgeben
        return singleton;
    }
}


