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

    class `n7f31b0829a9147eb8574a3f4ac73f94db13` {
    
    }

    class `n7f31b0829a9147eb8574a3f4ac73f94db16` {
    
    }

    class `n7f31b0829a9147eb8574a3f4ac73f94db19` {
    
    }



`n7f31b0829a9147eb8574a3f4ac73f94db13`  --> `Variable`   :input  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`n7f31b0829a9147eb8574a3f4ac73f94db19`  --> `Variable`   :output on error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`n7f31b0829a9147eb8574a3f4ac73f94db16`  --> `Variable`   :output  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Complete  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Error  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Direct Workflow Task`  --> `Direct Workflow Task`   :on Success  

`Task`  --> `Variable`   :output on error  

`Task`  --> `Variable`   :output on error  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`Reverse Workflow Task`  --> `Reverse Workflow Task`   :requires  

`Task`  --> `Variable`   :output  

`Task`  --> `Variable`   :input  

`Task`  --> `Variable`   :input  

`Task`  --> `Variable`   :output  

```