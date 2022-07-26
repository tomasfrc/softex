package GetAndSet;

public class Main {

	public static void main(String[] args) {
		Pessoa p1 = new Pessoa();
		p1.setNome("Alysson Campelo");
		p1.setIdade(25);
		
		System.out.println("Sobre a pessoa: ");
		System.out.println("Nome: " + p1.getNome());
		System.out.println("Idade: " + p1.getIdade());

	}

}