import React from 'react';
import {Box, IconButton, Typography} from "@mui/material";
import {Outlet, useNavigate} from "react-router-dom";
import {Receipt} from "@mui/icons-material";

function Template() {
    const navigate = useNavigate()

    const handleClickOpenCommande = () => {
        navigate('/commandes')
    }
    const handleClickOpenDefault = () => {
        navigate('/')
    }

    return (
        <Box className="flex-col flex" sx={{
            width: '100vw',
            height: '100vh',
        }}>
            <Box sx={{
                boxShadow: "0px 4px 4px #00000052",
                zIndex: 999,
            }} className=" flex justify-between p-2">
                <Typography className="cursor-pointer" onClick={handleClickOpenDefault} fontSize={48} fontWeight="bold" color="primary">
                    IPSSI Express Food
                </Typography>
                <IconButton onClick={handleClickOpenCommande}>

                    <Receipt/>
                </IconButton>
            </Box>
            <Box className="flex-1 flex justify-center w-[100%]" sx={{bgcolor: "#F0EDDC"}}>
                <Outlet/>
            </Box>
        </Box>
    );
}

export default Template;