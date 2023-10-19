
import React from 'react';
import { useEffect, useState } from 'react';
// @ts-ignore
import EZUIKit from 'ezuikit-js';
import { Skeleton } from '@chakra-ui/react';
import { env_vars } from '../../models/constants';
import API from '../../controllers/api/api';
import qs from 'qs';


type EzvizPlayerProps = {
    width: number,
    height: number,
    cameraURL: string,
}

function EzvizPlayer(props: EzvizPlayerProps) {
    const api = new API(env_vars.EZVIZ_END_POINT ?? '');
    const { width, height, cameraURL } = props;
    const [player, setPlayer] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);

    const getToken = async () => {
        const url = `/api/lapp/token/get`;
        const dataEncode = new URLSearchParams({
            appKey: 'bb9aa821c13944fbae1f916d0bb1307b',
            appSecret: '72ac899e28cd40c78697d146a19e05ae'
        }).toString();
        const respond = await fetch(env_vars.EZVIZ_END_POINT + url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: dataEncode,
        })

        console.log(dataEncode);
        // const respond = await api.post(url, {
        //     data: dataEncode,
        //     // headers: { 'content-type': 'application/x-www-form-urlencoded' },

        // });

        if (respond.status == 200) {
            const accessToken = (await respond.json()).data.accessToken;
            return String(accessToken) ?? '';
        }

        return '';
    }
    console.log("render eziz player");

    useEffect(() => {
        getToken().then((token) => {
            console.log('token: ' + token);
            const ezPlayer = new EZUIKit.EZUIKitPlayer({
                id: 'video-container',
                accessToken: token,
                url: cameraURL,
                template: 'mobileLive',
                plugin: ['talk'],
                deocoder: "",
                width: width,
                height: height,
                env: {
                    domain: "https://isgpopen.ezvizlife.com"
                }
            });
            setPlayer(ezPlayer);
            setIsLoaded(true);
        })

    }, [])
    return (

        <div className='flex justify-center w-full' id='video-container'>
            <Skeleton height={height} width={'full'} isLoaded={isLoaded}>

            </Skeleton>
        </div>

    )
}

export default EzvizPlayer;