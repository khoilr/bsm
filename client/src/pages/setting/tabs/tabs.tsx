import { MdAccountBox } from 'react-icons/md'
import { IoIosVideocam } from 'react-icons/io'
import { PiSpeakerSimpleNoneFill } from 'react-icons/pi'
import { HiMiniBellAlert } from 'react-icons/hi2'
import AccountTab from './account_tab';
import VideoTab from './video_tab';
import AudioTab from './audio_tab';
import AlertTab from './alert_tab';
export type TabItem = {
    title: string,
    icon: JSX.Element,
    component: JSX.Element,
}


const settingTabs: TabItem[] = [
    {
        title: 'Account',
        icon: <MdAccountBox />,
        component: <AccountTab />
    },
    {
        title: 'Video',
        icon: <IoIosVideocam />,
        component: <VideoTab />
    },
    {
        title: 'Audio',
        icon: <PiSpeakerSimpleNoneFill />,
        component: <AudioTab />
    },
    {
        title: 'Alert',
        icon: <HiMiniBellAlert />,
        component: <AlertTab />
    },

];

export default settingTabs;