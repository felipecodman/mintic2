package Ciclo2.Retos;

import java.util.Arrays;

public class array2 {

  public static void main(String[] args){

  int arr[] = new int[]{1, 2, 1, 3, 3, 1, 2, 1, 5, 1};

    //1: Ordenamos el array
    Arrays.sort(arr);
    //2: Obtenemos el ultimo item del array que seria el valor maximo.
    int max = arr[arr.length - 1];

    //3: recorremos todos los numeros entre 1 y el valox maximo, para imprimirlos.
    for(int i = 1; i <= max; i++){
        // 4: imprimimos el numero a contar
        System.out.print(i + ": ");
        //5: recorremos el array para imprimir * por cada vez que encontremos el numero actual i
        for (int x = 0; x < arr.length; x++){
            // 6: si el numero actual i es igual al numero en la pocision x del array imprime *
            if (i == arr[x]){
                System.out.print("*");
            }
        }
        //7: salto de linea al final de imprimir los * o vacio en caso de no encontrar el número
        System.out.println();
    }
  }
}