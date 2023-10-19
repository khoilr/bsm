import { Avatar } from "@chakra-ui/react";
import PageTitle from "../../../components/headings/PageTitle";
import ContentLayout from "../../../components/layouts/content_layout";
import HLSPlayer from "../../../components/players/hls_player";
import { FaCalendarAlt } from 'react-icons/fa';
import { FaBolt } from 'react-icons/fa6';
import { IoMdPerson } from 'react-icons/io';
import { MdCamera } from 'react-icons/md'
function ActionDetailPage() {
    return (
        <ContentLayout>
            <PageTitle>Actions</PageTitle>

            <div className="flex flex-col p-4 bg-white w-full flex-grow items-start space-y-2">
                <HLSPlayer />
                <div className="flex flex-col items-start">
                    <div className='flex flex-row justify-between items-start w-full space-x-4'>
                        <FaCalendarAlt color='#004CBD' />
                        <span className='flex-grow text-black text-[14px] font-bold'>Time</span>

                        <span>03.10.2023 - 09:00 AM</span>
                    </div>
                    <div className='flex flex-row items-start w-full space-x-4'>
                        <IoMdPerson color='#9B4444' />
                        <div className='flex flex-col justify-start items-start'>
                            <span className='flex-grow text-black text-[14px] font-bold'>Person</span>
                            <div className="flex flex-wrap ml-4">
                                <div className="flex flex-col items-center">
                                    <Avatar size={'md'} />
                                    <span className='flex-grow text-black text-[14px] font-bold'>KhoiLCM</span>
                                    <span>63.07%</span>
                                </div>
                            </div>


                        </div>

                    </div>
                    <div className='flex flex-row justify-start items-center space-x-4 w-full'  >
                        <FaBolt color='#FFE711' />
                        <span className=' text-black text-[14px] font-bold mr-10'>Actions</span>
                        <span className='bg-green-400 pt-1 text-white px-2 rounded-full'>check-in</span>

                    </div>
                    <div className='flex flex-row justify-start items-center space-x-4  '>
                        <MdCamera color='black' />
                        <span className=' text-black text-[14px] font-bold'>CAM_LAU_1</span>
                    </div>

                </div>

            </div>
        </ContentLayout>
    )
}

export default ActionDetailPage;