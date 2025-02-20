frequencias = [
    "Unica",
    "Aniversario",
    "Vencimento",
    "Diario",
    "Semanal",
    "Quinzanal",
    "Mensal",
    "Anual"]

semanas = [
    "Segunda",
    "Terca",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sabado",
    "Domingo"]    
meses = [
    "Janeiro", 
    "Fevereiro",
    "Marco",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"]   

opcoes_frequencia = [f"{frequencia}" for frequencia in frequencias]
opcoes_meses = [f"{frequencia}" for frequencia in meses]
opcoes_semanas = [f"{frequencia}" for frequencia in semanas]
opcoes_31_dias = [f"{dia:02}" for dia in range(1, 32)]
opcoes_30_dias = [f"{dia:02}" for dia in range(1, 31)]
opcoes_29_dias = [f"{dia:02}" for dia in range(1, 30)]
opcoes_28_dias = [f"{dia:02}" for dia in range(1, 29)]
