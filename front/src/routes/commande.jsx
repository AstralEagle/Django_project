import React, {useEffect, useState} from 'react';
import {Box, Typography} from "@mui/material";
import Cookie from "js-cookie";

function Commande() {

    const [commandes, setCommandes] = useState([])

    useEffect(() => {
        (async () => {
            const default_commande = Cookie.get("defaultTime")

            console.log(JSON.parse(default_commande))

            if (default_commande)
                setCommandes(await JSON.parse(default_commande))
        })()
    }, []);

    return (
        <Box className="py-2 flex flex-col gap-2">
            {commandes.map((commande, i) => (
                <Box
                    key={i}
                    sx={{
                        bgcolor: "white"
                    }}
                    className="p-2 rounded-md"
                >
                    <Typography fontWeight={700}>
                        Commande du {commande.date}
                    </Typography>
                    <Typography>
                        A l'adresse "{commande.address}"
                    </Typography>
                    <Box className="p-2">
                        {commande.commande.map((x, i) => (
                            <Box>
                                <Typography> - {x.name}</Typography>
                            </Box>
                        ))}
                    </Box>
                </Box>
            ))}
            {commandes.length == 0 && (
                <Typography>
                    Pas d'ancienne commande
                </Typography>
            )}
        </Box>
    );
}

export default Commande;