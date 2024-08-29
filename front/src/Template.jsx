import React from 'react';
import {Box, Typography} from "@mui/material";
import {Outlet} from "react-router-dom";

function Template() {
    return (
        <Box className="flex-col flex" sx={{
            width: '100vw',
            height: '100vh',
        }}>
            <Box sx={{
                boxShadow: "0px 4px 4px #00000052",
                zIndex: 999,
            }}>
                <Typography fontSize={48} fontWeight="bold" color="primary">
                    IPSSI Express Food
                </Typography>
            </Box>
            <Box className="flex-1 flex justify-center w-[100%]" sx={{bgcolor: "#F0EDDC"}}>
                <Outlet/>
            </Box>
        </Box>
    );
}

export default Template;