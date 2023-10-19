
import { useEffect, useState } from "react";
import VideoController from "./video_controller";
import ClientSocket from "../../models/socket/socket";
import { Skeleton } from "@chakra-ui/react";

type SocketPlayerProps = {
    socketURL: string,
}

const INTERVAL_TIME = 20;
function SocketPlayer(props: SocketPlayerProps) {
    const { socketURL } = props;
    const [isCameraLoaded, setCameraLoaded] = useState(false);
    const socket = new ClientSocket(socketURL, {
        path: "/ws/socket.io",
        autoConnect: false,
    });


    const [socketImageUrl, setSocketImageUrl] = useState('');
    let breakCount = 0;
    const onMessageReceive = (msg: string) => {
        if (msg.indexOf('connected') >= 0) {
            socket?.emit('live_data', "please send data");
            setCameraLoaded(true);
        }
        if (msg.indexOf('data') >= 0) {

            const receivedJson = JSON.parse(msg);
            if (receivedJson.type === 'base64') {
                console.log('data receive');
                const data = receivedJson.data;
                const imageUrl = 'data:image/jpeg;base64,' + data;
                setSocketImageUrl(imageUrl);
            }
        }
    }

    useEffect(() => {
        socket.addListener('message', onMessageReceive);
        // start socket
        socket.connect();
        return () => {
            console.log("call clean up");
            socket.disconnect()
        };
    }, [
    ])

    // useEffect(() => {

    //     if (socketURL && socketURL.length > 0) {
    //         try {
    //             console.log("Init web socket client");
    //             const socket = new WebSocket(socketURL);
    //             socket.onmessage = function (event) {
    //                 console.log('data receive');
    //                 if(breakCount<INTERVAL_TIME){
    //                     ++breakCount;
    //                 }else{
    //                     const imageUrl = 'data:image/jpeg;base64,' + event.data;
    //                     // TODO: handle data when receive
    //                     // document.getElementById('imageElement').src = imageUrl;
    //                     setSocketImageUrl(imageUrl);
    //                     //reset count
    //                     breakCount=0;
    //                 }

    //             };
    //             socket.onclose=(e)=>{
    //                 console.log("Socket close");
    //             }
    //             console.log("COnnect successfull")
    //             return () => socket.close();
    //         } catch (error) {
    //             console.log("Error connect socket");
    //         }
    //     }


    // },[]);
    return (
        <div className="relative">
            <Skeleton isLoaded={isCameraLoaded}>
                <img className="m-0 w-full h-full object-contain z-0" src={socketImageUrl} />
            </Skeleton>

            {/* <VideoController /> */}
        </div>
    )
}

export default SocketPlayer