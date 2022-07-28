package softex;

import java.io.ObjectOutputStream;

public class Main {

	public static void main(String[] args) {
		Aluno a1 = new Aluno();
		
		ObjectOutputStream objectOuput = new ObjectOutputStream(new FileOutputStream(nome:"product.bytej"));
		objectOuput.writeObject(a1);
		objectOuput.close();
	
	}

}