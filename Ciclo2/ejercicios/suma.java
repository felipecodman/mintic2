package Ciclo2.ejercicios;

public class suma {

    static int[]array = {1,3,4,2,7,0};
  
    public static void main(String[] args) {        
    
      for(int i=0; i<array.length; i++){
        for(int j=1;j<array.length; j++){
          if(array[i]+array[j]==10){
            
            System.out.println(array[i]+" "+array[j]);
            
            }
          }
        }     
      }
  }