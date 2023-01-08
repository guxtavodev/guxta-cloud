using System;

class MeuPrograma {
	static void Main(){
		Console.WriteLine("Rodando C# No Sublime hehe");
		int num1;
		int num2;
		int soma;

		Console.WriteLine("Digite o primeiro número!");
		num1 = int.Parse(Console.ReadLine());
		Console.WriteLine("Digite o segundo numero!");
		num2 = int.Parse(Console.ReadLine());
		soma=num1+num2;

		Console.WriteLine("A Soma dos 2 números é: {0}", soma);
	}
}