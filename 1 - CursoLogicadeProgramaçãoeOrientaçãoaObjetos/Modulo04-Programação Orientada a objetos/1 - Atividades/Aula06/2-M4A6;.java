package GetAndSet;

public class Pessoa {
	private String nome;
	private int idade;
	
	public Pessoa() {
		System.out.println("Pessoa citada, permanecer de pé");
	}
	
	public String getNome() {
		return this.nome;
	}
	public void setNome (String n) {
		this.nome = n;
	}
	
	public int getIdade() {
		return this.idade;	
	}
	public void setIdade(int i) {
		this.idade = i;
	}
		
}