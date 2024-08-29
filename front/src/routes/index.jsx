import React from 'react';
import {Box, Button, TextField, Typography} from "@mui/material";
import backgroundImage from '/background.webp'

function Index() {
    return (
        <Box
            className="h-[100%] w-[100%] flex justify-center items-center p-4"
            sx={{
                backgroundImage: `url(${backgroundImage})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
            }}
        >
            <Box className="p-[20px] max-w-[600px] flex flex-col items-center gap-2"
                 sx={{
                     bgcolor: "rgba(255, 255, 255, 75%)",
                    borderRadius: "5px",
                 }}
            >
                <Typography fontSize={20}>
                    Votre adresse
                </Typography>
                <Typography sx={{textAlign: "center"}}>
                    Veuillez entrer votre adresse ci-dessous pour vérifier si vous êtes éligible à la livraison. Si
                    votre adresse se trouve à moins de 20 minutes à vélo de 1 Avenue de Paris
                </Typography>
                <Box className="flex gap-1 flex-col md:flex-row" sx={{width: '100%'}}>
                    <TextField variant="outlined" className="flex-1"/>
                    <Button>Go</Button>
                </Box>

            </Box>
        </Box>
    );
}

export default Index;