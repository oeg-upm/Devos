```mermaid
	classDiagram

    
    class `File` {
    
    }

    class `Software` {
    
    }

    class `Software Directory` {
    
    }

    class `Service Module Version` {
    
    }

    class `Service Module` {
    
    }

    class `Auto Install Package` {
    
    }

    class `n47d99d32f16f42fbbd132fb6e1747a42b1` {
    
    }



`File`  --> `n47d99d32f16f42fbbd132fb6e1747a42b1`   :file type  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Service Module`  --> `Service Module Version`   :has version  

`Software`  --> `File`   :released as file  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`Software Directory`  --> `Software Directory`   :parent directory  

`File`  --> `Software Directory`   :in software directory  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Service Module`  --> `Service Module Version`   :has version  

`Service Module`  --> `Service Module Version`   :has version  

`Software`  --> `Software Directory`   :in software directory  

`Software`  --> `Software Directory`   :in software directory  

`Software`  --> `File`   :released as file  

`Software`  --> `File`   :released as file  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`Software Directory`  --> `Software Directory`   :parent directory  

`Software Directory`  --> `Software Directory`   :parent directory  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

```