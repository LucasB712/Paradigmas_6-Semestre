class Hora extends Thread{
  
  private int tempoEspera;
  public Hora(String name, int tempoespera) {
    super(name);
    this.tempoEspera = tempoEspera;
    
    System.out.println("Nome da thread: " + getName() + " Dorme por " + tempoEspera + "ms");
  
  }
  
  @Override
  public void run() {
    try {
      
      System.out.println(getName() + " indo dormir");
      Thread.sleep(tempoEspera);
    } catch ( Exception exception) {
      System.out.println("Thread interrompida: " + exception.toString());

    }
    
    System.out.println(getName() + " ja dormiu e terminou execucao");
  }
}
