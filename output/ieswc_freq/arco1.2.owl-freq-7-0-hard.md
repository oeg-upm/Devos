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

    class `Subject Discipline` {
    
    }

    class `Cartographic symbol` {
    
    }



`Cartographic classification`  --> `Cartographic symbol`   :ha simbolo cartografico  

`Subject Discipline`  --> `Bene culturale`   :is alternative discipline of  

`Bene culturale`  --> `Subject Discipline`   :ha disciplina principale  

`Bene culturale`  --> `Cartographic classification`   :ha classificazione cartografica  

`Bene culturale`  --> `Agent`   :ha ente schedatore  

`Agent`  --> `Bene culturale`   :is cataloguing agency of  

`Cartographic classification`  --> `Bene culturale`   :is cartographic classification of  

`Agent`  --> `Bene culturale`   :is heritage protection agency of  

`Bene culturale`  --> `Subject Discipline`   :ha altra disciplina  

`Bene Numismatico`  --> `Bene Numismatico`   :ha categoria di bene numismatico  

`Bene culturale`  --> `Agent`   :ha ente competente per la tutela  

`Bene culturale`  --> `Agent`   :ha ente collegato  

`Cartographic symbol`  --> `Cartographic classification`   :is cartographic symbol of  

`Agent`  --> `Bene culturale`   :is related agency of  

`Subject Discipline`  --> `Bene culturale`   :is main discipline of  

```