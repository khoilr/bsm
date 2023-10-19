import { StreamType } from "../constants";

const cameras = [
    {
        id: '00001',
        name: "1C Innovation - Ezviz",
        zoneId: '00001',
        zoneName: 'Zone 1',
        uri: 'ezopen://open.ezviz.com/BA3686955/1.hd.live',
        type: StreamType.EZVIZ,
    },
    {
        id: '00002',
        name: "1C Innovation - Hanet",
        zoneId: '00001',
        zoneName: 'Zone 1',
        uri: 'ws://127.0.0.1:8000/',
        type: StreamType.SOCKET,
    },
    {
        id: '00003',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },
    {
        id: '00004',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },
    {
        id: '00005',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },
    {
        id: '00006',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },
    {
        id: '00007',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },
    {
        id: '00008',
        name: "Camera Default",
        zoneId: '00002',
        zoneName: 'Zone 2',
        uri: '',
        type: StreamType.DEFAULT,
    },

];

export default cameras;