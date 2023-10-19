
import ReactPlayer from "react-player";
import PageTitle from "../../../components/headings/PageTitle";
import ContentLayout from "../../../components/layouts/content_layout";
import HLSPlayer from "../../../components/players/hls_player";
import { useSearchParams } from "react-router-dom";

import EzvizPlayer from "../../../components/players/ezviz_player";
import SocketPlayer from "../../../components/players/socket_player";

function DeviceDetailPage() {
    const [searchParams, setSearchParams] = useSearchParams();

    const type = searchParams.get('type') ?? '';
    const liveUrl = searchParams.get('url');
    console.log("type:" + type);
    console.log("url:" + liveUrl);
    return (
        <ContentLayout>
            <PageTitle>Devices</PageTitle>

            <div className="flex flex-col p-4 bg-white w-full flex-grow items-start space-y-2">
                <div className="flex justify-center w-full min-h-[400px]">
                    {type === 'default' && <HLSPlayer />}
                    {type === 'ezviz' && <EzvizPlayer width={600} height={400} cameraURL={liveUrl ?? ''} />}
                    {type === 'socket' && <SocketPlayer socketURL={liveUrl ?? ''} />}
                </div>

                <div className="flex flex-col items-start">
                    <h3>Camera A</h3>
                    <span className="text-[#28AA73] text-sm font-bold">Zone A- Zone B</span>
                    <div className="flex flex-row items-center">
                        <span className="text-black font-bold text-base mr-2">Description:</span>
                        <p className="m-0 text-black font-light text-sm">Camera Description</p>
                    </div>

                </div>

            </div>
        </ContentLayout>

    )
}

export default DeviceDetailPage;