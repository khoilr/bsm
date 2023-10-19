import { Box } from "@chakra-ui/react";
import { ReactNode } from "react";
import { ControlBar, Player } from "video-react";

type VideoControllerProps = {
    children?: ReactNode,
}

function VideoController(props: VideoControllerProps) {
    return (
        <Box className="absolute top-0 left-0 z-1 w-full h-full flex flex-col justify-between" width={'full'} height={'full'}>
            <div className="w-full h-full hover:opacity-30 hover:bg-slate-500">
                <div className=" bg-white w-full"></div>
                <div className="h-5 bg-yellow-500 w-full"></div>

            </div>
            <div className=" bg-orange-500  w-full">

                {/* <audio className="w-full" controls /> */}


            </div>



        </Box>

    )
}
export default VideoController;