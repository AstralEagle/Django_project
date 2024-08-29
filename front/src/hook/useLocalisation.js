import {useState} from "react";

const useLocalisation = () => {
    const [adress, setAdress] = useState("")

    const verifAdress = async () => {
        try{
            //TODO
            // call API pour voir si il est a moins de 20min
        }
        catch(error){
            console.error(error)
        }
        return false
    }

    return {
        adress,
        setAdress,
        verifAdress
    }
}

export default useLocalisation