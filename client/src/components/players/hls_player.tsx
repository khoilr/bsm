import ReactPlayer from "react-player"

function HLSPlayer() {
    return (
        <div className="h-[600px] w-full flex flex-row justify-center items-center bg-gray-300">
            <ReactPlayer playing url={'/stream/playlist.m3u8'} controls config={{
                file: {
                    forceHLS: true,
                }
            }} />

            {/* <img className="w-[200px] h-[120px] object-contain" src="/images/monitor_placeholder.png" /> */}
        </div>
    )
}

export default HLSPlayer