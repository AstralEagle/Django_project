import {useState} from "react";
import {enqueueSnackbar} from "notistack";


const useMyMenus = () => {
    const [myMenus, setMyMenus] = useState([]);

    const addPlat = (menu) => {
        const isItem = myMenus.find(x => menu.id === x.id)
        if (isItem)
            enqueueSnackbar("Vous avez déja cette plat dans votre panier", {variant: "error"})
        else {
            setMyMenus([...myMenus, menu]);
            enqueueSnackbar("Vous avez ajouter l'article au panier", {variant: "success"})
        }

    }

    const removePlat = (removedMenu) => {
        setMyMenus(myMenus.filter(menu => removedMenu.id !== menu.id))
    }

    return {myMenus, addPlat, removePlat}
}

export default useMyMenus;