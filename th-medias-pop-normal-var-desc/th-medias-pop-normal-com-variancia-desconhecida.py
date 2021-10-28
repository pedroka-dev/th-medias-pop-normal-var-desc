
from _typeshed import StrOrBytesPath
import statistics
import scipy.stats as stats
import math

def thMediaPopNormalSemVariancia(amostra, hipotese, alpha, operacao):
    n = len(amostra);
    media = statistics.mean(dadosAmostra);
    variancaAmostral = statistics.variance(dadosAmostra);
    phi = n-1;

    tCalc = (media - hipotese) / math.sqrt(variancaAmostral/n);
    if(operacao == "=/="):
        alpha = alpha/2;
    tPhiAlpha = stats.t.ppf(1-(alpha)/2, phi);  #T-Student

    print("==============================");
    print("Hipotese nula (h0): μ = " + str(hipotese));
    print("Hipotese alternativa (h1): μ "+  str(operacao) + " " + str(hipotese));   #!! MUDANÇA FEITA APÓS O VIDEO !!
    print("Elementos na amostra (n) = " + str(n));
    print("Media da amostra (x̄) = " + str(media));
    print("Varianca amostral (s²) = " + str(variancaAmostral));
    print("Phi (φ) = " + str(phi));

    print("==============================");
    print("Tcalc = " + str(tCalc));
    print("TPhiAlpha (Tφa) = " + str(tPhiAlpha));
    print("==============================");

    if(operacao == ">"): 
        ehAfirmacaoLegitima = tCalc > tPhiAlpha;
    elif(operacao == "<"):
        ehAfirmacaoLegitima = tCalc < -tPhiAlpha;
    elif(operacao == "=/="):
        ehAfirmacaoLegitima = (tCalc > tPhiAlpha) or (tCalc < -tPhiAlpha);  #alpha = alpha/2

    if(ehAfirmacaoLegitima):
        print("Temos evidências o suficiente ao nível de "+ str(alpha) + " para confirmar a afirmação.");
    else:
        print("Não temos evidencias suficientes ao nível de "+ str(alpha) + " para confirmar a afirmação.");


#TH para Médias de populações normais com variâncias desconhecidas 
# Exercício: A receita média, em porcentagem, dos quase 600 municípios de um estado tem sido de 7%.
# O governo pretende melhorar esse índice e, para isso, está estudando alguns incentivos. 
# Para verificar os efeitos desses incentivos, sorteou 10 cidades e estudou quais seriam as porcentagens investidas neles. 
# Os resultados foram, em porcentagem, 8, 10, 9, 11, 8, 12, 16, 9, 12, 13. 
# Admitindo-se que esses números realmente venham a ocorrer, os dados trazem evidência de melhoria ao nível de 5%? 

dadosAmostra = [8, 10, 9, 11, 8, 12, 16, 9, 12, 13];
hipoteseInicial = 0.07;
alpha = 0.05;
tipoOperacao = ">";
thMediaPopNormalSemVariancia(dadosAmostra,hipoteseInicial,alpha,tipoOperacao)



