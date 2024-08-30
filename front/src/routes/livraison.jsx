import React, {useEffect} from 'react';
import {Box, Typography} from "@mui/material";
import useLivraison from "../hook/useLivraison.js";
import {useSelector} from "react-redux";
import {useNavigate} from "react-router-dom";

function Livraison(props) {
    const address = useSelector((state) => state.address.address);
    const navigate = useNavigate();
    const {estimation} = useLivraison()

    useEffect(() => {
        if(!address)
            navigate("/")
    }, []);

    if (address)
        return (
            <Box className="max-w-[1400px] p-2 flex flex-col gap-5">
                <Box className="p-[20px] max-w-[600px] flex flex-col items-center gap-2"
                     sx={{
                         bgcolor: "rgba(255, 255, 255, 75%)",
                         borderRadius: "5px",
                     }}
                >
                    <Typography>
                        Un de nos livreur se dirige vers {address}
                    </Typography>
                </Box>
                <Box className="p-[20px] max-w-[600px] flex flex-col items-center gap-2"
                     sx={{
                         bgcolor: "rgba(255, 255, 255, 75%)",
                         borderRadius: "5px",
                     }}
                >
                    <Typography>
                        Estimation de l'heure d'arrivé : {estimation.toLocaleTimeString()}
                    </Typography>
                </Box>
            </Box>
        );
    return (<Box></Box>)
}

export default Livraison;