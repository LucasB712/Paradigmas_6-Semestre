import java.util.*;

public class Main {
  public static void main(String[] args) {
    
    ImprimirThread thread1;
    Hora thread2;
    thread1 = new ImprimirThread("Noticias", 500);
    thread2 = new Hora("Hora", 1000);
    
    System.out.println("Iniciando threads ...");
    
    thread1.start();
    thread2.start();
    
    
  }
}
