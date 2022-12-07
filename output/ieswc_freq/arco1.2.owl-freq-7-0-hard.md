```mermaid
	classDiagram

    
    class `Bene culturale` {
    
    }

    class `Cartographic classification` {
    
    }

    class `Agent` {
    
    }

    class `Classificazione di bene fotografico` {
    
    }

    class `Bene Numismatico` {
    
    }

    class `SubjectDiscipline` {
    
    }

    class `Classificazione di strumento musicale` {
    
    }



`Bene culturale`  --> `SubjectDiscipline`   :ha disciplina principale  

`Agent`  --> `Bene culturale`   :is heritage protection agency of  

`SubjectDiscipline`  --> `Bene culturale`   :is main discipline of  

`Cartographic classification`  --> `Bene culturale`   :is cartographic classification of  

`Bene culturale`  --> `Agent`   :ha ente collegato  

`Agent`  --> `Bene culturale`   :is cataloguing agency of  

`Bene culturale`  --> `SubjectDiscipline`   :ha altra disciplina  

`Bene culturale`  --> `Agent`   :ha ente competente per la tutela  

`Bene culturale`  --> `Agent`   :ha ente schedatore  

`Bene culturale`  --> `Cartographic classification`   :ha classificazione cartografica  

`Agent`  --> `Bene culturale`   :is related agency of  

`SubjectDiscipline`  --> `Bene culturale`   :is alternative discipline of  

`Cartographic classification`  --> `Bene culturale`   :is cartographic classification of  

`Cartographic classification`  --> `Bene culturale`   :is cartographic classification of  

`Bene Numismatico`  --> `Bene Numismatico`   :ha categoria di bene numismatico  

`Bene Numismatico`  --> `Bene Numismatico`   :ha categoria di bene numismatico  

```