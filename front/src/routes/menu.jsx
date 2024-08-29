import React, {useEffect, useState} from 'react';
import {Box, Button, Typography} from "@mui/material";
import useMenus from "../hook/useMenus.js";
import useMyMenus from "../hook/useMyMenus.js";

const Plat = ({plat, addToMyMenu}) => {
    return (<Box className="flex flex-col cursor-pointer" onClick={() => addToMyMenu(addToMyMenu)}>
        <Box className="flex justify-between items-center">
            <Typography>
                {plat.name}
            </Typography>
            <Typography>
                {plat.price} €
            </Typography>
        </Box>
        <img
            src={plat.image}
            alt="Image du plat"
            style={{
                width: "337px", height: "200px"
            }}
        />
    </Box>)
}


function Menu() {

    const {menus, desserts} = useMenus()
    const {myMenus, addPlat, removePlat} = useMyMenus()
    const [totalCommande, setTotalCommande] = useState(0)

    useEffect(() => {
        setTotalCommande(myMenus.reduce((acc, cur) => acc + cur.price, 0))
    }, [myMenus]);


    return (
        <Box className="max-w-[1400px] p-2">
        <Typography fontSize={48} fontWeight={800}>
            Plat
        </Typography>
        <Box className="flex flex-col md:flex-row  gap-3">
            {menus.map((plat, i) => (<Plat key={i} plat={plat} addToMyMenu={() => addPlat(plat)}/>))}
        </Box>
        <Typography fontSize={48} fontWeight={800}>
            Dessert
        </Typography>
        <Box className="flex flex-col md:flex-row  gap-3">
            {desserts.map((plat, i) => (<Plat key={i} plat={plat} addToMyMenu={() => addPlat(plat)}/>))}
        </Box>
        <Box className="flex flex-col mt-4">
            <Typography fontSize={48} fontWeight={800}>
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
                    <Button variant="contained">Commander</Button>
                </Box>
            </Box>
        </Box>
    </Box>);
}

export default Menu;