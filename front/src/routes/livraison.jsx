import React from 'react';
import {Box, Typography} from "@mui/material";
import useLivraison from "../hook/useLivraison.js";

function Livraison(props) {

    const {estimation} = useLivraison()
    return (
        <Box className="max-w-[1400px] p-2 flex flex-col gap-5">
            <Box className="p-[20px] max-w-[600px] flex flex-col items-center gap-2"
                 sx={{
                     bgcolor: "rgba(255, 255, 255, 75%)",
                     borderRadius: "5px",
                 }}
            >
                <Typography>
                    Adress
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
}

export default Livraison;