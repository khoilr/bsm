import { FaCalendarAlt } from 'react-icons/fa';
import { FaBolt } from 'react-icons/fa6';
import { IoMdPerson } from 'react-icons/io';
import { MdCamera } from 'react-icons/md'
function ActivityCard() {
    return (
        <div className="flex flex-col items-start rounded-lg p-2 shadow-[0_0_4px_0px_rgba(0,0,0,0.25)] space-y-[6px]">
            <img className="w-[240px] h-[160px] object-cover m-0" src="/images/activity_palceholder.jpeg" />
            <div className='flex flex-row justify-between items-center w-full'>
                <div className='flex justify-start space-x-4 items-center'>
                    <FaCalendarAlt color='#004CBD' />
                    <span className='flex-grow text-black text-[14px] font-bold'>Time</span>
                </div>

                <span>03.10.2023 - 09:00 AM</span>
            </div>
            <div className='flex flex-row justify-between items-center w-full'>
                <div className='flex justify-start space-x-4 items-center'>
                    <IoMdPerson color='#9B4444' />
                    <span className='flex-grow text-black text-[14px] font-bold'>KhoiLCM</span>

                </div>
                <span>63.07%</span>
            </div>
            <div className='flex flex-row justify-start items-start space-x-4 w-full'  >
                <FaBolt color='#FFE711' />
                <div className='flex flex-col items-start space-y-2'>
                    <span className=' text-black text-[14px] font-bold'>Actions</span>
                    <div className='flex flex-row'>
                        <span className='bg-green-400 pt-1 text-white px-2 rounded-full'>check-in</span>
                    </div>
                </div>

            </div>
            <div className='flex flex-row justify-start items-center space-x-4  '>
                <MdCamera color='black' />
                <span className=' text-black text-[14px] font-bold'>CAM_LAU_1</span>
            </div>
            <button className=' w-full flex items-center justify-center  rounded-lg pt-2 pb-1 bg-[#7D9CB7] text-white'>
                Details
            </button>


        </div>
    )
}

export default ActivityCard;