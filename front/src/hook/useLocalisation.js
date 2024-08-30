import {useState} from "react";
import axios from "axios";
import {useDispatch} from "react-redux";
import {setAddress} from "../store/adress.js";

const useLocalisation = () => {
    const [adress, setAdress] = useState("")
    const dispatch = useDispatch();

    const verifAdress = async () => {
        try {
            const response = await axios.get("http://localhost:8000/delivery/get-delivery-time", {
                params: {
                    address1: "25 Rue Claude Tillier, 75012 Paris",
                    address2: adress
                }
            })
            if (response.data.can_order)
                await dispatch(setAddress(adress))
            return response.data.can_order;
        } catch (error) {
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