package tratamento;

public class Execao {

	public static void main(String[] args) {
		
	try {
		int[] vetor = new int[4];	
		vetor[4] = 1;
		
		
	} catch(ArrayIndexOutOfBoundsException exception) {
		System.out.println("O indice indicato não existe");
		
	}
		
	}

}