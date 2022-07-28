package softex;
import java.io.Serializable;

public class Aluno implements Serializable{
	private String nome;
	private int idade;
	
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