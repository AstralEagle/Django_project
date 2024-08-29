import {useEffect, useState} from "react";


const useLivraison = () => {
    const [estimation, setEstimation] = useState(new Date())

    useEffect(() => {
        (async() =>  {
           try{
               const minutesAJouter = 20 * 60 * 1000;
                const now = new Date()
               setEstimation(new Date(now.getTime() + minutesAJouter))
           }
           catch(e){
               console.error(e)
           }
        })()
    }, []);

    return {estimation}
}

export default useLivraison;