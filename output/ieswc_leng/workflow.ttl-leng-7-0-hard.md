```mermaid
	classDiagram

    
    class `Reverse Workflow` {
    
    }

    class `Direct Workflow` {
    
    }

    class `Workflow` {
    
    }

    class `Variable` {
    
    }

    class `Task` {
    
    }

    class `Direct Workflow Task` {
    
    }

    class `Reverse Workflow Task` {
    
    }



`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Task`  --> `Variable`   :output on error  

`Task`  --> `Variable`   :output on error  

`Workflow`  --> `Variable`   :output  

`Workflow`  --> `Variable`   :output  

`Task`  --> `Variable`   :input  

`Task`  --> `Variable`   :input  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`Task`  --> `Variable`   :output  

`Task`  --> `Variable`   :output  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Workflow`  --> `Variable`   :input  

`Workflow`  --> `Variable`   :output on error  

`Workflow`  --> `Variable`   :input  

`Workflow`  --> `Variable`   :output on error  

```