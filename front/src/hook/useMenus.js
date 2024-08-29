import {useEffect, useState} from "react";

const defaultPlat1 = {id: 0, name: "Plat_1", price: 14.15, image: "https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/plat-familial-sans-four/97674744-2-fre-FR/15-recettes-de-plats-familiaux-sans-four.jpg"}
const defaultPlat2 = {id: 1, name: "Plat_2", price: 14.15, image: "https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/plat-familial-sans-four/97674744-2-fre-FR/15-recettes-de-plats-familiaux-sans-four.jpg"}
const defaultDessert1 = {id: 3, name: "Dessert_1", price: 14.15, image: "https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/plat-familial-sans-four/97674744-2-fre-FR/15-recettes-de-plats-familiaux-sans-four.jpg"}
const defaultDessert2 = {id: 4, name: "Dessert_2", price: 14.15, image: "https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/plat-familial-sans-four/97674744-2-fre-FR/15-recettes-de-plats-familiaux-sans-four.jpg"}

const useMenus = () => {
    const [menus, setMenus] = useState([]);
    const [desserts, setDesserts] = useState([]);

    useEffect(() => {
        (async () => {
            try {
                await setMenus([defaultPlat1, defaultPlat2]);
                await setDesserts([defaultDessert1, defaultDessert2]);
            }
            catch(e) {
                console.error(e)
            }
        })()
    }, []);

    return {menus, desserts}
}

export default useMenus;