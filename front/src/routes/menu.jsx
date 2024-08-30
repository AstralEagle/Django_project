import React, {useEffect, useState} from 'react';
import {Box, Button, Typography} from "@mui/material";
import useMenus from "../hook/useMenus.js";
import useMyMenus from "../hook/useMyMenus.js";
import {useSelector} from "react-redux";
import {useNavigate} from "react-router-dom";
import adress from "../store/adress.js";

import Cookie from "js-cookie"

const Plat = ({plat, addToMyMenu}) => {
    return (<Box className="flex flex-col cursor-pointer max-w-[337px]" onClick={() => addToMyMenu(addToMyMenu)}>
        <Box className="flex justify-between items-center gap-2">
            <Typography>
                {plat.name}
            </Typography>
            <Typography>
                {plat.price}€
            </Typography>
        </Box>
        <img
            src={plat.image}
            alt="Image du plat"
            style={{
                width: "337px", height: "180px"
            }}
        />
    </Box>)
}


function Menu() {

    const address = useSelector((state) => state.address.address);
    const navigate = useNavigate();

    const {menus, desserts} = useMenus()
    const {myMenus, addPlat, removePlat} = useMyMenus()
    const [totalCommande, setTotalCommande] = useState(0)

    useEffect(() => {
        if (!address)
            navigate("/")
    }, []);

    useEffect(() => {
        setTotalCommande(myMenus.reduce((acc, cur) => acc + cur.price, 0))
    }, [myMenus]);

    const handleClickOpenLivraison = async () => {
        const commande = {
            commande: myMenus.map(x => ({name: x.name, id: x.id})),
            address: address,
            date: new Date().toLocaleDateString()
        }
        const default_commande = Cookie.get("defaultTime")
        const commandes = default_commande  ? await JSON.parse(default_commande) : []
        Cookie.set('defaultTime', JSON.stringify([...commandes, commande]))

        navigate('/livraison')
    }

    if (adress)
        return (
            <Box className="max-w-[1400px] p-2 gap-2 flex flex-col">
                <Box>
                    <Typography fontSize={48} fontWeight={800} lineHeight="48px">
                        Plat
                    </Typography>
                    <Box className="flex flex-col md:flex-row  gap-3">
                        {menus.map((plat, i) => (<Plat key={i} plat={plat} addToMyMenu={() => addPlat(plat)}/>))}
                    </Box>
                </Box>
                <Box>

                    <Typography fontSize={48} fontWeight={800} lineHeight="48px">
                        Dessert
                    </Typography>
                    <Box className="flex flex-col md:flex-row  gap-3">
                        {desserts.map((plat, i) => (<Plat key={i} plat={plat} addToMyMenu={() => addPlat(plat)}/>))}
                    </Box>
                </Box>
                <Box className="flex flex-col mt-4">
                    <Typography fontSize={48} fontWeight={800} lineHeight="48px">
                        Total
                    </Typography>
                    <Box className="flex gap-4 flex-col md:flex-row">
                        <Box className="flex flex-col flex-1 gap-2">
                            {myMenus.map((plat, i) => (<Box key={i} className="flex items-center gap-2">
                                <Typography className="flex-1">
                                    {plat.name}
                                </Typography>
                                <Typography>
                                    {plat.price} €
                                </Typography>
                                <Button size="small" variant="contained" color="error" onClick={() => removePlat(plat)}>
                                    Remove
                                </Button>
                            </Box>))}
                        </Box>
                        <Box className="min-w-[150px] flex-col flex justify-center">
                            <Box className="flex justify-between gap-2">
                                <Typography>
                                    Commande:
                                </Typography>
                                <Typography>
                                    {totalCommande} €
                                </Typography>
                            </Box>
                            <Box className="flex justify-between gap-2">
                                <Typography>
                                    Livraison:
                                </Typography>
                                <Typography>
                                    {totalCommande > 19.99 ? 0 : 5} €
                                </Typography>
                            </Box>
                            <Box sx={{height: "30px"}}/>
                            <Box className="flex justify-between gap-2">
                                <Typography>
                                    Total:
                                </Typography>
                                <Typography>
                                    {(totalCommande > 19.99 ? 0 : 5) + totalCommande} €
                                </Typography>
                            </Box>
                            <Button variant="contained" onClick={handleClickOpenLivraison}
                                    disabled={!(myMenus.length > 0)}>Commander</Button>
                        </Box>
                    </Box>
                </Box>
            </Box>);
    else
        return (
            <Box/>
        )
}

export default Menu;