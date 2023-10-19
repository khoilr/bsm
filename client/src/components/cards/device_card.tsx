
import { BiSolidCctv } from 'react-icons/bi';
import { MdLocationPin } from 'react-icons/md';
import { Link } from 'react-router-dom';
import { StreamType } from '../../models/constants';


type DeviceCardProps = {
    streamType?: StreamType,
    uri?: string,
    displayName?: string,
    zone?: string
}

function DeviceCard(props: DeviceCardProps) {
    const { streamType, uri, displayName, zone } = props;
    let paramsPostfix = '?';
    switch (streamType) {
        case StreamType.EZVIZ:
            paramsPostfix += 'type=ezviz';
            paramsPostfix += '&url=' + encodeURIComponent('ezopen://open.ezviz.com/BA3686955/1.hd.live');
            break;
        case StreamType.SOCKET:
            paramsPostfix += 'type=socket';
            paramsPostfix += '&url=' + encodeURIComponent('ws://127.0.0.1:8000/');
            break;
        default:
            paramsPostfix += 'type=default';
            break;
    }
    paramsPostfix += '&url=' + encodeURIComponent(uri ?? '');

    return (
        <Link className='text-link' to={'/device/detail' + paramsPostfix} >
            <div className="flex flex-col w-[200px] space-y-2 p-[10px] rounded-[10px] border-gray-200 border m-2">
                {<img className='w-full h-24 object-cover m-0' src="./images/cctv_background.png" />}
                <div className='flex flex-row justify-start items-center space-x-1'>
                    <BiSolidCctv />
                    <span className='truncate font-semibold'>{displayName}</span>
                </div>
                <div className='flex flex-row justify-start items-center space-x-1'>
                    <MdLocationPin color='red' />
                    <span className='truncate'>{zone}</span>
                </div>
            </div>
        </Link>
    )
}

export default DeviceCard;