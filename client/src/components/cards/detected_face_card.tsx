import { IoMdPerson } from 'react-icons/io';
import { MdCamera } from 'react-icons/md'

type DetectedFaceCardProps = {

}

function DetectedFaceCard(props: DetectedFaceCardProps) {
    return (
        <div className="flex min-w-[240px] flex-col items-start p-2 space-y-1 shadow-[0_0_4px_0px_rgba(0,0,0,0.25)] rounded">
            <img className="w-[240px h-[160px] object-cover m-0" src="/images/detected_face.png" />
            <span className=' text-[12px] font-light text-black'>03.10.2023 - 09:00 AM</span>
            <div className="flex flex-row justify-start space-x-2 items-center ">
                <IoMdPerson color='#9B4444' size={16} />
                <span className='text-[12px] font-bold text-black'>KhoiCLM</span>
            </div>
            <div className="flex flex-row justify-start space-x-2 items-center">
                <MdCamera size={16} />
                <span className='text-[12px] font-bold text-black'>CAM_LAU_1</span>
            </div>
        </div>
    );
}

export default DetectedFaceCard;