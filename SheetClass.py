# Montando uma ficha de personagem, Alem de montar um dicionario para os modificadores
# a classe esta em ingles e os inputs brutos em portugues pois é mais facil para nos trabalharmos em portugues, mas como o dnd api é em ingles, pensei em dar consistencia
# ao projeto deixando em ingles
ModDic = {
    6:-2,
    7:-2,
    8:-1,
    9:-1,
    10:0,
    11:0,
    12:1,
    13:1,
    14:2,
    15:2,
    16:3,
    17:3,
    18:4,
    19:4,
    20:5
}
# A classe character sheet permite a gente não só criar uma classe e publica-la mais facil, como tambem permite no fututo fazer açoes simples envolvendo a propria ficha
# como por exemplo, fazer um codigo onde a ficha upa de level apenas com uma funçao, ou até mesmo criar ações simples como "atacar" e coisa do tipo

# explicando os inputs: rawstats pode ser um dicionario que tem como keys, força, destreza, constituiçao, inteligencia, sabedoria e carisma
# tambem cria o modificador baseado no dicionario criado acima NOTA-SE: neste modelo atual, devemos incluir no rawstats os bonus de stats que a raça proporciona

# penso que rawclass pode ser um dicionario que recebe informações como o hitdie para hp, as proficiencias separadas em categorias
# skills que foram selecionadas aleatoriamente, magias, equipamentos e habilidades de level 1, preferencialmente em formato de lista,

# rawrace pode ser tambem um dicionario das informações relevantes da raça, como nome da subclasse, lista de proficiencias, skills e magias concedidas

# rawbackground tambem sera um dicionario contendo coisas como equipamentos, proficiencias, skills e o que mais for dado por causa de background

# sem ideias de como definir a armor class da ficha, ja que ela depende de diversos fatores como que tipo de armadura é usada, ou regras especificas de classe


class CharSheet{
    def __init__(rawstats, rawclass, rawrace, rawbackground){
        self.name = # Aqui vai vir a integração com api de nomes aleatorios
        # para deixar o jogador mais informado, aqui colocaremos o nome da classe e subclasse(se tiver) e tambem nome da raça e subraça e tambem do background
        self.classname = rawclass[nome] + rawclass[subclasse]
        self.racename = rawrace[name] + rawrace[subraca]
        self.backgroundname = rawbackground[name]
        #Velocidade é definido pela raça
        self.speed = rawrace[velocidade]
        #stats é um dicionario, contendo cada stat, que é um dicionario contendo o modificador e o valor bruto
        self.stats = {strength : {value: rawstats[forca],modifier: ModDic[rawstats[forca]],

                      dexterity : {value: rawstats[destreza], modifier: ModDic[rawstats[destreza]],

                      constitution : {value : rawstats[constituicao], modifier: ModDic[rawstats[constituicao]],

                      intelligence : {value : rawstats[inteligencia], modifier: ModDic[rawstats[inteligencia]],

                      wisdom : {value : rawstats[sabedoria], modifier: ModDic[rawstats[sabedoria]],

                      charisma : {value : rawstats[carisma], modifier: ModDic[rawstats[carisma]]
                      }}}}}}}
        # o valor de vida maxima no lvl 1 é o "hit die" da classe + o modificador de constituição
        self.HP = rawclass[HP] + self.stats[constitution][modifier]
        # modificador de proficiencia lvl 1 é 2
        self.profMod = 2
        # um dicionario de todas as categorias de proficiencia(que me lembro), a ideia é concatenar as listas de proficiencias que a classe, raça e background concedem
        self.savingthrows = rawclass[savingthrows]
        self.proficiencies = {weapons : rawclass[proficiencia][armas] + rawrace[proficiencia][armas] + rawbackground[proficiencia][armas],
                              armor : rawclass[proficiencia][armadura] + rawrace[proficiencia][armadura] + rawbackground[proficiencia][armadura],
                              tools : rawclass[proficiencia][ferramentas] + rawrace[proficiencia][ferramentas] + rawbackground[proficiencia][ferramentas],
                              languages : rawclass[proficiencia][linguas] + rawrace[proficiencia][linguas] + rawbackground[proficiencia][linguas]}
        # uma simples concatenação de listas vindas de rawclass, rawrace e rawbackground, contendo as skills recebidas e escolhidas
        self.skills = rawclass[skills] + rawrace[skills] + rawbackground[skills]
        # um dicionario de equipamento separado em categorias, como raças não provem equipamentos é diferente de proficiencia,
        # tambem possui a categoria "outros", para qualquer coisa avulsa
        self.equipments = {weapons : rawclass[equipamento][armas] + rawbackground[equipamento][armas],
                           armor : rawclass[equipamento][armadura] + rawbackground[equipamento][armadura],
                           tools : rawclass[equipamento][ferramentas] + rawbackground[equipamento][ferramentas],
                           other : rawclass[equipamento][outros] + rawbackground[equipamento][outros]}
        # magias podem ser tanto vindas de classe quanto de raça, no nivel 1, apenas é possivel ter truque e magias de lvl1, porem nem todas as raças e classes possuem magia
        self.spells = {cantrips : rawclass[magia][truque] + rawrace[magia][truque],
                       level1 : rawclass[magia][nivel1] + rawrace[magia][nivel1]}
    }
    #creio que seja tudo isso para a criação de uma ficha, a partir de agora apenas precisamos coletar dados. Qualquer mudança necessária, adicionar coisas, remover coisas ou até
    # mesmo recriar a classe para conveniencia, vão em frente
    
    #criar uma funcao que printa a classe
    def PrintSheet(){
        output = f'''
        Name:{self.name}                                        Health:{self.HP}
        Class:{self.classname}                                  Speed:{self.speed}
        Race:{self.racename}                                    Proficiency:{self.profMod}
        Background:{self.backgroundname}

        Stats:                                                  Strength: {self.stats[strength][value]}({self.stats[strength][modifier]})
                                                               Dexterity: {self.stats[dexterity][value]}({self.stats[dexterity][modifier]})
                                                            Constitution: {self.stats[constitution][value]}({self.stats[constitution][modifier]})
                                                            Intelligence: {self.stats[intelligence][value]}({self.stats[intelligence][modifier]})
                                                                  Wisdom: {self.stats[wisdom][value]}({self.stats[wisdom][modifier]})
                                                                Charisma: {self.stats[charisma][value]}({self.stats[charisma][modifier]})

        Saving Throws: {self.savingthrows}

        Skills: {self.skills}

        Proficiency: {self.proficiencies}
        
        Equipment: {self.equipments}

        Spells: {self.spells}
        '''
        print(output)

        return output
    }
}