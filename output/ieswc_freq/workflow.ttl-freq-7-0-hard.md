```mermaid
	classDiagram

    
    class `Direct Workflow Task` {
    
    }

    class `Variable` {
    
    }

    class `Reverse Workflow Task` {
    
    }

    class `Task` {
    
    }

    class `n4a00967428fe43e798eca9a602073717b13` {
    
    }

    class `n4a00967428fe43e798eca9a602073717b16` {
    
    }

    class `n4a00967428fe43e798eca9a602073717b19` {
    
    }



`Task`  --> `Variable`   :input  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`n4a00967428fe43e798eca9a602073717b19`  --> `Variable`   :output on error  

`Task`  --> `Variable`   :output on error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Task`  --> `Variable`   :output  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`n4a00967428fe43e798eca9a602073717b16`  --> `Variable`   :output  

`n4a00967428fe43e798eca9a602073717b13`  --> `Variable`   :input  

```