import {useState} from "react";
import axios from "axios";

const useLocalisation = () => {
    const [adress, setAdress] = useState("")

    const verifAdress = async () => {
        try{
            const response = await axios.get("http://localhost:8000/delivery/get-delivery-time", {
                params: {
                    address1: "25 Rue Claude Tillier, 75012 Paris",
                    address2: adress
                }
            })
            return response.data.can_order;
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