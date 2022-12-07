```mermaid
	classDiagram

    
    class `Explanation` {
    
    }

    class `Counterfactual Explanation` {
    
    }

    class `Ontology` {
    
    }

    class `System Recommendation` {
    
    }

    class `SIO_000085` {
    
    }

    class `Object Record` {
    
    }

    class `Explanation Modality` {
    
    }

    class `ExplanationCollection` {
    
    }

    class `User` {
    
    }

    class `Explanation Goal` {
    
    }

    class `AI Method` {
    
    }

    class `Knowledge` {
    
    }



`Explanation`  --> `SIO_000085`   :addresses  

`System Recommendation`  --> `Object Record`   :SIO001277  

`Explanation`  --> `System Recommendation`   :is based on  

`Explanation`  --> `Explanation Modality`   :has presentation  

`ExplanationCollection`  --> `Explanation`   :SIO000059  

`User`  --> `Explanation`   :is consumer of  

`Explanation`  --> `Explanation Goal`   :SIO000008  

`System Recommendation`  --> `AI Method`   :SIO000232  

`Explanation`  --> `Knowledge`   :is based on  

```